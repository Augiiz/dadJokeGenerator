from joke_menu import Joke_Menu
from starter_jokes import Starter_Jokes


def main():
    Joke_Menu.menu()
    option = str(input())
    Joke_Menu.option_menu(option)


if __name__ == "__main__":
    Starter_Jokes.fill_joke_list()
    while True:
        main()