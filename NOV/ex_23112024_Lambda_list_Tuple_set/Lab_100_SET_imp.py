#Write a program to find non repeating words in string using set
#string->swiss

def non_repetitive_word(string):
    for char in string:
        if string.count(char)==1:
            return char

    return None

print(non_repetitive_word("swiss"))
print(non_repetitive_word("pepper"))
print(non_repetitive_word("dada"))
print(non_repetitive_word("annushinha"))