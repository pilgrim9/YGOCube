import json
import csv
import requests
import os

HEADERS = [
    "name",
    "type",
    "attribute",
    "race",
    "level",
    "atk",
    "def",
    "image",
    "desc",
]

API = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

CARD_LIST = [
    "Nova Summoner",
    "Koa'ki Meiru Bergzak",
    "Dark Nephthys",
    "Kuraz the Light Monarch",
    "Labyrinth Barrage",
    "Gorz the Emissary of Darkness",
    "Koa'ki Meiru Drago",
    "Koa'ki Meiru Gravirose",
    "Koa'ki Meiru Powerhand",
]

OUTPUT_FILE = "cardinfo.csv"


def get_columns(card_names: list, output_file: str, columns: list):
    response = requests.get(API+"?name="+"|".join(card_names)).json()
    cards = response.get("data", [])
    if not cards:
        print("empty response")
        return

    for card in cards:
        card["image"] = card["card_images"][0]["image_url_cropped"]
    with open(get_dir()+output_file, "w+", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, columns, extrasaction="ignore")
        writer.writerows(cards)


def get_dir():
    return os.getcwd()+"\\"


def load_card_names(input_file):
    with open(get_dir()+input_file, "r", encoding="utf-8", newline='') as f:
        reader = csv.reader(f)
        return [line[0] for line in reader]


if __name__ == '__main__':
    get_columns(CARD_LIST, OUTPUT_FILE, HEADERS)
