def sude_nebo_liche(cislo: int) -> None:
    """
    Funkce, která zjistí, zda je číslo sudé nebo liché.

    :param cislo: int
    :return: none
    """
    if cislo % 2 == 0:
        print(f"{cislo} je sudé.")
    else:
        print(f"{cislo} je liché.")


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    sude_nebo_liche(cislo)
