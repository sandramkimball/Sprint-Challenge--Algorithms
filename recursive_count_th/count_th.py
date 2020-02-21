'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of *"th"* occur within `word`. Case matters.
Your function must utilize recursion. No loops.
'''
def count_th(word):
    count = 0
    i = 0
    
    if i == len(word):
        return count
        
    if word[i] + word[i+1] == 'th' and i < len(word)-1:
        print(f'if: {word[i]}{word[i+1]}')
        i += 1
        count += 1

    else:
        i += 1
        print(f'else: {word[i]}{word[i+1]}')

    
    count_th(word)
    return count



count_th('ABCDEth')