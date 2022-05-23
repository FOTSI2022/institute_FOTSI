'''
Exercise 4 : How Many Characters In A Sentence ?
Instructions
Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
'''

'''
def characters_in_a_sentence():
    #my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    my_text = "papa est ici"
    number_characters=len(my_text)
    print(f"The number of characters is {number_characters}")
characters_in_a_sentence()

'''
'''
Exercise 5: Longest Word Without A Specific Character
Instructions
Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
'''

def longest_sentence_without_A():
    sentence=input('Give the longest sentence without the character A.....')
    print(sentence)

    #transform to uppercase
    sentence_uppercase=sentence.upper()
    print(sentence_uppercase)

    # transform to list
    sentence_uppercase_list=list(sentence_uppercase)
    print(sentence_uppercase_list)

    A_present=False
    A="A"

    if A in  sentence_uppercase_list:
        A_present=True

    if A_present:
        print("The sentence has the word A.....YOU LOST")
    else:
        print(f" Congratulations.......Your sentence {sentence} has not the word A")

longest_sentence_without_A()