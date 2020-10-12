'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th_1(word):
    if word.find('th') > -1:
        rep = word.replace('th', '*')
        return count_th(rep)

    return word.count('*')


def count_th(word):
    find = 'th'
    # if word < find stop the recursion and carry value up
    if len(word) < len(find):
        return 0
    # if 'th' found, return 1
    if word[0:len(find)] == find:
        return count_th(word[len(find) - 1:]) + 1
    # if not just keep going
    return count_th(word[len(find) - 1:])


print(count_th("thhtthht"))
# print(count_th("abcthefthghith"))
# print(count_th("abc"))
# print(count_th("ath-bth-cth"))
