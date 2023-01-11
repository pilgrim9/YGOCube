from fetch_card_info import load_card_names, get_columns

INPUT_FILE = "cube_list_names.csv"
OUTPUT_FILE = "cube_list_codes.csv"

if __name__ == '__main__':
    get_columns(load_card_names(INPUT_FILE), OUTPUT_FILE, ["id"])
