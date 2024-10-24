def _pohyb_pesce(start_pozice, cil_pozice, obsazene_pozice):
    """Kontrola pohybu pěšce"""
    start_radek, start_sloupec = start_pozice
    cil_radek, cil_sloupec = cil_pozice

    if cil_sloupec != start_sloupec:  # Nemůže se pohybovat do stran
        return False

    # Standardní tah o jedno pole
    if cil_radek == start_radek + 1:
        return cil_pozice not in obsazene_pozice

    # Tah o dvě pole pouze z první řady
    if start_radek == 1 and cil_radek == 3:  # změna z 2 na 1 a z 4 na 3
        # Kontrola, zda není překážka v cestě a cílové pole není obsazené
        mezipozice = (start_radek + 1, cil_sloupec)
        return (mezipozice not in obsazene_pozice and
                cil_pozice not in obsazene_pozice)
    return False


def _pohyb_jezdce(start_pozice, cil_pozice, _):
    """Kontrola pohybu jezdce"""
    start_radek, start_sloupec = start_pozice
    cil_radek, cil_sloupec = cil_pozice
    radek_diff = abs(cil_radek - start_radek)
    sloupec_diff = abs(cil_sloupec - start_sloupec)
    return (radek_diff == 2 and sloupec_diff == 1) or (radek_diff == 1 and sloupec_diff == 2)


def _pohyb_veze(start_pozice, cil_pozice, obsazene_pozice):
    """Kontrola pohybu věže"""
    start_radek, start_sloupec = start_pozice
    cil_radek, cil_sloupec = cil_pozice
    if cil_radek != start_radek and cil_sloupec != start_sloupec:
        return False
    return _je_cesta_volna(start_radek, start_sloupec, cil_radek, cil_sloupec, obsazene_pozice)


def _pohyb_strelce(start_pozice, cil_pozice, obsazene_pozice):
    """Kontrola pohybu střelce"""
    start_radek, start_sloupec = start_pozice
    cil_radek, cil_sloupec = cil_pozice
    if abs(cil_radek - start_radek) != abs(cil_sloupec - start_sloupec):
        return False
    return _je_cesta_volna(start_radek, start_sloupec, cil_radek, cil_sloupec, obsazene_pozice)


def _pohyb_damy(start_pozice, cil_pozice, obsazene_pozice):
    """Kontrola pohybu dámy"""
    start_radek, start_sloupec = start_pozice
    cil_radek, cil_sloupec = cil_pozice
    if (cil_radek == start_radek or cil_sloupec == start_sloupec or
            abs(cil_radek - start_radek) == abs(cil_sloupec - start_sloupec)):
        return _je_cesta_volna(start_radek, start_sloupec, cil_radek, cil_sloupec, obsazene_pozice)
    return False


def _pohyb_krale(start_pozice, cil_pozice, _):
    """Kontrola pohybu krále"""
    start_radek, start_sloupec = start_pozice
    cil_radek, cil_sloupec = cil_pozice
    return abs(cil_radek - start_radek) <= 1 and abs(cil_sloupec - start_sloupec) <= 1


def _je_cesta_volna(start_radek, start_sloupec, cil_radek, cil_sloupec, obsazene_pozice):
    """Pomocná funkce pro kontrolu, zda je cesta mezi dvěma body volná."""
    # Určení směru pohybu
    radek_krok = 0 if start_radek == cil_radek else (cil_radek - start_radek) // abs(cil_radek - start_radek)
    sloupec_krok = 0 if start_sloupec == cil_sloupec else (cil_sloupec - start_sloupec) // abs(
        cil_sloupec - start_sloupec)

    # Kontrola všech polí na cestě (kromě cílového)
    radek, sloupec = start_radek + radek_krok, start_sloupec + sloupec_krok
    while (radek, sloupec) != (cil_radek, cil_sloupec):
        if (radek, sloupec) in obsazene_pozice:
            return False
        radek += radek_krok
        sloupec += sloupec_krok

    return True


# Slovník mapující typy figur na jejich kontrolní funkce
KONTROLY_POHYBU = {
    "pěšec": _pohyb_pesce,
    "jezdec": _pohyb_jezdce,
    "věž": _pohyb_veze,
    "střelec": _pohyb_strelce,
    "dáma": _pohyb_damy,
    "král": _pohyb_krale
}


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.

    :return: True, pokud je tah možný, jinak False.
    """
    # 1. Kontrola, zda je cílová pozice na šachovnici
    radek, sloupec = cilova_pozice
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False

    # 2. Kontrola, zda není cílová pozice obsazená
    if cilova_pozice in obsazene_pozice:
        return False

    # Pokud je cílová pozice stejná jako aktuální, tah není možný
    if cilova_pozice == figurka["pozice"]:
        return False

    # 3. Kontrola pohybu podle typu figury
    kontrola_pohybu = KONTROLY_POHYBU.get(figurka["typ"])
    if kontrola_pohybu:
        return kontrola_pohybu(figurka["pozice"], cilova_pozice, obsazene_pozice)

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2),
                       obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4),
                       obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
