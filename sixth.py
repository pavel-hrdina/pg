import sys

import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    response = requests.get(url)
    if response.status_code == 200:
        odkazy = response.content.decode("utf-8")
        hrefs = []
        # Ziskani vsech odkazu
        while odkazy.find("<a href=") != -1:
            start_index = odkazy.find("<a href=")
            end_index = odkazy.find(">", start_index)
            href = odkazy[start_index + 9:end_index - 1]
            hrefs.append(href)
            odkazy = odkazy[end_index + 1:]
        return hrefs
    else:
        print("Chyba pri stahovani stranky")
        return []


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        download_url_and_get_all_hrefs(url)
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
