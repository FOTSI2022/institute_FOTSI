""" TIC TAC TOE
"""
"""
Analyse de l'exercice
Pour créer ce jeu, nous allons uiliser 5 fonctions
-print_results: pour afficher les resultats
-verif_results: pour vérifier si un joueur donné a gagné
-saisie_O: pour permettre le joueur de O de saisir son resultat
-saisir_X: pour permettre le joueur X de saisir son resultat

Le jeu se déclinera donc globalement en:
 print_results()
 saisi_O()
 verif_results()
 saisi_X()
 verif_results()
 
 Nous aurons besoin suivant nos analyses à trois variables globales matrix_jeu, nombre_case_non_vide et jeu_non_fin
"""
#Déclaration de la matrice
matrix_jeu=[[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
            ]
#Initialisation de la variable jeu_non_fini de type boolean
jeu_non_fini=True
O_vainqueur=False
X_vainqueur=False

#Initialisation de la variable nombre_case_non_vide
#initialisation du compteur
nombre_case_non_vide=0
for i in range(0,len(matrix_jeu)):
    nombre_case_non_vide +=len(matrix_jeu[i])
#print(nombre_case_non_vide)

#creation de la fonction print_results()
def print_results():
    print("Welcome to TIC TAC TOE !!!")
    print('***************')
    print(f"*  {matrix_jeu[0][0]} | {matrix_jeu[0][1]} | {matrix_jeu[0][2]}  *")
    print('-----|---|------')
    print(f"*  {matrix_jeu[1][0]} | {matrix_jeu[1][1]} | {matrix_jeu[1][2]}  *")
    print('-----|---|------')
    print(f"*  {matrix_jeu[2][0]} | {matrix_jeu[2][1]} | {matrix_jeu[2][2]}  *")
    print('***************')
#print_results()

#creation de la fonction de controle la saisine d'un entier
def controle_x_et_y_saisies():
    x = 10000
    while not (1 <= x <= 3):
        x_saisi = input("Enter row...1, 2 or 3 :")
        try:
            x = int(x_saisi)
        except:
            print('X should be a integer...')

    y = 1000
    while not (1 <= y <= 3):
        y_saisi = input("Enter column...1, 2 or 3 :")
        try:
            y = int(y_saisi)
        except:
            print('Y should be a integer...')
    return x-1, y-1
# En faisant la soustraction x-1 et y-1, celà permet de prendre en compte le principe d'indexation dans la matrice

#(a, b)=controle_x_et_y_saisies()
#print(a)
#print(b)

#creation de la fonction saisi_O()
def saisi_O():
    global nombre_case_non_vide
    print("Player O's turn...")
    (x, y) = controle_x_et_y_saisies()
    while matrix_jeu[x][y] != ' ':
        print('Impossible this case is already filled, choose another one..')
        (x, y) = controle_x_et_y_saisies()
    else:
        matrix_jeu[x][y] = 'O'
        nombre_case_non_vide -= 1
#saisi_O()
#print_results()

#creation de la fonction saisi_X()
def saisi_X():
    global nombre_case_non_vide
    print("Player X's turn...")
    (x, y) = controle_x_et_y_saisies()
    while matrix_jeu[x][y] != ' ':
        print('Impossible this case is already filled, choose another one..')
        (x, y) = controle_x_et_y_saisies()
    else:
        matrix_jeu[x][y] = 'X'
        nombre_case_non_vide-=1
#saisi_X()
#print_results()

#creation de la fonction verification de resultats verif_results()
def verif_results():
    global jeu_non_fini, O_vainqueur, X_vainqueur
    # On fixe la ligne i du tableau
    for i in range(0,3):
        result_ligne=''
        # On parcours les colonnes du tableau sur la ligne i
        for k in range(0,3):
            result_ligne=matrix_jeu[i][k]+result_ligne
        if result_ligne=='XXX':
            # On altère la valeur de jeu_non_fini
            jeu_non_fini=False
            X_vainqueur = True
        if result_ligne=='OOO':
            # On altère la valeur de jeu_non_fini
            jeu_non_fini=False
            O_vainqueur = True

    # On fixe la ligne k du tableau
    for k in range(0,3):
        result_colonne=''
        # On parcours les lignes du tableau sur la colonne k
        for i in range(0,3):
            result_colonne=matrix_jeu[i][k]+result_colonne

        if result_colonne=='XXX':
            # On altère la valeur de jeu_non_fini
            jeu_non_fini=False
            X_vainqueur=True
        if result_colonne=='OOO':
            # On altère la valeur de jeu_non_fini
            jeu_non_fini=False
            O_vainqueur = True
    return jeu_non_fini, O_vainqueur , X_vainqueur
#(jeu_non_fini, O_vainqueur , X_vainqueur)=verif_results()

#Sequence finale du code

while jeu_non_fini and nombre_case_non_vide !=0:
    print_results()
    print(nombre_case_non_vide)
    saisi_X()
    print_results()
    (jeu_non_fini, O_vainqueur , X_vainqueur)=verif_results()
    if X_vainqueur:
        print("Player X win")
    else:
        if nombre_case_non_vide == 0:
            print("End of game. No one has won")
        else:
            saisi_O()
            (jeu_non_fini, O_vainqueur, X_vainqueur) = verif_results()
            if O_vainqueur:
                print("Player O win......GOODBYE")









