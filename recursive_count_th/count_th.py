'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if word.find('th') > -1:
        rep = word.replace('th', '*')
        return count_th(rep)

    return word.count('*')


# print(count_th("thhtthht"))
# print(count_th("abcthefthghith"))
# print(count_th("abc"))
