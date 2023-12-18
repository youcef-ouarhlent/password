import hashlib
import json
import random
import string

chemin = 'password.json'

def verification_securite(choix_du_mot_de_passe):
    return (
        len(choix_du_mot_de_passe) >= 8 and
        any(c.isupper() for c in choix_du_mot_de_passe) and
        any(c.islower() for c in choix_du_mot_de_passe) and
        any(c.isdigit() for c in choix_du_mot_de_passe) and
        any(not c.isalnum() for c in choix_du_mot_de_passe)
    )

def generer_mot_de_passe():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(12))  # Générer un mot de passe aléatoire de longueur 12
    return mot_de_passe

def verifier_doublon_mot_de_passe(h):
    with open(chemin, "r") as fichier:
        try:
            liste = json.load(fichier)
        except json.decoder.JSONDecodeError:
            liste = []
    return h in liste

def creer_ou_generer_mot_de_passe():
    choix = input("Voulez-vous créer votre propre mot de passe (C) ou en générer un aléatoirement (G)? ").upper()
    
    if choix == 'C':
        mot_de_passe_valide = False
        while not mot_de_passe_valide:
            choix_du_mot_de_passe = input("Choisir un mot de passe qui contient au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial : ")
            
            if verification_securite(choix_du_mot_de_passe):
                mot_de_passe_valide = True
                print("Le mot de passe est sécurisé.")
                
                h = hashlib.sha256(choix_du_mot_de_passe.encode()).hexdigest()
                
                if verifier_doublon_mot_de_passe(h):
                    print("Ce mot de passe est déjà utilisé. Veuillez en choisir un autre.")
                    creer_ou_generer_mot_de_passe()
                else:
                    with open(chemin, "r") as fichier:
                        try:
                            liste = json.load(fichier)
                        except json.decoder.JSONDecodeError:
                            liste = []
                    liste.append(h)
                    with open(chemin, 'w') as fichier:
                        json.dump(liste, fichier, indent=4)
                        print("Le mot de passe haché est : ", h)
                        break
                    
            else:
                print("Le mot de passe n'est pas sécurisé. Veuillez réessayer.")
                if len(choix_du_mot_de_passe) < 8:
                    print("Le mot de passe doit contenir au moins 8 caractères")
                if not any(c.isupper() for c in choix_du_mot_de_passe):
                    print("Le mot de passe doit contenir au moins une majuscule")
                if not any(c.islower() for c in choix_du_mot_de_passe):
                    print("Le mot de passe doit contenir au moins une minuscule")
                if not any(c.isdigit() for c in choix_du_mot_de_passe):
                    print("Le mot de passe doit contenir au moins un chiffre")
                if not any(not c.isalnum() for c in choix_du_mot_de_passe):
                    print("Le mot de passe doit contenir au moins un caractère spécial")
    
    elif choix == 'G':
        mot_de_passe_aleatoire = generer_mot_de_passe()
        print("Le mot de passe généré aléatoirement est : ", mot_de_passe_aleatoire)
        h = hashlib.sha256(mot_de_passe_aleatoire.encode()).hexdigest()
        if verifier_doublon_mot_de_passe(h):
            print("Ce mot de passe aléatoire est déjà utilisé. Veuillez en générer un autre.")
            creer_ou_generer_mot_de_passe()
        else:
            with open(chemin, "r") as fichier:
                try:
                    liste = json.load(fichier)
                except json.decoder.JSONDecodeError:
                    liste = []
            liste.append(h)
            with open(chemin, 'w') as fichier:
                json.dump(liste, fichier, indent=4)
                print("Le mot de passe haché est : ", h)
    
    else:
        print("Choix invalide. Veuillez choisir 'C' pour créer un mot de passe ou 'G' pour en générer un aléatoirement.")
        creer_ou_generer_mot_de_passe()

creer_ou_generer_mot_de_passe()




        





    






