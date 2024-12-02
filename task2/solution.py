import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict

URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"


def get_animal_counts(url):
    counts = defaultdict(int)
    while url:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.select("#mw-pages .mw-category a"):
            first_letter = link.text[0].upper()
            counts[first_letter] += 1

        next_page = soup.select_one('a:contains("Следующая страница")')
        url = f"https://ru.wikipedia.org{next_page['href']}" if next_page else None

    return counts


def save_to_csv(counts, filename="beasts.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for letter, count in sorted(counts.items()):
            writer.writerow([letter, count])


animal_counts = get_animal_counts(URL)
save_to_csv(animal_counts)
