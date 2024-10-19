def cislo_text(cislo):
    """
    Funkce zkonvertuje číslo do jeho textové reprezentace
    např: "25" -> "dvacet pět", omezte se na čísla od 0 do 100.
    :param cislo: číslo jako string
    :return: textová reprezentace čísla
    """
    cislo = int(cislo)

    if cislo < 0 or cislo > 100:
        return "Číslo mimo povolený rozsah"

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desítky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    speciální = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct",
                 "devatenáct"]

    if cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return speciální[cislo - 10]
    elif cislo < 100:
        des = desítky[cislo // 10]
        jed = jednotky[cislo % 10]
        return des + (f" {jed}" if jed != "nula" else "")
    else:  # cislo == 100
        return "sto"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
