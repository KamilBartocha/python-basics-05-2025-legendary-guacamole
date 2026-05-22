# logs_solution.py - Projekt 03: Parser logow (rozwiazanie)

LOG_FILE = "projekt_03_logi/app.log"


# ─── Zadanie 1 ─ Wczytywanie pliku z logami ──────────────────────────────────
def read_logs(filepath):
    """Reads a log file and returns a list of non-empty lines."""
    lines = []
    with open(filepath) as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                lines.append(stripped)
    return lines


# ─── Zadanie 2 ─ Parsowanie pojedynczej linii logu do slownika ───────────────
def parse_line(line):
    """Parses a single log line into a dict with date, time, level, module, message."""
    parts = line.split()
    return {
        "date":    parts[0],
        "time":    parts[1],
        "level":   parts[2],
        "module":  parts[3],
        "message": " ".join(parts[4:]),
    }


# ─── Zadanie 3 ─ Zliczanie wpisow wedlug poziomu severity ───────────────────
def count_by_level(parsed_logs):
    """Returns a dict of {level: count} for all log entries."""
    counts = {}
    for log in parsed_logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts


# ─── Zadanie 4 ─ Liczba bledow per modul ─────────────────────────────────────
def errors_by_module(parsed_logs):
    """Returns a dict of {module: error_count} for ERROR-level entries only."""
    counts = {}
    for log in parsed_logs:
        if log["level"] == "ERROR":
            module = log["module"]
            if module in counts:
                counts[module] += 1
            else:
                counts[module] = 1
    return counts


def get_count(pair):
    """Returns the count from a (name, count) tuple - used as sort key."""
    return pair[1]


# ─── Zadanie 5 ─ Generowanie raportu tekstowego ──────────────────────────────
def print_report(filepath):
    """Reads the log file and prints a formatted analysis report."""
    lines = read_logs(filepath)
    parsed = []
    for line in lines:
        parsed.append(parse_line(line))

    levels  = count_by_level(parsed)
    errors  = errors_by_module(parsed)

    level_order = ["INFO", "WARNING", "ERROR"]
    error_pairs = sorted(errors.items(), key=get_count, reverse=True)

    last_errors = []
    for log in parsed:
        if log["level"] == "ERROR":
            last_errors.append(log)
    last_errors = last_errors[-3:]

    print(f"========== RAPORT LOGOW: {filepath} ==========")
    print(f"Wszystkich wpisow: {len(parsed)}")
    print()
    print("Poziomy:")
    for level in level_order:
        count = levels.get(level, 0)
        print(f"  {level:<10} {count}")
    print()
    print("Errors per module:")
    for module, count in error_pairs:
        print(f"  {module:<12} {count}")
    print()
    print("Ostatnie 3 ERROR:")
    for log in last_errors:
        print(f"  {log['date']} {log['time']}  {log['module']:<12} {log['message']}")
    print("===========================================")


# ─── Uruchomienie ─────────────────────────────────────────────────────────────
print_report(LOG_FILE)
