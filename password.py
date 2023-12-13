import hashlib
import json

chemin = 'password.json'

def verification_securite(choix_du_mot_de_passe):
    return (
        len(choix_du_mot_de_passe) >= 8 and
        any(c.isupper() for c in choix_du_mot_de_passe) and
        any(c.islower() for c in choix_du_mot_de_passe) and
        any(c.isdigit() for c in choix_du_mot_de_passe) and
        any(not c.isalnum() for c in choix_du_mot_de_passe)
    )

mot_de_passe_valide = False

while not mot_de_passe_valide:
    choix_du_mot_de_passe = input("Choisir un mot de passe qui contient au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial : ")
    
    if verification_securite(choix_du_mot_de_passe):
        mot_de_passe_valide = True
        print("Le mot de passe est sécurisé.")
        
        h = hashlib.sha256(choix_du_mot_de_passe.encode()).hexdigest()
        
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


    
    
            



        





    






