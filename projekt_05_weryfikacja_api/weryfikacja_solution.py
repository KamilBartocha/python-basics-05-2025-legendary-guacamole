# weryfikacja_solution.py - Projekt 05: Weryfikacja migracji API
#
# Firma migruje z legacy systemu (eksport XML) na nowe REST API (JSON).
# Tester musi weryfikowac, ze oba zrodla zwracaja te same dane.
# Twoj skrypt porownuje oba formaty i generuje raport rozbieznosci.
#
# Uruchomienie: python3 weryfikacja_solution.py

import json
import xml.etree.ElementTree as ET

JSON_FILE = "products.json"
XML_FILE = "products.xml"


# ─── Zadanie 1 ─ Klasa ReadJson: wczytywanie i nawigacja po JSON ──────────────
class ReadJson:
    """Reads a JSON file and provides path-based value access."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load(self):
        try:
            with open(self.filepath, encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"ReadJson: file not found: {self.filepath}")
        except json.JSONDecodeError as e:
            print(f"ReadJson: invalid JSON in {self.filepath}: {e}")

    def get(self, path):
        current = self.data
        for part in path.split("."):
            if not isinstance(current, dict):
                return None
            current = current.get(part)
        return current

    def get_all(self, path):
        parts = path.split(".")
        current = self.data
        for part in parts[:-1]:
            if not isinstance(current, dict):
                return []
            current = current.get(part)
        if not isinstance(current, list):
            return []
        return [item.get(parts[-1]) for item in current]

    def keys(self, path):
        value = self.get(path)
        if isinstance(value, dict):
            return list(value.keys())
        return []

    def __str__(self):
        if self.data is None:
            return f"ReadJson({self.filepath}, loaded=False)"
        products = self.get_all("catalog.product.sku")
        return f"ReadJson({self.filepath}, loaded=True, products={len(products)})"


# ─── Zadanie 2 ─ Klasa ReadXml: wczytywanie i nawigacja po XML ───────────────
class ReadXml:
    """Reads an XML file and provides path-based value access."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.root = None

    def load(self):
        try:
            self.root = ET.parse(self.filepath).getroot()
        except FileNotFoundError:
            print(f"ReadXml: file not found: {self.filepath}")
        except ET.ParseError as e:
            print(f"ReadXml: invalid XML in {self.filepath}: {e}")

    def get(self, path):
        parts = path.split(".")[1:]  # skip root tag
        current = self.root
        for part in parts:
            current = current.find(part)
            if current is None:
                return None
        return current.text

    def get_all(self, path):
        parts = path.split(".")[1:]  # skip root tag
        container = self.root
        for part in parts[:-2]:
            container = container.find(part)
            if container is None:
                return []
        return [item.find(parts[-1]).text for item in container.findall(parts[-2])]

    def __str__(self):
        if self.root is None:
            return f"ReadXml({self.filepath}, loaded=False)"
        products = len(self.root.findall("product"))
        return (
            f"ReadXml({self.filepath}, loaded=True, "
            f"root={self.root.tag}, products={products})"
        )


# ─── Zadanie 3 ─ Klasa CompareJsonVsXml: rejestracja mapowania pol ───────────
class CompareJsonVsXml:
    """Compares field values between an XML source and a JSON source."""

    def __init__(self, xml_reader, json_reader):
        self.xml_reader = xml_reader
        self.json_reader = json_reader
        self.mappings = []

    def add_mapping(self, xml_path, json_path, label):
        self.mappings.append({
            "xml_path": xml_path,
            "json_path": json_path,
            "label": label,
        })

    def compare_field(self, xml_path, json_path):
        xml_value = self.xml_reader.get(xml_path)
        json_value = self.json_reader.get(json_path)
        return {
            "xml_value": xml_value,
            "json_value": json_value,
            "match": xml_value == json_value,
        }

# ─── Zadanie 4 ─ Porownanie wszystkich mapowań i podsumowanie ────────────────
    def compare_all(self):
        results = []
        for mapping in self.mappings:
            xml_values = self.xml_reader.get_all(mapping["xml_path"])
            json_values = self.json_reader.get_all(mapping["json_path"])
            total = max(len(xml_values), len(json_values))
            mismatches = []
            for i in range(total):
                xv = xml_values[i] if i < len(xml_values) else None
                jv = json_values[i] if i < len(json_values) else None
                if xv != jv:
                    mismatches.append({"index": i + 1, "xml_value": xv, "json_value": jv})
            results.append({
                "label": mapping["label"],
                "total": total,
                "mismatches": mismatches,
            })
        return results

    def summary(self):
        results = self.compare_all()
        total = sum(r["total"] for r in results)
        mismatched = sum(len(r["mismatches"]) for r in results)
        return {
            "total_compared": total,
            "total_matched": total - mismatched,
            "total_mismatched": mismatched,
        }

# ─── Zadanie 5 ─ Raport weryfikacji ──────────────────────────────────────────
    def print_report(self):
        results = self.compare_all()
        stats = self.summary()
        status = "OK" if stats["total_mismatched"] == 0 else "FAILED"

        print("========== RAPORT WERYFIKACJI API ==========")
        print(f"XML : {self.xml_reader}")
        print(f"JSON: {self.json_reader}")
        print()

        for r in results:
            n_mis = len(r["mismatches"])
            print(f"  {r['label']:<20}: {r['total']} porownano, {n_mis:>2} niezgodne")

        print()
        print("Szczegoly niezgodnosci:")
        any_mismatch = False
        for r in results:
            for m in r["mismatches"]:
                any_mismatch = True
                label = f"[{r['label']:<16}]"
                print(
                    f"  {label} #{m['index']:<3} "
                    f"XML={str(m['xml_value'])!r:<30} "
                    f"JSON={str(m['json_value'])!r}"
                )
        if not any_mismatch:
            print("  Brak niezgodnosci.")

        print()
        print(
            f"Lacznie : {stats['total_compared']} porownano, "
            f"{stats['total_matched']} zgodnych, "
            f"{stats['total_mismatched']} niezgodnych"
        )
        print(f"Status  : {status}")
        print("============================================")


# ─── Uruchomienie ─────────────────────────────────────────────────────────────
json_reader = ReadJson(JSON_FILE)
xml_reader = ReadXml(XML_FILE)

json_reader.load()
xml_reader.load()

comparator = CompareJsonVsXml(xml_reader, json_reader)
comparator.add_mapping("catalog.product.name",     "catalog.product.name",     "Product names")
comparator.add_mapping("catalog.product.price",    "catalog.product.price",    "Product prices")
comparator.add_mapping("catalog.product.category", "catalog.product.category", "Categories")
comparator.add_mapping("catalog.product.stock",    "catalog.product.stock",    "Stock levels")

comparator.print_report()
