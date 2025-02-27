import pathlib
import fileinput


def remplacer_lettres_par_x(chemin_fichier, lettres_a_remplacer):
	try:
		# Traitement du fichier avec un backup
		with fileinput.FileInput(chemin_fichier, inplace=True, backup=".bak") as fichier:
			for ligne in fichier:
				for lettre in lettres_a_remplacer:
					ligne = ligne.replace(lettre, "x")  # Remplace les lettres spécifiées (les voyelles dans mon cas)
				print(ligne, end='')  # Réécrit dans le fichier et empeche les /n a la fin de la ligne
		print(f"Remplacement effectué avec succès dans '{chemin_fichier}'.")
	except FileNotFoundError:
		print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
	except Exception as e:
		print(f"Une erreur inattendue est survenue : {e}")


# Obtenir le chemin du fichier root a la racine de l'exercice
root_path = pathlib.Path(__file__).parent.resolve()
chemin_exemple = root_path / "test.txt"

# appel de la fonction pour changer les voyelles de mon fichier par des 'x'
remplacer_lettres_par_x(chemin_exemple, lettres_a_remplacer=["a", "e", "i", "o", "u"])
