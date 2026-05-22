# orders_solution.py - Projekt 01: Przetwarzanie zamowien (rozwiazanie)


orders = [
    {"id": 1,  "client": "Anna Kowalska",    "product": "Laptop",     "amount": 3499.00, "status": "completed"},
    {"id": 2,  "client": "Piotr Nowak",      "product": "Mysz",       "amount":   89.99, "status": "pending"},
    {"id": 3,  "client": "Anna Kowalska",    "product": "Monitor",    "amount": 1299.00, "status": "completed"},
    {"id": 4,  "client": "Maria Wisniewska", "product": "Klawiatura", "amount":  229.00, "status": "completed"},
    {"id": 5,  "client": "Piotr Nowak",      "product": "Laptop",     "amount": 4199.00, "status": "cancelled"},
    {"id": 6,  "client": "Tomasz Wojcik",    "product": "Sluchawki",  "amount":  349.00, "status": "completed"},
    {"id": 7,  "client": "Maria Wisniewska", "product": "Webcam",     "amount":  199.00, "status": "pending"},
    {"id": 8,  "client": "Anna Kowalska",    "product": "Mysz",       "amount":   89.99, "status": "completed"},
    {"id": 9,  "client": "Tomasz Wojcik",    "product": "Monitor",    "amount": 1299.00, "status": "cancelled"},
    {"id": 10, "client": "Piotr Nowak",      "product": "Sluchawki",  "amount":  349.00, "status": "completed"},
    {"id": 11, "client": "Maria Wisniewska", "product": "Laptop",     "amount": 3499.00, "status": "completed"},
    {"id": 12, "client": "Tomasz Wojcik",    "product": "Klawiatura", "amount":  229.00, "status": "pending"},
]


def filter_by_status(orders, status):
    """Returns orders filtered by the given status."""
    result = []
    for order in orders:
        if order["status"] == status:
            result.append(order)
    return result


def calculate_revenue(orders):
    """Returns total amount of all completed orders, rounded to 2 decimal places."""
    total = 0
    for order in filter_by_status(orders, "completed"):
        total += order["amount"]
    return round(total, 2)


def client_totals(orders):
    """Returns a dict of {client_name: total_completed_amount}."""
    totals = {}
    for order in filter_by_status(orders, "completed"):
        client = order["client"]
        if client in totals:
            totals[client] += order["amount"]
        else:
            totals[client] = order["amount"]
    return totals


def get_amount(client_tuple):
    """Returns the amount from a (client, amount) tuple - used as sort key."""
    return client_tuple[1]


def top_clients(orders, n=3):
    """Returns a list of n (client, total_amount) tuples, sorted descending."""
    totals = client_totals(orders)
    pairs = []
    for client in totals:
        pairs.append((client, totals[client]))
    sorted_pairs = sorted(pairs, key=get_amount, reverse=True)
    return sorted_pairs[:n]


def print_report(orders):
    """Prints a formatted summary report for the given orders."""
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
