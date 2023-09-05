import random  # Importe le module random pour générer un nombre aléatoire.


def jeu_deviner_nombre():
    # Génère un nombre aléatoire entre 1 et 5.
    nombre_secret = random.randint(1, 5)

    # Demande à l'utilisateur de deviner le nombre.
    while True:
        try:
            guess = int(input("Devine un nombre entre 1 et 5 : "))  # Demande à l'utilisateur de saisir un nombre.

            # Vérifie si la devinette est en dehors de la plage autorisée.
            if guess < 1 or guess > 5:
                print("Le nombre doit être entre 1 et 5.")
                continue  # Réitère la boucle pour une nouvelle tentative.

            # Vérifie si la devinette est correcte.
            if guess == nombre_secret:
                print("Félicitations ! Tu as deviné le nombre.")
                break  # Sort de la boucle si la devinette est correcte.
            else:
                print("Essaie encore. Ce n'est pas le bon nombre.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")  # Gère les erreurs de saisie non numérique.

    # Fin du jeu.


# Appelle la fonction pour commencer le jeu.
jeu_deviner_nombre()
