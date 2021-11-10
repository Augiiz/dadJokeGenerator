from random_joke_integer import Random_Joke_Integer as RJI
from filter import Filter


class Joke:
    joke_list = []

    def list_len():
        return len(Joke.joke_list) - 1

    def print_jokes():
        for joke in Joke.joke_list:
            for pt in joke:
                print(pt)
            print('\n')

    def random_joke():
        x = RJI.get_int(Joke.list_len())
        print(Joke.joke_list[x][0])
        print(Joke.joke_list[x][1])

    def specific_joke(number):
        print(Joke.joke_list[number - 1][0])
        print(Joke.joke_list[number - 1][1])

    def joke_count():
        return len(Joke.joke_list)

    def random_joke_random_punchline():
        statement_num = RJI.get_int(Joke.list_len())
        punchline_num = RJI.get_int(Joke.list_len())
        while (statement_num == punchline_num):
            punchline_num = RJI.get_int(Joke.list_len())
        print(Joke.joke_list[statement_num][0])
        print(Joke.joke_list[punchline_num][1])

    def add_new_joke(statement, punchline):
        if Filter.filter_new_joke(statement, punchline) is True:
            Joke.joke_list.append([statement, punchline])
            return "Joke has been added succesfully"
        elif Filter.filter_new_joke(statement, punchline) is False:
            return "Statement and punchline can not be left empty"
        else:
            return f"You can not use these words: {Filter.filter_new_joke(statement, punchline)}"