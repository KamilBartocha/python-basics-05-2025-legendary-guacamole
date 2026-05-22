# reconciliation_solution.py - Projekt 04: Reconciliacja płatnosci
#
# Dział finansowy eksportuje co miesiac dwa pliki:
# wyciag bankowy i rejestr ksiegowy.
# Twoim zadaniem jest porownac oba pliki i wykryc rozbieżności.
# Twoj skrypt zastapi manualny proces.
#
# Uruchomienie: python3 reconciliation_solution.py

BANK_FILE = "bank.csv"
ACCOUNTING_FILE = "accounting.csv"


# ─── Zadanie 1 ─ Wczytanie pliku CSV do listy slownikow ──────────────────────
def load_csv(filepath):
    """Read a CSV file and return its rows as a list of dictionaries.

    Opens the file, reads the header row, then parses each subsequent line
    into a dict using the header fields as keys. Skips completely empty lines.

    Args:
        filepath: Path to the CSV file to read.

    Returns:
        A list of dicts, one per data row, with keys taken from the header.

    Example:
        load_csv("bank.csv")
        -> [{"date": "2024-01-02", "reference": "REF-2024-0042",
             "amount": "1250.00", "description": "Przelew za..."}, ...]

    Hint: open the file with encoding="utf-8", use .split(",") on each line,
    and zip() to pair header fields with row values.
    """
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    header = lines[0].strip().split(",")
    rows = []
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        values = line.split(",")
        rows.append(dict(zip(header, values)))
    return rows


# ─── Zadanie 2 ─ Transakcje obecne w banku, ale brakujace w ksiegowosci ──────
def find_missing_in_accounting(bank_rows, accounting_rows):
    """Return bank transactions whose reference does not appear in accounting.

    Builds a set of all reference values from accounting_rows, then filters
    bank_rows to entries whose "reference" key is not in that set.

    Args:
        bank_rows:       List of dicts loaded from bank.csv.
        accounting_rows: List of dicts loaded from accounting.csv.

    Returns:
        A list of bank row dicts with no matching reference in accounting.

    Example:
        find_missing_in_accounting(bank, acc)
        -> [{"reference": "REF-2024-0201", ...}, ...]
    """
    acc_refs = {row["reference"] for row in accounting_rows}
    return [row for row in bank_rows if row["reference"] not in acc_refs]


# ─── Zadanie 3 ─ Transakcje z niezgodna kwota ────────────────────────────────
def find_amount_mismatches(bank_rows, accounting_rows):
    """Return transactions present in both files but with differing amounts.

    Builds a lookup dict from accounting_rows keyed by reference. For each
    bank row whose reference exists in accounting, compares the float values
    of their "amount" fields. Collects mismatches as dicts with keys:
    "reference", "bank_amount", "accounting_amount".

    Rows where either amount is None (failed parsing) are skipped silently.

    Args:
        bank_rows:       List of dicts loaded from bank.csv.
        accounting_rows: List of dicts loaded from accounting.csv.

    Returns:
        A list of mismatch dicts, each with keys "reference",
        "bank_amount", "accounting_amount".

    Example:
        find_amount_mismatches(bank, acc)
        -> [{"reference": "REF-2024-0141",
             "bank_amount": 12345.67, "accounting_amount": 12245.67}, ...]

    Hint: use parse_amount() from Zadanie 5 to safely convert amount strings.
    """
    acc_lookup = {row["reference"]: row for row in accounting_rows}
    mismatches = []
    for row in bank_rows:
        ref = row["reference"]
        if ref not in acc_lookup:
            continue
        bank_amount = parse_amount(row.get("amount", ""))
        acc_amount = parse_amount(acc_lookup[ref].get("amount", ""))
        if bank_amount is None or acc_amount is None:
            continue
        if bank_amount != acc_amount:
            mismatches.append({
                "reference": ref,
                "bank_amount": bank_amount,
                "accounting_amount": acc_amount,
            })
    return mismatches


