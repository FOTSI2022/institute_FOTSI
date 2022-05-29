
"""
En cryptographie, un chiffrement de César est l'une des techniques de chiffrement les plus simples et les plus connues.
C'est un type de chiffrement par substitution dans lequel chaque lettre du texte en clair est remplacée par une lettre à un nombre fixe de positions dans l'alphabet.

Par exemple, avec un décalage à gauche de 3 -> D serait remplacé par A,
–> E deviendrait B, et ainsi de suite.

La méthode porte le nom de Jules César, qui l'a utilisée dans sa correspondance privée.

Créez un programme python qui crypte et décrypte les messages avec le chiffrement césar.
L'utilisateur entre dans le programme, puis le programme lui demande s'il veut chiffrer ou déchiffrer, puis exécuter le chiffrement/déchiffrement sur un message donné et un décalage donné.
"""
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(alphabet)
print(len(alphabet))

operation_a_faire=int(input("Que voulez-vous faire: 1-CRIPTER....2-DECRYPTER...."))
if operation_a_faire==1:
    chiffre = int(input('Enter le chiffre sur lequel est basé le chiffrement...Ce chiffre doit être inférieur ou égal à 25..'))
    message = input('Entrer le message à chiffrer...')

    # on recupere chaque mot de la phrase et le met dans un tableau pour codifier
    message_list = message.split(' ')
    print(message_list)
    # on parcours chaque mot du message
    for mot in message_list:
        #print(mot)
        # on garde son index. Cet index sera utilisé pour réintégrer le mot dans le tableau
        index_mot = message_list.index(mot)
        # on cree une variable qui nous permettra de convertir nos mots
        mot_modifie=''
        # on parcours chaque lettre du mot
        for i in range(0, len(mot)):
            # on copie la lettre correspondante. on va aller le convertir dans l'alphabet en fonction du chiffrement
            j = mot[i]
            #print("j: "+j)
            # on prends son index dans alphabet
            j_index_alphabet = alphabet.index(j)
            #print(j_index_alphabet)
            # on chiffre index de j
            if j_index_alphabet + chiffre > 25:
                j_index_alphabet_chiffre = (j_index_alphabet + chiffre)%25-1
            else:
                j_index_alphabet_chiffre = j_index_alphabet + chiffre
            #print(j_index_alphabet_chiffre)
            # on recupere la nouvelle lettre correspond dans l alphabet
            j_nouveau = alphabet[j_index_alphabet_chiffre]
            #print(j_nouveau)
            # modifions le mot
            mot_modifie = mot_modifie+ j_nouveau
            #print(mot_modifie)
        # on garde le mot converti
        message_list[index_mot] = mot_modifie
        #print(message_list)
    # on affiche le message initial
    print("message initial")
    print(message)
    # on affiche le message convertit
    print("message cripté")
    mes_crip=''
    for p in message_list:
        mes_crip+=p+' '
    print(mes_crip)
else:
    chiffre = int(
        input('Enter le chiffre sur lequel est basé le chiffrement...Ce chiffre doit être inférieur ou égal à 25..'))
    message = input('Entrer le message à chiffrer...')

    # on recupere chaque mot de la phrase et le met dans un tableau pour codifier
    message_list = message.split(' ')
    print(message_list)
    # on parcours chaque mot du message
    for mot in message_list:
        # print(mot)
        # on garde son index. Cet index sera utilisé pour réintégrer le mot dans le tableau
        index_mot = message_list.index(mot)
        # on cree une variable qui nous permettra de convertir nos mots
        mot_modifie = ''
        # on parcours chaque lettre du mot
        for i in range(0, len(mot)):
            # on copie la lettre correspondante. on va aller le convertir dans l'alphabet en fonction du chiffrement
            j = mot[i]
            # print("j: "+j)
            # on prends son index dans alphabet
            j_index_alphabet = alphabet.index(j)
            # print(j_index_alphabet)
            # on chiffre index de j
            if j_index_alphabet - chiffre < 0:
                j_index_alphabet_chiffre = 26 + j_index_alphabet - chiffre
            else:
                j_index_alphabet_chiffre = j_index_alphabet - chiffre
            # print(j_index_alphabet_chiffre)
            # on recupere la nouvelle lettre correspond dans l alphabet
            j_nouveau = alphabet[j_index_alphabet_chiffre]
            # print(j_nouveau)
            # modifions le mot
            mot_modifie = mot_modifie + j_nouveau
            # print(mot_modifie)
        # on garde le mot converti
        message_list[index_mot] = mot_modifie
        # print(message_list)
    # on affiche le message initial
    print("message initial")
    print(message)
    # on affiche le message convertit
    print("message cripté")
    mes_crip = ''
    for p in message_list:
        mes_crip += p + ' '
    print(mes_crip)





