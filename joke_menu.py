from joke import Joke


class Joke_Menu:
    def menu():
        print("""\n1. Print all dad jokes
2. Print random dad joke
3. Print chosen dad joke
4. Print the number of dad jokes in the database
5. Print random joke statement with random punchline
6. Add your own dad joke
0. Quit program
\n""")

    def option_menu(option):
        if option == '1':
            Joke.print_jokes()
        elif option == '2':
            Joke.random_joke()
        elif option == '3':
            joke_number = int(input(f"Enter the number from 1 to {Joke.joke_count()} : "))
            Joke.specific_joke(joke_number)
        elif option == '4':
            print("We have", Joke.joke_count(), "jokes in our database ")
        elif option == '5':
            Joke.random_joke_random_punchline()
        elif option == '6':
            statement = str(input("Enter statement of your dad joke: "))
            punchline = str(input("Enter punchline of your dad joke: "))
            print(Joke.add_new_joke(statement, punchline))
        elif option == '0':
            print("Quiting program")
            quit()
        else:
            print("Invalid input try again")