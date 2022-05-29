"""
Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
Display a little cake as seen below:
"""
def candle_birthday():
    birthday=input("Give me your birthday under the format DD/MM/YYYY....")
    number_candle=int(birthday[-1])

    #print("i"* number_candle)
    candle=""
    for i in range(0,number_candle):
        candle += 'i'
    print(candle)

    candle_ = ""
    for i in range(0, number_candle//2):
        if i<=3:
            candle_ += ' '
        else:
            candle_ += '_'
    print(candle_)

    ligne1=candle_+candle+candle_
    print(ligne1)

    print("__|:H:a:p:p:y:|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")
candle_birthday()


