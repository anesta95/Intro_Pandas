import pandas as pd
from functools import reduce

import os
os.chdir('C:/Users/Adrian/Documents/Data_Journalism/DataCamp\
         Lesson Datafiles/')
tweets_df = pd.read_csv('tweets.csv')


def shout():
    shout_word = 'congratulations' + '!!!'
    print(shout_word)


shout()


def shout2(word):
    shout_word = word + '!!!'
    print(shout_word)


shout2('congratulations')


def shout3(word):
    shout_word = word + '!!!'
    return shout_word


yell = shout3('congratulations')

print(yell)


def shout4(word1, word2):
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    new_shout = shout1 + shout2
    return new_shout


yell = shout4('congratulations', 'you')
print(yell)


def shout_all(word1, word2):
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    shout_words = (shout1, shout2)
    return shout_words


yell1, yell2 = shout_all('congratulations', 'you')


print(yell1)
print(yell2)

team = "teen titans"


def change_teams():
    global team
    team = "justice league"


print(team)

change_teams()

print(team)


def three_shouts(word1, word2, word3):
    def inner(word):
        return word + '!!!'
    return (inner(word1), inner(word2), inner(word3))


print(three_shouts('a', 'b', 'c'))


def echo(n):
    def inner_echo(word1):
        echo_word = word1 * n
        return echo_word
    return inner_echo


twice = echo(2)
thrice = echo(3)
print(twice('hello'), thrice('hello'))


def echo_shout(word):
    echo_word = word + word
    print(echo_word)

    def shout1():
        nonlocal echo_word
        echo_word = echo_word + '!!!'
    shout1()
    print(echo_word)


print(echo_shout('hello'))


def shout_echo(word1, echo=1):
    echo_word = word1 * echo
    shout_word = echo_word + '!!!'
    return shout_word


no_echo = shout_echo('Hey')
with_echo = shout_echo('Hey', 5)

print(no_echo, with_echo)


def shout_echo2(word1, echo=1, intense=False):
    echo_word = word1 * echo
    if intense is True:
        echo_word_new = echo_word.upper() + '!!!'
    else:
        echo_word_new = echo_word + '!!!'
    return echo_word_new


with_big_echo = shout_echo2("Yo", 5, True)
big_no_echo = shout_echo2("Yo", intense=True)
nothing_at_all = shout_echo2("Yo")
print(with_big_echo, big_no_echo, nothing_at_all)


def gibberish(*args):
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge


one_word = gibberish('luke')
many_words = gibberish("luke", "leia", "han", "obi", "darth")

print(one_word, many_words)


def report_status(**kwargs):
    print("\nBEGIN: REPORT\n")
    for key, value in kwargs.items():
        print(key + ' : ' + value)
    print('\nEND REPORT')


report_status(name="luke", affiliation="jedi", status="missing")
report_status(name="anakin", affiliation="sith lord", status="deceased")


def count_entries(df, col_name):
    cols_count = {}
    col = df[col_name]
    for entry in col:
        if entry in cols_count.keys():
            cols_count[entry] += 1
        else:
            cols_count[entry] = 1
    return cols_count


result1 = count_entries(tweets_df, 'lang')
result2 = count_entries(tweets_df, 'source')

print(result1, result2)


def count_entries_flex(df, *args):
    cols_count = {}
    for col_name in args:
        col = df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
    return cols_count


result3 = count_entries_flex(tweets_df, 'lang')
result4 = count_entries_flex(tweets_df, 'lang', 'source')
print(result3, result4)

echo_word = (lambda word1, echo: word1 * echo)
result = echo_word('hey', 5)
print(result)

spells = ["protego", "accio", "expecto patronum", "legilimens"]
shout_spells = map(lambda spell: spell + '!!!', spells)
shout_spells_list = list(shout_spells)

print(shout_spells_list)

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir',
              'legolas', 'gimli', 'gandalf']

result5 = filter(lambda character: len(character) > 6, fellowship)
result_list = list(result5)
print(result_list)

stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
result6 = reduce(lambda item1, item2: item1 + item2, stark)

print(result6)


def shout_echo3(word1, echo=1):
    echo_word = ''
    shout_words = ''
    try:
        echo_word = word1 * echo
        shout_words = echo_word + '!!!'
    except TypeError:
        print("word1 must be a string and echo must be an integer.")
    return shout_words


shout_echo3("particle", echo="accelerator")


def shout_echo4(word1, echo=1):
    if echo < 0:
        raise ValueError('echo must be greater than 0')
    echo_word = word1 * echo
    shout_words = echo_word + '!!!'
    return shout_words


shout_echo4("particle", echo=-5)


result7 = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

results_list2 = list(result7)

for tweet in results_list2:
    print(tweet)
