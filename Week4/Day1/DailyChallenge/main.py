'''
Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.

Then, print the first and last characters of the given text.

Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
'''

def build_up_a_string():
    text_string=input("Please give me a string...")

    if len(text_string)<10:
        print(f"<<{text_string}>> has just {len(text_string)} letters. string not long enough")
    else:
        print(f"<<{text_string}>> just {len(text_string)} letters. string too long")

    #Then, print the first and last characters of the given text.
    print(f"<<{text_string[0]}>> is the first character")
    print(f"<<{text_string[-1]}>> is the first character")
#build_up_a_string()

def construct_the_string():
    text_string=input("Please give me the sentence to construct...")

    number_character=len(text_string)
    character=""
    i=0

    while i <= number_character:
        print(character)
        if i<number_character:
            character = character+text_string[i]
        i+=1

#construct_the_string()


def shuffle_the_string():
    import random
    text_string=input("Please give me the sentence to construct...")
    text_string_list=list(text_string)

    random.shuffle(text_string_list)

    """ utiliser pour reconstruire"""
    final_text_string=""

    for i in text_string_list:
        final_text_string = final_text_string + i

    print(final_text_string)

shuffle_the_string()

