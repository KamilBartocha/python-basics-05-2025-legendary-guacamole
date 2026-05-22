# copybook_task.py - Projekt 02: Enkoder wiadomosci płatniczej ISO 20022
#
# System core-banking działa
# na COBOLu i oczekuje wiadomosci w formacie fixed-width: kazde pole ma
# scisle okreslona długosc w bajtach zgodna z definicja copybook'a.
#
# Twoje zadanie: na podstawie słownika z danymi przelewu (transaction)
# i listy definicji pol (fields) zbudowac jeden string o stałej długości,
# gdzie kazde pole jest dopełnione spacjami (X) lub zerami (9).
#
# Przykład (pole DBTR-NM, typ X, długosc 35, wartosc "Jan Kowalski"):
#   "Jan Kowalski                          "   <- 35 znakow, uzupełnionych spacjami
#
# Przykład (pole INSTR-AMT, typ 9, długość 18, decimals 2, wartosc 1234.56):
#   "000000000000123456"   <- 18 cyfr, kwota * 100, dopełniona zerami z lewej
#
# Uruchomienie: python3 copybook_task.py

fields = [
    # --- Message Header ---
    {"name": "MSG-ID",          "type": "X", "length": 35,                  "desc": "Message Identification"},
    {"name": "CREATION-DATE",   "type": "X", "length": 10,                  "desc": "Creation Date YYYY-MM-DD"},
    {"name": "CREATION-TIME",   "type": "X", "length": 8,                   "desc": "Creation Time HH-MM-SS"},
    {"name": "NB-OF-TXS",       "type": "9", "length": 15,                  "desc": "Number of Transactions"},
    {"name": "CTRL-SUM",        "type": "9", "length": 18, "decimals": 2,   "desc": "Control Sum"},
    # --- Payment Type Information ---
    {"name": "PMT-MTD",         "type": "X", "length": 3,                   "desc": "Payment Method TRF/CHK"},
    {"name": "INSTR-PRTY",      "type": "X", "length": 4,                   "desc": "Instruction Priority NORM/HIGH"},
    {"name": "SVC-LVL-CD",      "type": "X", "length": 4,                   "desc": "Service Level Code SEPA/SDVA"},
    {"name": "LCL-INSTRM-CD",   "type": "X", "length": 35,                  "desc": "Local Instrument Code"},
    {"name": "CTGY-PURP-CD",    "type": "X", "length": 4,                   "desc": "Category Purpose Code"},
    # --- Debtor ---
    {"name": "DBTR-NM",         "type": "X", "length": 140,                 "desc": "Debtor Name"},
    {"name": "DBTR-STREET",     "type": "X", "length": 70,                  "desc": "Debtor Street Name"},
    {"name": "DBTR-BLDG-NB",    "type": "X", "length": 16,                  "desc": "Debtor Building Number"},
    {"name": "DBTR-POST-CD",    "type": "X", "length": 16,                  "desc": "Debtor Postal Code"},
    {"name": "DBTR-TOWN",       "type": "X", "length": 35,                  "desc": "Debtor Town Name"},
    {"name": "DBTR-CTRY",       "type": "X", "length": 2,                   "desc": "Debtor Country ISO 3166"},
    {"name": "DBTR-IBAN",       "type": "X", "length": 34,                  "desc": "Debtor IBAN"},
    {"name": "DBTR-BIC",        "type": "X", "length": 11,                  "desc": "Debtor BIC/SWIFT"},
    {"name": "DBTR-ACCT-TP",    "type": "X", "length": 4,                   "desc": "Debtor Account Type IBAN/BBAN"},
    {"name": "DBTR-LEI",        "type": "X", "length": 20,                  "desc": "Debtor Legal Entity Identifier"},
    # --- Creditor ---
    {"name": "CDTR-NM",         "type": "X", "length": 140,                 "desc": "Creditor Name"},
    {"name": "CDTR-STREET",     "type": "X", "length": 70,                  "desc": "Creditor Street Name"},
    {"name": "CDTR-BLDG-NB",    "type": "X", "length": 16,                  "desc": "Creditor Building Number"},
    {"name": "CDTR-POST-CD",    "type": "X", "length": 16,                  "desc": "Creditor Postal Code"},
    {"name": "CDTR-TOWN",       "type": "X", "length": 35,                  "desc": "Creditor Town Name"},
    {"name": "CDTR-CTRY",       "type": "X", "length": 2,                   "desc": "Creditor Country ISO 3166"},
    {"name": "CDTR-IBAN",       "type": "X", "length": 34,                  "desc": "Creditor IBAN"},
    {"name": "CDTR-BIC",        "type": "X", "length": 11,                  "desc": "Creditor BIC/SWIFT"},
    {"name": "CDTR-ACCT-TP",    "type": "X", "length": 4,                   "desc": "Creditor Account Type IBAN/BBAN"},
    {"name": "CDTR-LEI",        "type": "X", "length": 20,                  "desc": "Creditor Legal Entity Identifier"},
    # --- Transaction ---
    {"name": "END-TO-END-ID",   "type": "X", "length": 35,                  "desc": "End-to-End Identification"},
    {"name": "TX-ID",           "type": "X", "length": 35,                  "desc": "Transaction Identification"},
    {"name": "INSTR-ID",        "type": "X", "length": 35,                  "desc": "Instruction Identification"},
    {"name": "CLR-SYS-REF",     "type": "X", "length": 35,                  "desc": "Clearing System Reference"},
    {"name": "STTLM-DT",        "type": "X", "length": 10,                  "desc": "Settlement Date YYYY-MM-DD"},
    {"name": "INSTR-AMT",       "type": "9", "length": 18, "decimals": 2,   "desc": "Instructed Amount"},
    {"name": "INSTR-CCY",       "type": "X", "length": 3,                   "desc": "Instructed Currency ISO 4217"},
    {"name": "INTR-BK-AMT",     "type": "9", "length": 18, "decimals": 2,   "desc": "Interbank Settlement Amount"},
    {"name": "INTR-BK-CCY",     "type": "X", "length": 3,                   "desc": "Interbank Settlement Currency"},
    {"name": "EXCH-RATE",       "type": "9", "length": 11, "decimals": 10,  "desc": "Exchange Rate"},
    # --- Charges ---
    {"name": "CHRG-BR",         "type": "X", "length": 4,                   "desc": "Charge Bearer DEBT/CRED/SHAR/SLEV"},
    {"name": "CHRG-AMT",        "type": "9", "length": 18, "decimals": 2,   "desc": "Charges Amount"},
    {"name": "CHRG-CCY",        "type": "X", "length": 3,                   "desc": "Charges Currency"},
    {"name": "CHRG-AGT-BIC",    "type": "X", "length": 11,                  "desc": "Charges Agent BIC"},
    {"name": "CHRG-TP",         "type": "X", "length": 35,                  "desc": "Charges Type"},
    # --- Remittance Information ---
    {"name": "RMT-INF-TP",      "type": "X", "length": 4,                   "desc": "Remittance Info Type STRD/USTRD"},
    {"name": "RMT-INF-REF",     "type": "X", "length": 35,                  "desc": "Remittance Reference"},
    {"name": "RMT-INF-INV-NB",  "type": "X", "length": 35,                  "desc": "Invoice Number"},
    {"name": "RMT-INF-DT",      "type": "X", "length": 10,                  "desc": "Remittance Date YYYY-MM-DD"},
    {"name": "RMT-USTRD",       "type": "X", "length": 140,                 "desc": "Unstructured Remittance Info"},
]

