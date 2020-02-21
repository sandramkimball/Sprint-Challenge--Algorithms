'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of *"th"* occur within `word`. Case matters.
Your function must utilize recursion. No loops.
'''
def count_th(word):
    count = 0
    i = 0

    if len(word) >= 2 and i < len(word)-1:
        if word[:2] == 'th':
            count += 1
            i += 1
            return 1 + count_th(word[2:])
        else: 
            return 0 + count_th(word[1:])

    # count += count_th(word)
    return count



count_th('ABCDEth')