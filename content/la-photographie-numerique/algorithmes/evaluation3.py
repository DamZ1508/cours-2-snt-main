#!/bin/env python3

# Copyright Louis Paternault 2020
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Gènere les images correspondant à tous les algorithmes du TP.

Usage : evaluation3.py [FICHIERS]

Pour chacun des fichiers foo-bar.py, génère des images foo-bar-assombrie.png, foo-bar-gris.png etc. Pour les fichiers qui génèrent des erreurs, produit foo-bar-eclaircie.log avec le log de l'erreur.
"""  # pylint: disable=line-too-long

import contextlib
import difflib
import importlib
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)

ENONCE = os.path.join(os.path.dirname(__file__), "traitement-d-image.py")
IMAGE = os.path.abspath(os.path.join(os.path.dirname(__file__), "gere.jpg"))

ACTIONS = {
    "action_niveaux_de_gris": "gris",
    "action_symetrie_gauchedroite": "gauchedroite",
    "action_eclaircir": "eclaircie",
    "action_assombrir": "assombrie",
    "action_rotation90": "rotation90",
    "action_inverse": "inverse",
}


@contextlib.contextmanager
def chdir(dirname):
    """Change le répertoire courant (et l'ajoute au PYTHONPATH) temporairement."""
    if not dirname:
        dirname = "."
    oldpath = sys.path.copy()
    oldcwd = os.getcwd()
    sys.path.insert(0, dirname)
    os.chdir(dirname)
    yield
    os.chdir(oldcwd)
    sys.path = oldpath


def check_diff(fichier):
    """Affiche le diff du fichier avec l'énoncé, et demande confirmation.

    Utile pour vérifier qu'un élève n'a pas ajouté un
    ``shutil.rmtree("/")`` quelque part.
    """
    with open(ENONCE) as fileobject:
        original = fileobject.readlines()
    with open(fichier, errors="ignore") as fileobject:
        eleve = fileobject.readlines()
    sys.stdout.writelines(
        difflib.unified_diff(original, eleve, fromfile=ENONCE, tofile=fichier)
    )
    while True:
        user = input("Le fichier {fichier} est-il sûr ? [yn] ".format(fichier=fichier))
        if user == "y":
            return True
        if user == "n":
            return False


def run_action(fichier, action):
    """Applique une action d'un fichier.

    Charge le ficher .py, exécute l'action, puis :
    - si l'action a réussi, renomme l'image résultante en FICHIER-ACTION.png ;
    - si l'action a échoué, enregistre le log dans FICHIER-ACTION.log.
    """
    logging.info(
        "Fichier %s : exécution de l'action %s.", os.path.basename(fichier), action
    )
    basename = os.path.basename(fichier)[:-3]
    with chdir(os.path.dirname(fichier)):
        try:
            module = importlib.import_module(basename)
            getattr(module, action)(IMAGE)
        except Exception as error:  # pylint: disable=broad-except
            with open("{}-{}.log".format(basename, ACTIONS[action]), "w") as fileobject:
                fileobject.write(str(error))
                fileobject.write("\n")
            return
        new = "{}-{}.png".format(basename, ACTIONS[action])
        if os.path.exists(new):
            os.remove(new)
        os.rename("{}.png".format(ACTIONS[action]), new)


def run(fichier):
    """Exécute le fichier pour chacune des actions."""
    logging.info("Exécution du fichier %s.", fichier)
    if not fichier.endswith(".py"):
        with open("{}.log".format(fichier), "w") as fileobject:
            fileobject.write("Le nom du fichier doit se terminer par .py.\n")
        return
    if not check_diff(fichier):
        return
    for action in sorted(ACTIONS):
        run_action(fichier, action)


def main():
    """Fonction principale."""
    for fichier in sys.argv[1:]:
        run(fichier)


if __name__ == "__main__":
    main()
