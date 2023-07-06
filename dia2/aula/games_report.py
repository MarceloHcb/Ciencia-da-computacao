import json

def load_games_from_json(file_path):
    games = []
    try:        
        with open(file_path, "r") as file:
            games = json.load(file)
    except FileNotFoundError:
        # print("Arquivo não encontrado!")
        raise FileNotFoundError("Arquivo não encontrado!")
    except json.decoder.JSONDecodeError:
        print("Arquivo inválido")

    return games

def get_all_consoles(games_data):
    all_consoles = set()
    for game in games_data:
        console = game["Release"]["Console"]
        all_consoles.add(console)
    return all_consoles

def get_sales_by_console(games_data: list[dict]) ->dict:
    result = dict()
    for game in games_data:
        console = game["Release"]["Console"]
        sales = game["Metrics"]["Sales"]

        if console in result:
            result[console] += sales
        else:
            result[console] = sales
    return result


if __name__ == "__main__":
    video_games = load_games_from_json("data/video_games.json")
    consoles = get_all_consoles(video_games)
    print(f"Consoles:/n {consoles} ")
    print(f"Vendas (U$k):\n {get_sales_by_console(video_games)}")

