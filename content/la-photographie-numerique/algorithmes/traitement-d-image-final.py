#! /usr/bin/env python3

import os
import mimetypes
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))

################################################################################
# NE RIEN MODIFIER AVANT CETTE LIGNE
################################################################################

def action_niveaux_de_gris(nom):
    """Convertit l'image en niveaux de gris."""
    source = Image.open(nom).convert('RGB')
    largeur = source.width
    hauteur = source.height
    dest  = Image.new('RGB', (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            rouge, vert, bleu = source.getpixel((x, y))
            moyenne = (rouge + vert + bleu)//3
            dest.putpixel((x, y), (moyenne, moyenne, moyenne))

    dest.save("gris.png")

def action_symetrie_gauchedroite(nom):
    """Effectue la symérie gauche-droite"""
    source = Image.open(nom).convert('RGB')
    largeur = source.width
    hauteur = source.height
    dest  = Image.new('RGB', (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            rouge, vert, bleu = source.getpixel((x, y))
            dest.putpixel((largeur-x-1, y), (rouge, vert, bleu))

    dest.save("gauchedroite.png")

def action_symetrie_hautbas(nom):
    """Effectue la symérie haut-bas"""
    source = Image.open(nom).convert('RGB')
    largeur = source.width
    hauteur = source.height
    dest  = Image.new('RGB', (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            rouge, vert, bleu = source.getpixel((x, y))
            dest.putpixel((x, hauteur-y-1), (rouge, vert, bleu))

    dest.save("hautbas.png")

def action_eclaircir(nom):
    """Éclaircit l'image"""
    source = Image.open(nom).convert('RGB')
    largeur = source.width
    hauteur = source.height
    dest  = Image.new('RGB', (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            rouge, vert, bleu = source.getpixel((x, y))
            dest.putpixel((x, y), (
                rouge//2+128,
                vert//2+128,
                bleu//2+128,
                ))

    dest.save("eclaircie.png")

def action_assombrir(nom):
    """Assombrit l'image"""
    source = Image.open(nom).convert('RGB')
    largeur = source.width
    hauteur = source.height
    dest  = Image.new('RGB', (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            rouge, vert, bleu = source.getpixel((x, y))
            dest.putpixel((x, y), (
                rouge//2,
                vert//2,
                bleu//2,
                ))

    dest.save("assombrie.png")

def action_rotation90(nom):
    """Pivoter la photo de 90° vers la gauche"""
    source = Image.open(nom).convert('RGB')
    largeur = source.width
    hauteur = source.height
    dest  = Image.new('RGB', (hauteur, largeur))

    for x in range(largeur):
        for y in range(hauteur):
            rouge, vert, bleu = source.getpixel((x, y))
            dest.putpixel((y, largeur-x-1), (rouge, vert, bleu))

    dest.save("rotation90.png")

def action_inverse(nom):
    """Inverser les couleurs"""
    source = Image.open(nom).convert('RGB')
    largeur = source.width
    hauteur = source.height
    dest  = Image.new('RGB', (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            rouge, vert, bleu = source.getpixel((x, y))
            dest.putpixel((x, y), (
                255-rouge,
                255-vert,
                255-bleu,
                ))

    dest.save("inverse.png")

################################################################################
# NE RIEN MODIFIER APRÈS CETTE LIGNE
################################################################################

ACTIONS = [
    action_niveaux_de_gris,
    action_symetrie_gauchedroite,
    action_symetrie_hautbas,
    action_eclaircir,
    action_assombrir,
    action_rotation90,
    action_inverse,
    ]

def choix_image():
    print("#"*80)
    print("# Choix de l'image #")
    images = [name for name in sorted(os.listdir()) if str(mimetypes.guess_type(name)[0]).startswith("image")]
    for compteur in range(len(images)):
        print("[{}] {}".format(compteur, images[compteur]))
    while True:
        choix = input("Quelle image traiter ? ")
        try:
            if 0 <= int(choix) < len(images):
                print()
                return images[int(choix)]
        except ValueError:
            pass
        print("Veuillez choisir un nombre entre 0 et {}.".format(len(images)-1))

def docstring(fonction):
    if not fonction.__doc__.strip():
        raise Exception("La fonction '{}' n'a pas de docstring.".format(fonction.__name__))
    else:
        return fonction.__doc__.strip().split("\n")[0]


def choix_action():
    print("#"*80)
    print("# Choix de l'action #")
    for compteur in range(len(ACTIONS)):
        print("[{}] {}".format(compteur, docstring(ACTIONS[compteur])))
    while True:
        choix = input("Quelle action effectuer ? ")
        try:
            if 0 <= int(choix) < len(ACTIONS):
                print()
                return ACTIONS[int(choix)]
        except ValueError:
            pass
        print("Veuillez choisir un nombre entre 0 et {}.".format(len(ACTIONS)-1))

source = choix_image()
action = choix_action()

action(source)
