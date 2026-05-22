# orders_task.py - Projekt 01: Przetwarzanie zamówień
#
# Firma e-commerce. Dostajesz surowe dane zamówień
# i masz napisac skrypt, ktory przetworzy je i wygeneruje raport.
#
# Dane sa juz przygotowane ponizej jako lista słowników.
# Twoje zadanie: zaimplementowac 5 funkcji opisanych w komentarzach.


orders = [
    {"id": 1,  "client": "Anna Kowalska",    "product": "Laptop",     "amount": 3499.00, "status": "completed"},
    {"id": 2,  "client": "Piotr Nowak",      "product": "Mysz",       "amount":   89.99, "status": "pending"},
    {"id": 3,  "client": "Anna Kowalska",    "product": "Monitor",    "amount": 1299.00, "status": "completed"},
    {"id": 4,  "client": "Maria Wisniewska", "product": "Klawiatura", "amount":  229.00, "status": "completed"},
    {"id": 5,  "client": "Piotr Nowak",      "product": "Laptop",     "amount": 4199.00, "status": "cancelled"},
    {"id": 6,  "client": "Tomasz Wojcik",    "product": "Słuchawki",  "amount":  349.00, "status": "completed"},
    {"id": 7,  "client": "Maria Wisniewska", "product": "Webcam",     "amount":  199.00, "status": "pending"},
    {"id": 8,  "client": "Anna Kowalska",    "product": "Mysz",       "amount":   89.99, "status": "completed"},
    {"id": 9,  "client": "Tomasz Wojcik",    "product": "Monitor",    "amount": 1299.00, "status": "cancelled"},
    {"id": 10, "client": "Piotr Nowak",      "product": "Słuchawki",  "amount":  349.00, "status": "completed"},
    {"id": 11, "client": "Maria Wisniewska", "product": "Laptop",     "amount": 3499.00, "status": "completed"},
    {"id": 12, "client": "Tomasz Wojcik",    "product": "Klawiatura", "amount":  229.00, "status": "pending"},
]


# ─── Zadanie 1 ─ Filtrowanie zamowien po statusie ────────────────────────────
def filter_by_status(orders, status):
    """Return only the orders matching the given status.

    Iterates over the orders list and collects entries whose "status" value
    equals the status argument.

    Args:
        orders: A list of order dicts, each with keys: id, client, product,
                amount, status.
        status: The status string to filter by. Valid values: "completed",
                "pending", "cancelled".

    Returns:
        A list of order dicts whose status matches the given value.

    Example:
        filter_by_status(orders, "completed") -> [order1, order3, ...]
    """
    pass


# ─── Zadanie 2 ─ Obliczanie łacznego przychodu ze zrealizowanych zamowien ─────
def calculate_revenue(orders):
    """Return the total amount of all completed orders, rounded to 2 decimal places.

    Filters the orders list to completed entries only, then sums their
    "amount" values.

    Args:
        orders: A list of order dicts.

    Returns:
        A float representing the total revenue from completed orders,
        rounded to 2 decimal places.

    Example:
        calculate_revenue(orders) -> 9313.99
    """
    pass


# ─── Zadanie 3 ─ Suma wydatkow per klient (tylko completed) ──────────────────
def client_totals(orders):
    """Return total completed spending per client as a dictionary.

    Filters to completed orders only, then for each order accumulates the
    "amount" under the client's name key.

    Args:
        orders: A list of order dicts.

    Returns:
        A dict mapping each client name to the sum of their completed order
        amounts.

    Example:
        client_totals(orders)
        -> {"Anna Kowalska": 4887.99, "Maria Wisniewska": 3728.00, ...}
    """
    pass


# ─── Zadanie 4 ─ Ranking klientow z najwyzszymi wydatkami ────────────────────
def top_clients(orders, n=3):
    """Return the n clients with the highest total completed spending.

    Builds a list of (client_name, total_amount) tuples from client_totals,
    sorts it by amount descending, and returns the first n entries.

    Args:
        orders: A list of order dicts.
        n:      Number of top clients to return (default 3).

    Returns:
        A list of (client_name, total_amount) tuples, sorted by amount
        descending, limited to n entries.

    Example:
        top_clients(orders, n=3)
        -> [("Anna Kowalska", 4887.99), ("Maria Wisniewska", 3728.00), ...]

    Hint: write a helper function that extracts the amount from a tuple and
    pass it as the key argument to sorted().
    """
    pass


# ─── Zadanie 5 ─ Generowanie raportu (gotowy - uruchom skrypt po implementacji)
def print_report(orders):
    """Print a formatted summary report for the given orders list."""
    completed = filter_by_status(orders, "completed")
    pending   = filter_by_status(orders, "pending")
    cancelled = filter_by_status(orders, "cancelled")
    revenue   = calculate_revenue(orders)
    top       = top_clients(orders)

    print("========== RAPORT ZAMOWIEN ==========")
    print(f"Wszystkich zamowien : {len(orders)}")
    print(f"Zrealizowanych      : {len(completed)}")
    print(f"Oczekujacych        : {len(pending)}")
    print(f"Anulowanych         : {len(cancelled)}")
    print()
    print(f"Przychod (completed): {revenue:.2f} PLN")
    print()
    print(f"Top {len(top)} klientow:")
    for i, (client, amount) in enumerate(top):
        print(f"  {i + 1}. {client:<20} {amount:>8.2f} PLN")
    print("=====================================")


# Uruchomienie
print_report(orders)
