import random
import csv

random.seed(42)

COMPANIES = [
    "Kowalski i Wspolnicy Sp. z o.o.",
    "ABC Tech S.A.",
    "Nowak Consulting",
    "XYZ Solutions Sp. z o.o.",
    "Techpol S.A.",
    "DataCorp Sp. z o.o.",
    "Polsoft S.A.",
    "InnoTech Sp. z o.o.",
    "BiznesPlus S.A.",
    "MegaCorp Sp. z o.o.",
]

ACCOUNT_CODES = ["200-01", "200-02", "300-01", "300-02", "400-01", "400-02", "500-01", "500-02"]

DATES = (
    [f"2024-01-{d:02d}" for d in range(2, 32) if d not in (6, 7, 13, 14, 20, 21, 27, 28)]
    * 12
)[:200]


def make_amount():
    return round(random.uniform(300, 48000), 2)


def make_ref(n):
    return f"REF-2024-{n:04d}"


# --- Base 200 transactions (shared by both files) ---
base = []
for i in range(1, 201):
    base.append({
        "ref": make_ref(i),
        "date": DATES[i - 1],
        "amount": make_amount(),
        "company": COMPANIES[i % len(COMPANIES)],
        "account": ACCOUNT_CODES[i % len(ACCOUNT_CODES)],
    })

# Transactions with amount mismatches (refs 141-150): accounting has different amount
MISMATCH_REFS = {make_ref(i) for i in range(141, 151)}

# Bank-only transactions (not in accounting): refs 201-210
bank_only = []
for i in range(201, 211):
    bank_only.append({
        "ref": make_ref(i),
        "date": DATES[i % len(DATES)],
        "amount": make_amount(),
        "company": COMPANIES[i % len(COMPANIES)],
    })

# Bank duplicates: repeat refs 11, 22, 33, 44, 55
BANK_DUP_REFS = [make_ref(i) for i in (11, 22, 33, 44, 55)]
bank_dups = [t for t in base if t["ref"] in BANK_DUP_REFS]

# Accounting duplicates: repeat refs 66, 77, 88, 99, 110
ACC_DUP_REFS = [make_ref(i) for i in (66, 77, 88, 99, 110)]
acc_dups = [t for t in base if t["ref"] in ACC_DUP_REFS]

# Invalid amount positions in bank (within base rows): refs 31, 32, 33 get bad values
BANK_INVALID_REFS = {make_ref(i) for i in (61, 62, 63, 64, 65)}
BANK_INVALID_VALUES = ["n/a", "", "ERROR", "n/a", ""]

# Invalid amount positions in accounting: refs 171, 172, 173
ACC_INVALID_REFS = {make_ref(i) for i in (171, 172, 173, 174, 175)}
ACC_INVALID_VALUES = ["ERROR", "", "n/a", "ERROR", ""]


# --- Write bank.csv ---
bank_rows = []
bank_invalid_iter = iter(BANK_INVALID_VALUES)
for t in base:
    if t["ref"] in BANK_INVALID_REFS:
        amount_str = next(bank_invalid_iter)
    else:
        amount_str = str(t["amount"])
    bank_rows.append({
        "date": t["date"],
        "reference": t["ref"],
        "amount": amount_str,
        "description": f"Przelew za FV/2024/{t['ref'][-4:]} - {t['company']}",
    })

for t in bank_only:
    bank_rows.append({
        "date": t["date"],
        "reference": t["ref"],
        "amount": str(t["amount"]),
        "description": f"Przelew za FV/2024/{t['ref'][-4:]} - {t['company']}",
    })

for t in bank_dups:
    bank_rows.append({
        "date": t["date"],
        "reference": t["ref"],
        "amount": str(t["amount"]),
        "description": f"Duplikat - {t['company']}",
    })

random.shuffle(bank_rows)

with open("bank.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "reference", "amount", "description"])
    writer.writeheader()
    writer.writerows(bank_rows)


# --- Write accounting.csv ---
acc_rows = []
acc_invalid_iter = iter(ACC_INVALID_VALUES)
for t in base:
    if t["ref"] in ACC_INVALID_REFS:
        amount_str = next(acc_invalid_iter)
    elif t["ref"] in MISMATCH_REFS:
        amount_str = str(round(t["amount"] + random.choice([-100, -50, 50, 100, 200]), 2))
    else:
        amount_str = str(t["amount"])
    acc_rows.append({
        "date": t["date"],
        "reference": t["ref"],
        "amount": amount_str,
        "account_code": t["account"],
    })

for t in acc_dups:
    acc_rows.append({
        "date": t["date"],
        "reference": t["ref"],
        "amount": str(t["amount"]),
        "account_code": t["account"],
    })

random.shuffle(acc_rows)

with open("accounting.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "reference", "amount", "account_code"])
    writer.writeheader()
    writer.writerows(acc_rows)


print("Generated bank.csv and accounting.csv")
print(f"  bank.csv      : {len(bank_rows)} rows")
print(f"  accounting.csv: {len(acc_rows)} rows")
print(f"  Bank-only refs : {len(bank_only)}")
print(f"  Mismatches     : {len(MISMATCH_REFS)}")
print(f"  Bank duplicates: {len(bank_dups)}")
print(f"  Acc duplicates : {len(acc_dups)}")
print(f"  Bank invalid   : {len(BANK_INVALID_REFS)}")
print(f"  Acc invalid    : {len(ACC_INVALID_REFS)}")
