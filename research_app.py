from src.parser import load_history
from src.research import search_track

df = load_history()

while True:

    print()

    print("=" * 40)
    print("Spotify History Research")
    print("=" * 40)

    print()

    print("1 - Pesquisar música")

    print("0 - Sair")

    print()

    option = input("> ")

    if option == "0":
        break

    if option == "1":

        nome = input("\nNome da música: ")

        print()

        search_track(df, nome)