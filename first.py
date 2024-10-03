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


sude_nebo_liche(1000)
sude_nebo_liche(5)
