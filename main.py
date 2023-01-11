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


def main():
    response = requests.get(API+"?name="+"|".join(CARD_LIST))
    cards: list = response.json().get("data", [])
    if not cards:
        print("empty response")
        return

    for card in cards:
        card["image"] = card["card_images"][0]["image_url_cropped"]
    with open(os.getcwd()+OUTPUT_FILE, "w+", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, HEADERS, extrasaction="ignore")
        writer.writerows(cards)


if __name__ == '__main__':
    main()

