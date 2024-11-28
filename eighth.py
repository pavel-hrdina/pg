#     implementujte  funkci bin_to_dec(), která
#     bude konvertovat binární číslo 10011101 na decimální 167, číslo
#     může být do funkce předáno jako str i jako int


def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    # 2 znamena, ze cislo je v binarni soustave
    return int(str(binarni_cislo), 2)


def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