transaction = {
    "MSG-ID":         "MSGPL20240115000001",
    "CREATION-DATE":  "2024-01-15",
    "CREATION-TIME":  "09-30-00",
    "NB-OF-TXS":      1,
    "CTRL-SUM":       1234.56,
    "PMT-MTD":        "TRF",
    "INSTR-PRTY":     "NORM",
    "SVC-LVL-CD":     "SEPA",
    "LCL-INSTRM-CD":  "SCT",
    "CTGY-PURP-CD":   "SUPP",
    "DBTR-NM":        "Jan Kowalski",
    "DBTR-STREET":    "ul. Marszalkowska",
    "DBTR-BLDG-NB":   "15A",
    "DBTR-POST-CD":   "00-001",
    "DBTR-TOWN":      "Warszawa",
    "DBTR-CTRY":      "PL",
    "DBTR-IBAN":      "PL61109010140000071219812874",
    "DBTR-BIC":       "WBKPPLPP",
    "DBTR-ACCT-TP":   "IBAN",
    "DBTR-LEI":       "",
    "CDTR-NM":        "Acme Sp. z o.o.",
    "CDTR-STREET":    "ul. Dluga",
    "CDTR-BLDG-NB":   "3",
    "CDTR-POST-CD":   "31-147",
    "CDTR-TOWN":      "Krakow",
    "CDTR-CTRY":      "PL",
    "CDTR-IBAN":      "PL27114020040000300201355387",
    "CDTR-BIC":       "INGBPLPW",
    "CDTR-ACCT-TP":   "IBAN",
    "CDTR-LEI":       "",
    "END-TO-END-ID":  "E2E-INV-2024-00042",
    "TX-ID":          "TX-20240115-001",
    "INSTR-ID":       "INSTR-20240115-001",
    "CLR-SYS-REF":    "",
    "STTLM-DT":       "2024-01-16",
    "INSTR-AMT":      1234.56,
    "INSTR-CCY":      "PLN",
    "INTR-BK-AMT":    1234.56,
    "INTR-BK-CCY":    "PLN",
    "EXCH-RATE":      1.0,
    "CHRG-BR":        "SLEV",
    "CHRG-AMT":       0.0,
    "CHRG-CCY":       "PLN",
    "CHRG-AGT-BIC":   "",
    "CHRG-TP":        "",
    "RMT-INF-TP":     "STRD",
    "RMT-INF-REF":    "INV-2024-00042",
    "RMT-INF-INV-NB": "INV-2024-00042",
    "RMT-INF-DT":     "2024-01-10",
    "RMT-USTRD":      "Faktura INV-2024-00042 za uslugi IT",
}