# ─── Zadanie 4 ─ Wykrywanie duplikatow ───────────────────────────────────────
def find_duplicates(rows):
    """Return references that appear more than once in the given row list.

    Iterates over rows, counting occurrences of each "reference" value.
    Collects references whose count exceeds 1.

    Args:
        rows: A list of row dicts, each containing a "reference" key.

    Returns:
        A list of reference strings that appear more than once.

    Example:
        find_duplicates(bank_rows)
        -> ["REF-2024-0011", "REF-2024-0022", ...]
    """
    counts = {}
    for row in rows:
        ref = row["reference"]
        counts[ref] = counts.get(ref, 0) + 1
    return [ref for ref, count in counts.items() if count > 1]


# ─── Zadanie 5 ─ Walidacja kwot i obsluga wyjatkow ───────────────────────────
def parse_amount(value):
    """Parse an amount string to float, returning None for invalid values.

    Attempts to convert value to float. Returns None instead of raising
    an exception for the following error cases:
    - Empty string or whitespace-only string (ValueError)
    - Non-numeric string such as "n/a" or "ERROR" (ValueError)
    - Missing key in a dict (KeyError) - handle at the call site using
      this function's None return to skip the row

    Args:
        value: A string representing a numeric amount.

    Returns:
        A float if conversion succeeds, or None if the value is invalid.

    Examples:
        parse_amount("1250.00") -> 1250.0
        parse_amount("n/a")     -> None
        parse_amount("")        -> None
        parse_amount("ERROR")   -> None

    Hint: use try/except ValueError and strip() to catch blank strings.
    """
    try:
        return float(value.strip())
    except ValueError:
        return None


def _count_invalid(rows):
    return sum(1 for row in rows if parse_amount(row.get("amount", "")) is None)


# ─── Zadanie 6 ─ Raport koncowy ──────────────────────────────────────────────
def print_report(bank_file, accounting_file):
    """Load both CSV files and print a formatted reconciliation report.

    Orchestrates the full pipeline: loads files, runs all checks, then
    prints a structured summary. Marks the reconciliation as OK only when
    there are zero missing entries, zero mismatches, and zero duplicates.

    Args:
        bank_file:       Path to the bank CSV file.
        accounting_file: Path to the accounting CSV file.

    Expected output format:
        ========== RAPORT RECONCILIACJI ==========
        Wiersze bankowe    : 215
        Wiersze ksiegowe   : 205
        Wiersze odrzucone  : 10  (niepoprawna kwota)

        Brakujace w ksiegowosci : 10
          REF-2024-0201
          REF-2024-0202
          ...

        Niezgodne kwoty : 10
          REF-2024-0141  bank: 12345.67  ksiegowosc: 12245.67
          ...

        Duplikaty w banku : 5
          REF-2024-0011, REF-2024-0022, ...

        Duplikaty w ksiegowosci : 5
          REF-2024-0066, REF-2024-0077, ...

        Status: FAILED
        ==========================================
    """
    bank = load_csv(bank_file)
    acc = load_csv(accounting_file)

    missing = find_missing_in_accounting(bank, acc)
    mismatches = find_amount_mismatches(bank, acc)
    bank_dups = find_duplicates(bank)
    acc_dups = find_duplicates(acc)
    invalid_count = _count_invalid(bank) + _count_invalid(acc)

    status = "OK" if not missing and not mismatches and not bank_dups and not acc_dups else "FAILED"

    print("========== RAPORT RECONCILIACJI ==========")
    print(f"Wiersze bankowe    : {len(bank)}")
    print(f"Wiersze ksiegowe   : {len(acc)}")
    print(f"Wiersze odrzucone  : {invalid_count}  (niepoprawna kwota)")

    print(f"\nBrakujace w ksiegowosci : {len(missing)}")
    for row in missing:
        print(f"  {row['reference']}")

    print(f"\nNiezgodne kwoty : {len(mismatches)}")
    for m in mismatches:
        print(f"  {m['reference']}  bank: {m['bank_amount']}  ksiegowosc: {m['accounting_amount']}")

    print(f"\nDuplikaty w banku : {len(bank_dups)}")
    if bank_dups:
        print(f"  {', '.join(bank_dups)}")

    print(f"\nDuplikaty w ksiegowosci : {len(acc_dups)}")
    if acc_dups:
        print(f"  {', '.join(acc_dups)}")

    print(f"\nStatus: {status}")
    print("==========================================")


# ─── Uruchomienie ─────────────────────────────────────────────────────────────
print_report(BANK_FILE, ACCOUNTING_FILE)
