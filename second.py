def cislo_text(cislo: int) -> str:
    """
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

    :param cislo: int
    :return: str
    """
    if cislo <= 0 or cislo >= 100:
        return "Mimo rozsah"

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát",
               "devadesát"]

    if cislo % 10 == 0:
        return desitky[cislo // 10]
    elif cislo < 10:
        return jednotky[cislo]
    else:
        return desitky[cislo // 10] + " " + jednotky[cislo % 10]


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)