# ─── Zadanie 1 ────────────────────────────────────────────────────────────────
def encode_alpha(value, length):
    """Encode a text value into a fixed-width, left-justified, space-padded string.

    Converts value to str, then truncates to length characters if too long,
    or pads with spaces on the right if too short.

    Args:
        value:  The value to encode. Will be cast to str.
        length: The exact number of characters the result must contain.

    Returns:
        A string of exactly length characters.

    Examples:
        encode_alpha("Jan Kowalski", 35)
            -> "Jan Kowalski                       "
        encode_alpha("TOOLONGVALUE", 4)
            -> "TOOL"

    Hint: use str.ljust(length) for padding.
    """
    pass


# ─── Zadanie 2 ────────────────────────────────────────────────────────────────
def encode_numeric(value, length, decimals=0):
    """Encode a numeric value into a fixed-width, zero-padded integer string.

    Multiplies value by 10**decimals to remove the decimal point, converts to
    int, then zero-pads on the left to exactly length digits. If the result
    exceeds length digits, keeps only the rightmost length digits.

    Args:
        value:    The numeric value to encode (int or float).
        length:   The exact number of digit characters the result must contain.
        decimals: Number of implied decimal places (default 0). The value is
                  scaled by 10**decimals before encoding.

    Returns:
        A string of exactly length digit characters.

    Examples:
        encode_numeric(1234.56, 18, decimals=2) -> "000000000000123456"
        encode_numeric(7, 15)                   -> "000000000000007"

    Hint: use str(int_value).zfill(length) for zero-padding.
    """
    pass


# ─── Zadanie 3 ────────────────────────────────────────────────────────────────
def encode_field(field, value):
    """Dispatch encoding to the correct function based on the field type.

    Reads field["type"] and calls either encode_alpha or encode_numeric
    with the appropriate parameters extracted from the field definition.

    Args:
        field: A dict with keys "type", "length", and optionally "decimals".
        value: The raw value to encode.

    Returns:
        A fixed-width encoded string matching field["length"] characters.

    Hint: use field.get("decimals", 0) to safely read the optional key.
    """
    pass


# ─── Zadanie 4 gotowy - buduje wiadomość ──────────────────────────────────────
def build_message(fields, transaction):
    """Build a single fixed-width message string from all field definitions.

    Iterates over fields in order. For each field, reads the corresponding
    value from transaction using field["name"] as the key, encodes it via
    encode_field, and concatenates the results into one string.

    Args:
        fields:      List of field definition dicts (name, type, length, ...).
        transaction: Dict mapping field names to their raw values.

    Returns:
        A single string whose total length equals the sum of all field lengths.
    """
    message = ""
    for field in fields:
        value = transaction[field["name"]]
        message += encode_field(field, value)
    return message


# ─── Zadanie 5 ─ Podsumowanie ─────────────────────────────────────────────────
def print_summary(message):
    """Print a summary of the encoded message."""
    pass


# ─── Uruchomienie ─────────────────────────────────────────────────────────────
message = build_message(fields, transaction)
print_summary(message)


# ─── Rozwiązanie dla danych z tego pliku: ─────────────────────────────────────
"""
Length: 1330 chars.

Message >MSGPL20240115000001                2024-01-1509-30-00000000000000001000000000000123456TRFNORMSEPASCT                                SUPPJan Kowalski                                                                                                                                ul. Marszalkowska                                                     15A             00-001          Warszawa                           PLPL61109010140000071219812874      WBKPPLPP   IBAN                    Acme Sp. z o.o.                                                                                                                             ul. Dluga                                                             3               31-147          Krakow                             PLPL27114020040000300201355387      INGBPLPW   IBAN                    E2E-INV-2024-00042                 TX-20240115-001                    INSTR-20240115-001                                                    2024-01-16000000000000123456PLN000000000000123456PLN10000000000SLEV000000000000000000PLN                                              STRDINV-2024-00042                     INV-2024-00042                     2024-01-10Faktura INV-2024-00042 za uslugi IT                                                                                                         <
"""
