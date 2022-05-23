#Exercice nombre magique
'''
Le programme doit demander choisir un nombre aléatoire et demander à l'utilisateur de le retrouver
L'utilisateur a un nombre de vie limité à renseigner au départ
Le nombre à retrouver doit être dans un intervalle prédéfini
Au terme du jeu, même si l'utilisateur a perdu, la réponse lui sera donnée
A chaque fois que l'utilisateur entre un nombre, on doit lui indiquer si le nombre est plus petit ou grand

******************************************************************
STRUCTURE DE MON CODE
******************************************************************
1-Ecrire une fonction qui demande le nom du joueur et le nom de vie pour le jeu
2-Ecrire une fonction qui demande l'intervalle du nombre magique et le prédéfinit
3-Ecrire la fonction qui permet effectivement de donner le nombre magique en prenant en compte les tres paramètres
'''

#Fonction de demande du nom et du nombre de vie du joueur
def demander_nomjoueur_nombreviejoueur():
    nomjoueur=""
    while nomjoueur=="":
        nomjoueur=input("Quel est votre nom?")
        if nomjoueur=="":
            print("Attention: Le nom ne doit pas être vide")

    nombre_vie=0
    while nombre_vie <=0:
        nombre_vie_saisi=input(f"{nomjoueur}, Quel est le nombre de vie pour le jeu que vous souhaitez?")
        try:
            nombre_vie=int(nombre_vie_saisi)
            if nombre_vie==0:
                print(f"{nomjoueur}, Le nombre de vie doit être un nombre entier positif")
        except:
            print(f"{nomjoueur}, Le nombre de vie doit être un nombre entier positif")

    return nomjoueur, nombre_vie
'''test fonction
(nom_joueur_valide, nombre_vie_valide) = demander_nomjoueur_nombreviejoueur()
print(nom_joueur_valide, nombre_vie_valide)
'''
#Fonction qui demande l'intervelle du nombre de vit et le prédéfinit
#on recupere les informations du joueur
(nom_joueur_valide, nombre_vie_valide) = demander_nomjoueur_nombreviejoueur()

def demander_intervalle_nombre_magique(nom_joueur_valide):
    borne_inferieur_nombre=-1
    while borne_inferieur_nombre<0:
        borne_inferieur_nombre_saisi=input("Quel est la valeur minimale du nombre magique?")
        try:
            borne_inferieur_nombre=int(borne_inferieur_nombre_saisi)
            if borne_inferieur_nombre<0:
                print(f"Attention {nom_joueur_valide}: Le nombre doit être positif")
        except:
            print(f"Attention {nom_joueur_valide}: Le nombre doit être positif")

    borne_superieur_nombre = 0
    while borne_superieur_nombre <= borne_inferieur_nombre:
        borne_superieur_nombre_saisi = input("Quel est la valeur maximale du nombre magique?")
        try:
            borne_superieur_nombre = int(borne_superieur_nombre_saisi)
            if borne_superieur_nombre <= borne_inferieur_nombre:
                print(f"Attention {nom_joueur_valide}: La valeur maximale doit être supérieure à la valeur minimale ({borne_inferieur_nombre})")
        except:
            print(f"Attention {nom_joueur_valide}: Le nombre doit être positif et supérieur à la valeur minimale ({borne_inferieur_nombre})")
    #tirage du nombre magique
    import random
    nombre_magique=random.randint(borne_inferieur_nombre,borne_superieur_nombre)

    return nombre_magique, borne_inferieur_nombre, borne_superieur_nombre


#recupere les infos obtenues par la fonction
(nombre_magique_valide, borne_inferieur_nombre_valide, borne_superieur_nombre_valide)=demander_intervalle_nombre_magique(nom_joueur_valide)


# Fonction qui s'assure que le nombre est un entier
def controle_nature_entier_nombre(borne_inferieur_nombre_valide, borne_superieur_nombre_valide):
    nombre_magique=0
    while nombre_magique==0:
        nombre_magique_saisi = input(f" Quel est le nombre magique situé entre {borne_inferieur_nombre_valide} et {borne_superieur_nombre_valide} :")
        try:
            nombre_magique=int(nombre_magique_saisi)
        except:
            print("Attention: Saisir un nombre")
    return nombre_magique


#fonction de message en cas de gain/perte
def menu_message_resultat(resultat=0):
    if resultat==0:
        print(f" GAME OVER {nom_joueur_valide}!!!! VOUS AVEZ PERDU")
        print(f" LE NOMBRE MAGIQUE SITUE ENTRE {borne_inferieur_nombre_valide} ET {borne_superieur_nombre_valide} est {nombre_magique_valide} ")
    else:
        print(f" BRAVO {nom_joueur_valide}!!!! VOUS AVEZ GAGNE")
        print(f" LE NOMBRE MAGIQUE SITUE ENTRE {borne_inferieur_nombre_valide} ET {borne_superieur_nombre_valide} est bel et bien {nombre_magique_valide} ")
        print(f" NOMBRE DE VIE RESTANTES :{nombre_vie_valide}")

# resultat est definit dans le nom de la fonction comme un paramètre optionnel
#menu_message_resultat()

#fonction de menu du jeu
def menu_nombre_magique():
    print("**************************************************************")
    print(f"BIENVENUE UNE FOIS DE PLUS {nom_joueur_valide} AU JEU DU NOMBRE MAGIQUE")
    print(f"NOMBRE DE CHANCES  POUR TROUVER LE NOMBRE MAGIQUE: {nombre_vie_valide}")
    print(f"RAPPEL LE NOMBRE MAGIQUE EST SITUE ENTRE :  {borne_inferieur_nombre_valide} ET {borne_superieur_nombre_valide} ")
    print("C'EST PARTI.............................................JOUONS")
    print("**************************************************************")
#appelle fonction de menu du jeu
menu_nombre_magique()


#fonction de recherche du nombre magique
'''LE principe en quelques mots
Le joueur entre le nombre, on le compare à la valeur du nombre magique
  -si le nombre est inferieur au nombre magique, on lui dit que c'est plus grand en changeant la borne inferieure
  -si le nombre est superieur au nombre magique, on lui dit que c'est plus plus petit en changeant la borne superieure
  -On rappelle le nombre de vie restant à chaque fois et le compare à 0
  -au cas ou nombre de vie est 0, on envoie le message de perte
  -en cas de victoire, on envoie le message de vie
'''
def recherche_nombre_magique(nombre_vie_valide):
    inferieur=borne_inferieur_nombre_valide
    superieur=borne_superieur_nombre_valide
    nombre_magique_saisi = -1

    while nombre_magique_saisi != nombre_magique_valide and nombre_vie_valide != 0:
        #Le bout de code suivant permet d'obliger le joueur à entrer un nombre dans l'intervalle
        condition = False
        #print(condition)
        while condition == False:
              nombre_magique_saisi=controle_nature_entier_nombre(inferieur, superieur)
              condition = nombre_magique_saisi >= inferieur and nombre_magique_saisi <= superieur
        # Fin du bout de code

        # code pour reaffecter les bornes

        if nombre_magique_saisi < nombre_magique_valide:
            inferieur=nombre_magique_saisi
        else:
            superieur = nombre_magique_saisi

        # Fin du code pour reaffecter les bornes
        nombre_vie_valide -= 1
        print(f"Nombre de vies restantes :{nombre_vie_valide} ")

    if nombre_magique_saisi == nombre_magique_valide:
        menu_message_resultat(1)
    else:
        menu_message_resultat()

recherche_nombre_magique(nombre_vie_valide)







