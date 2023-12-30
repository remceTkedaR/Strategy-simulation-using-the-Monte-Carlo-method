# //=============================================================================
# //Radosław Tecmer)
# //(c)Copyright (2023) free of copyright
# //-----------------------------------------------------------------------------
# //Program Symulator Monte Carlo.
# //Analiza Strategii dla handlu na Forex
# //1. Stały procent ryzykowanego kapitału
# //2. Stała kwota ryzykowana na transakcję
# //3. Maksymalne obsunięcie kapitału
# //4. Stała ryzyka Williamsa
# // --Może będę go rozwijał. To są małe próba --
# //-----------------------------------------------------------------------------
# //contact:
# //https://github.com/remceTkedaR
# //radek69tecmer@gmail.com
# //-------------------------------------------------------------------------------


import random
import matplotlib.pyplot as plt


def symulacja_monte_carlo(poczatkowy_kapital, liczba_transakcji, prawdopodobienstwo_wygranej, ryzyko_procent=None, ryzyko_kwota=None, maksymalna_strata=None, stala_ryzyka_williamsa=None):
    historia_kapitalu = [poczatkowy_kapital]

    for _ in range(liczba_transakcji):
        if stala_ryzyka_williamsa is not None:
            # Używamy stałej ryzyka Williamsa
            ryzyko_procent = stala_ryzyka_williamsa
            ryzyko_kwota = None

        if ryzyko_procent is not None:
            ryzykowana_kwota = poczatkowy_kapital * ryzyko_procent / 100
        elif ryzyko_kwota is not None:
            ryzykowana_kwota = ryzyko_kwota
        else:
            raise ValueError("Musisz wybrać jedną z opcji: ryzyko_procent lub ryzyko_kwota")

        if random.uniform(0, 1) < prawdopodobienstwo_wygranej:
            # Wygrana transakcja
            zysk = random.uniform(0, 2) * ryzykowana_kwota
            poczatkowy_kapital += zysk
        else:
            # Przegrana transakcja
            strata = random.uniform(0, 2) * ryzykowana_kwota
            poczatkowy_kapital -= strata

        if maksymalna_strata is not None and (maksymalna_strata > 0) and (poczatkowy_kapital - min(historia_kapitalu)) / poczatkowy_kapital > maksymalna_strata:
            break

        historia_kapitalu.append(poczatkowy_kapital)

    return historia_kapitalu


def rysuj_wykres(historia_kapitalu, nazwa_strategii):
    plt.plot(historia_kapitalu, label=nazwa_strategii)

# Wprowadzanie danych ręcznie przez użytkownika
poczatkowy_kapital = float(input("Podaj początkowy kapitał (USD): "))
liczba_transakcji = int(input("Podaj liczbę transakcji: "))
prawdopodobienstwo_wygranej = 0.5  # Prawdopodobieństwo wygranej transakcji

# Dodatkowe opcje
print("Wybierz wersję symulacji:")
print("1. Stały procent ryzykowanego kapitału")
print("2. Stała kwota ryzykowana na transakcję")
print("3. Maksymalne obsunięcie kapitału")
print("4. Stała ryzyka Williamsa")

wybor = int(input("Podaj numer wybranej wersji symulacji: "))

if wybor == 1:
    ryzyko_procent = float(input("Podaj dopuszczalne ryzyko procentowe (% kapitału): "))
    maksymalna_strata = None
    ryzyko_kwota = None
    stala_ryzyka_williamsa = None
elif wybor == 2:
    ryzyko_kwota = float(input("Podaj dopuszczalną ryzykowaną kwotę (USD): "))
    maksymalna_strata = None
    ryzyko_procent = None
    stala_ryzyka_williamsa = None
elif wybor == 3:
    maksymalna_strata = float(input("Podaj maksymalną dopuszczalną stratę (USD): "))
    ryzyko_procent = 1.0  # Ustawienie domyślnej wartości ryzyko_procent na 1%
    ryzyko_kwota = None
    stala_ryzyka_williamsa = None
elif wybor == 4:
    stala_ryzyka_williamsa = float(input("Podaj stałą ryzyka Williamsa (współczynnik ryzyka 0-1): "))
    maksymalna_strata = None
    ryzyko_procent = None
    ryzyko_kwota = None
else:
    print("Nieprawidłowy numer wersji symulacji.")
    exit()

# Dodatkowe opcje Monte Carlo
liczba_symulacji = int(input("Podaj liczbę symulacji Monte Carlo: "))

for i in range(liczba_symulacji):
    historia_kapitalu = symulacja_monte_carlo(poczatkowy_kapital, liczba_transakcji, prawdopodobienstwo_wygranej, ryzyko_procent=ryzyko_procent, ryzyko_kwota=ryzyko_kwota, maksymalna_strata=maksymalna_strata, stala_ryzyka_williamsa=stala_ryzyka_williamsa)
    rysuj_wykres(historia_kapitalu, f'Symulacja {str(i + 1)}')

# Rysowanie wykresu
plt.title("Symulacja Monte Carlo")
plt.xlabel("Liczba Transakcji")
plt.ylabel("Kapitał")
plt.legend()
plt.show()




