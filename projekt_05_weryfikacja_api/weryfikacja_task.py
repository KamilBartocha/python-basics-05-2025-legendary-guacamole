# weryfikacja_task.py - Projekt 05: Weryfikacja migracji API
#
# Firma migruje z legacy systemu (eksport XML) na nowe REST API (JSON).
# Weryfikacja, ze oba źródła zwracaja te same dane.
# Twoj skrypt porownuje oba formaty i generuje raport rozbieznosci.
#
# Uruchomienie: python3 weryfikacja_task.py

import json
import xml.etree.ElementTree as ET

JSON_FILE = "products.json"
XML_FILE = "products.xml"


# ─── ReadXml (gotowa klasa - wzorzec do nauki) ───────────────────────────────
class ReadXml:
    """Reads an XML file and provides path-based value access.

    Attributes:
        filepath: Path to the XML file.
        root:     Root Element after parsing. None until load() is called.
    """

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


# ─── Zadanie 1 ─ Klasa ReadJson: wczytywanie i nawigacja po JSON ──────────────
class ReadJson:
    """Reads a JSON file and provides path-based value access.

    Study ReadXml above as a reference — ReadJson mirrors the same interface:
    load(), get(path), get_all(path), __str__. The difference is navigating
    a Python dict/list instead of an XML element tree.

    Attributes:
        filepath: Path to the JSON file.
        data:     Parsed JSON content as a Python dict. None until load() is called.
    """

    def __init__(self, filepath):
        """Store filepath and initialise data to None."""
        pass

    def load(self):
        """Parse the JSON file and store the result in self.data.

        Raises no exceptions to the caller. Prints a message and leaves
        self.data as None on failure.

        Handled exceptions:
            FileNotFoundError: file does not exist at self.filepath.
            json.JSONDecodeError: file content is not valid JSON.
        """
        pass

    def get(self, path):
        """Return a single value by navigating a dot-path through dicts.

        Splits path on "." and calls .get() at each step. Returns None as
        soon as a key is missing or the current value is not a dict.

        Args:
            path: Dot-separated path string, e.g. "catalog.product".

        Returns:
            The value at the given path, or None if any segment is missing.

        Examples:
            get("catalog") -> {"product": [...]}
            get("catalog.missing") -> None
        """
        pass

    def get_all(self, path):
        """Return a list of field values from every item in an array.

        Navigates all but the last path segment to reach a list, then
        collects the last segment's value from each list element.

        Args:
            path: Dot-separated path whose second-to-last segment is a list,
                  e.g. "catalog.product.price".

        Returns:
            A list of values, one per list element. Returns an empty list
            if the path is invalid or the parent is not a list.

        Example:
            get_all("catalog.product.name")
            -> ["Laptop Dell XPS 15", "MacBook Air M2", ...]

        Hint: split path, navigate parts[:-1] with get(), then
        [item.get(parts[-1]) for item in current].
        """
        pass

    def keys(self, path):
        """Return the keys of the dict located at the given path.

        Args:
            path: Dot-separated path to a dict, e.g. "catalog.product[0]".

        Returns:
            A list of key strings, or an empty list if path is invalid or
            the value at path is not a dict.

        Example:
            keys("catalog.product[0]") -> ["sku", "name", "price", ...]
        """
        pass

    def __str__(self):
        """Return a one-line summary of this reader.

        Example:
            ReadJson(products.json, loaded=True, products=25)
        """
        pass


# ─── Zadanie 2 ─ Klasa CompareJsonVsXml: rejestracja mapowania pol ───────────
class CompareJsonVsXml:
    """Compares field values between an XML source and a JSON source.

    Attributes:
        xml_reader:  An instance of ReadXml (already loaded).
        json_reader: An instance of ReadJson (already loaded).
        mappings:    List of registered field mappings.
    """

    def __init__(self, xml_reader, json_reader):
        """Store both readers and initialise an empty mappings list."""
        pass

    def add_mapping(self, xml_path, json_path, label):
        """Register a field mapping to be compared.

        Args:
            xml_path:  Dot-path for ReadXml.get_all(), e.g. "catalog.product.price".
            json_path: Dot-path for ReadJson.get_all(), e.g. "catalog.product.price".
            label:     Human-readable name shown in the report, e.g. "Product prices".
        """
        pass

    def compare_field(self, xml_path, json_path):
        """Compare a single value from each source.

        Fetches one value from each reader using get() and returns a result dict.

        Args:
            xml_path:  Path passed to xml_reader.get().
            json_path: Path passed to json_reader.get().

        Returns:
            A dict with keys: "xml_value", "json_value", "match" (bool).

        Example:
            compare_field("catalog.product.sku", "catalog.product.sku")
            -> {"xml_value": "SKU-001", "json_value": "SKU-001", "match": True}
        """
        pass


# ─── Zadanie 3 ─ Porownanie wszystkich mapowań i podsumowanie ────────────────
    def compare_all(self):
        """Run all registered mappings and return a list of comparison results.

        For each mapping, fetches all values from both sources via get_all(),
        then compares them element by element. Pairs without a counterpart
        (different list lengths) are flagged as mismatches.

        Returns:
            A list of result dicts, one per mapping, each containing:
            "label", "total", "mismatches": list of
            {"index": N, "xml_value": ..., "json_value": ...}.

        Example:
            compare_all() -> [
                {"label": "Product prices", "total": 25,
                 "mismatches": [{"index": 3, "xml_value": "299.00",
                                 "json_value": "279.00"}, ...]},
                ...
            ]
        """
        pass

    def summary(self):
        """Return aggregate counts across all mappings.

        Calls compare_all() and totals the numbers.

        Returns:
            A dict with keys: "total_compared", "total_matched",
            "total_mismatched".

        Example:
            summary() -> {"total_compared": 100,
                          "total_matched": 94, "total_mismatched": 6}
        """
        pass


# ─── Zadanie 4 ─ Raport weryfikacji (gotowy - uruchom skrypt po implementacji) ─
    def print_report(self):
        """Print a formatted verification report to stdout."""
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
