import sys

# upravte v těle programu v if __name__ == '__main__' tak, aby z příkazové
# řádky četl název obrázku, pro který chcete zjistit typ, ošetřete případné vyjímky v bloku try-except
# upravte funkci read_header(file_name, header_length), aby načítala prvních header_length
# bytů ze souboru jehož jméno je předáno v parametru file_name upravte funkce is_jpeg, is_gif
# a is_png, aby vrátily True, pokud je obrázek daného typu, nebo False, pokud není

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    with open(file_name, 'rb') as file:
        return file.read(header_length)


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))

    # vyhodnoť zda je soubor jpeg
    if header == jpeg_header:
        return True
    else:
        return False


def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    # vyhodnoť zda je soubor gif
    if read_header(file_name, len(gif_header1)) == gif_header1 or read_header(file_name,
                                                                              len(gif_header2)) == gif_header2:
        return True
    else:
        return False


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    # vyhodnoť zda je soubor png
    if read_header(file_name, len(png_header)) == png_header:
        return True
    else:
        return False


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    # přidej try-catch blok, odchyť obecnou vyjímku Exception a vypiš ji
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except Exception as e:
        print(f'Chyba: {e}')
