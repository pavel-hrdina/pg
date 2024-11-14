import sys

import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Chyba pri stahovani stranky: {e}")
        return []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        hrefs = [a['href'] for a in soup.find_all('a', href=True)]
        return hrefs

    return []


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
