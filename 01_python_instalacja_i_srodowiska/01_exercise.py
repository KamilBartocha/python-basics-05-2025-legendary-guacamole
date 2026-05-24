# 01_exercise.py — 01 Instalacja, IDE i środowiska

# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Algorytm: oblicz BMI.
# Dane: waga = 75 kg, wzrost = 1.80 m
# Wzór: BMI = waga / wzrost²
# Wypisz wynik z dokładnością do 2 miejsc po przecinku.

weight = 75
height = 1.80
bmi = weight * height ** 2
print(round(bmi, 2))


# ─── Ćwiczenie 2 ──────────────────────────────────────────────────────────────
# Algorytm: przelicz temperaturę z Celsjusza na Fahrenheita i Kelviny.
# Wzory:
#   F = C * 9/5 + 32
#   K = C + 273.15
# Wypisz wszystkie trzy wartości: "C=20  F=68.0  K=293.15"

temp_celsius = 20
F = temp_celsius * (9/5) + 32
K = temp_celsius + 273.15

print(f"C={temp_celsius}, F={F}, K={K}")

# ─── Ćwiczenie 3 ──────────────────────────────────────────────────────────────
# Algorytm: przelicz sekundy na format HH:MM:SS.
# Dane: total_seconds = 3661
# Oczekiwany wynik: "01:01:01"
# Wskazówka: użyj operatorów // i %

total_seconds = 3661
seconds = total_seconds % 60
minutes_tmp = total_seconds // 60

minutes = minutes_tmp % 60
hours = minutes_tmp // 60

seconds = "0" + str(seconds)
minutes = "0" + str(minutes)
hours = "0" + str(hours)

result = hours[-2:] + ":" + minutes[-2:] + ":" + seconds[-2:]

print(result)
