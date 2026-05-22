# copybook_solution.py - Projekt 02: Enkoder wiadomosci platniczej ISO 20022 (rozwiazanie)

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


def encode_alpha(value, length):
    """Encodes a text value to a fixed-width left-justified, space-padded string."""
    text = str(value)
    if len(text) > length:
        return text[:length]
    return text.ljust(length)


def encode_numeric(value, length, decimals=0):
    """Encodes a numeric value to a fixed-width zero-padded integer string."""
    int_value = int(round(float(value) * (10 ** decimals)))
    digits = str(int_value).zfill(length)
    if len(digits) > length:
        return digits[-length:]
    return digits


def encode_field(field, value):
    """Dispatches encoding to encode_alpha or encode_numeric based on field type."""
    if field["type"] == "X":
        return encode_alpha(value, field["length"])
    return encode_numeric(value, field["length"], field.get("decimals", 0))


def build_message(fields, transaction):
    """Builds a single fixed-width string from all encoded field values."""
    message = ""
    for field in fields:
        value = transaction[field["name"]]
        message += encode_field(field, value)
    return message


def print_summary(message):
    """Prints total message length and the first 5 fields with their positions and values."""
    print(f"Length: {len(message)} chars.")
    print()
    print(f"Message >{message}<")


# ─── Uruchomienie ─────────────────────────────────────────────────────────────
message = build_message(fields, transaction)
print_summary(message)
