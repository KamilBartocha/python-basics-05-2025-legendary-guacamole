# logs_task.py - Projekt 03: Parser logow
#
# Dostajesz plik app.log z logami aplikacji
# i masz napisac skrypt, ktory przeanalizuje co sie działo i wygeneruje raport.
#
# Format kazdej linii w pliku:
#   2024-01-15 08:09:02 ERROR   database    Connection timeout after 30s
#   [data]     [czas]   [poziom] [modul]    [wiadomosc...]
#
# Uruchomienie: python3 logs_task.py

LOG_FILE = "app.log"


# ─── Zadanie 1 ─ Wczytywanie pliku z logami ──────────────────────────────────
def read_logs(filepath):
    """Read a log file and return a list of non-empty lines.

    Opens the file at filepath, iterates line by line, strips leading and
    trailing whitespace (including the newline character), and collects only
    lines that are non-empty after stripping.

    Args:
        filepath: Path to the log file to read.

    Returns:
        A list of stripped, non-empty strings, one per log entry.

    Hint: use open() with a with block and call .strip() on each line.
    """
    pass


# ─── Zadanie 2 ─ Parsowanie pojedynczej linii logu do slownika ───────────────
def parse_line(line):
    """Parse a single log line into a structured dictionary.

    Splits the line on whitespace and maps the tokens to their respective
    fields. The message field contains all remaining tokens joined by spaces.

    Args:
        line: A single log line string in the format:
              "YYYY-MM-DD HH:MM:SS LEVEL   module   message text..."

    Returns:
        A dict with keys: "date", "time", "level", "module", "message".

    Example:
        parse_line("2024-01-15 08:09:02 ERROR   database    Connection timeout")
        -> {"date": "2024-01-15", "time": "08:09:02", "level": "ERROR",
            "module": "database", "message": "Connection timeout"}

    Hint: line.split() handles multiple consecutive spaces automatically.
    """
    pass


# ─── Zadanie 3 ─ Zliczanie wpisow wedlug poziomu severity ───────────────────
def count_by_level(parsed_logs):
    """Count log entries grouped by severity level.

    Iterates over a list of parsed log dicts and tallies how many entries
    exist for each distinct value of the "level" key.

    Args:
        parsed_logs: A list of dicts as returned by parse_line.

    Returns:
        A dict mapping each level name to its entry count.

    Example:
        count_by_level([...]) -> {"INFO": 9721, "WARNING": 250, "ERROR": 129}
    """
    pass


# ─── Zadanie 4 ─ Liczba bledow per modul ─────────────────────────────────────
def errors_by_module(parsed_logs):
    """Count ERROR-level entries grouped by module name.

    Filters the parsed log list to entries where level == "ERROR", then
    tallies how many errors originated from each distinct module.

    Args:
        parsed_logs: A list of dicts as returned by parse_line.

    Returns:
        A dict mapping each module name to its error count.

    Example:
        errors_by_module([...]) -> {"database": 50, "cache": 24, "auth": 21}
    """
    pass


# ─── Zadanie 5 ─ Generowanie raportu (gotowy - uruchom skrypt po implementacji)
def _get_count(pair):
    return pair[1]


def print_report(filepath):
    """Read a log file and print a formatted analysis report to stdout."""
    lines  = read_logs(filepath)
    parsed = [parse_line(line) for line in lines]
    levels = count_by_level(parsed)
    errors = errors_by_module(parsed)

    level_order  = ["INFO", "WARNING", "ERROR"]
    error_pairs  = sorted(errors.items(), key=_get_count, reverse=True)
    last_errors  = [log for log in parsed if log["level"] == "ERROR"][-3:]

    print(f"========== RAPORT LOGOW: {filepath} ==========")
    print(f"Wszystkich wpisow: {len(parsed)}")
    print()
    print("Poziomy:")
    for level in level_order:
        print(f"  {level:<10} {levels.get(level, 0)}")
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
