from games_report import get_all_consoles


def test_get_all_consoles():
    data = [
        {
            "Title": "Lumines: Puzzle Fusion",
            "Metrics": {
                "Sales": 0.56,
            },
            "Release": {
                "Console": "Sony PSP",
                "Year": 2004,
            },
        },
        {
            "Title": "Hot Shots Golf: Open Tee",
            "Metrics": {
                "Sales": 0.49,
            },
            "Release": {
                "Console": "Sony PSP",
                "Year": 2004,
            },
        },
        {
            "Title": "Spider-Man 2",
            "Metrics": {
                "Sales": 0.45,
            },
            "Release": {
                "Console": "Nintendo DS",
                "Year": 2004,
            },
        },
        {
            "Title": "The Urbz: Sims in the City",
            "Metrics": {
                "Sales": 0.41,
            },
            "Release": {
                "Console": "Nintendo 64",
                "Year": 2004,
            },
        },
        {
            "Title": "WarioWare Touched!",
            "Metrics": {
                "Sales": 0.54,
            },
            "Release": {
                "Console": "Nintendo DS",
                "Year": 2004,
            },
        },
    ]
    consoles = get_all_consoles(data)
    assert consoles == {"Sony PSP", "Nintendo DS", "Nintendo 64"}
