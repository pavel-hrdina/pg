def je_prvocislo(cislo: int) -> bool:
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.

    Napoveda jak otestova prvocislo:
    Cislo 36 vznikne nasobenim:
    1 * 36
    2 * 18
    3 * 12
    4 * 9
    6 * 6
    9 * 4
    12 * 3
    18 * 2
    36 * 1
    Jak vidite v druhe polovine se dvojice opakuji, tzn. v tomto pripade staci overit delitelnost pouze do 6 (vcetne)
    """
    if cislo <= 1:
        return False
    if cislo == 2:
        return True  # 2 is prime
    if cislo % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    for i in range(3, int(cislo ** 0.5) + 1, 2):  # Check only up to the square root
        if cislo % i == 0:
            return False
    return True


def vrat_prvocisla(maximum: int) -> list:
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    prvocisla = []
    for i in range(1, maximum + 1):
        if je_prvocislo(i):
            prvocisla.append(i)
    return prvocisla


if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    print(vrat_prvocisla(cislo))
