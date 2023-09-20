#!/usr/bin/env python3

"""Un serveur web qui propose une calculatrice en ligne."""

#  pylint: disable=line-too-long

import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

PORT = 8000

SELECTED = {
    True: "selected",
    False: "",
}


def calcule(nombre1, nombre2, operation):
    """Effectue le calcul donné en argument."""
    if operation is None:
        return None

    if operation == "+":
        return nombre1 + nombre2

    return "À compléter…"


class Server(http.server.SimpleHTTPRequestHandler):
    """Un petit serveur web qui propose la calculatrice en ligne."""

    def extrait_parametres(self):
        """Extrait les paramètres de l'URL : les deux opérandes, et l'opération."""
        parametres = parse_qs(urlparse(self.path).query)

        if parametres.get("nombre1", None):
            nombre1 = parametres["nombre1"][0]
        else:
            nombre1 = "0"

        if parametres.get("nombre2", None):
            nombre2 = parametres["nombre2"][0]
        else:
            nombre2 = "0"

        if parametres.get("operation", None):
            operation = parametres["operation"][0]
        else:
            operation = None

        return int(nombre1), int(nombre2), operation

    def do_GET(self):
        self.protocol_version = "HTTP/1.1"
        self.send_response(200, "OK")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        nombre1, nombre2, operation = self.extrait_parametres()
        self.wfile.write(
            bytes(
                """
            <!doctype html>
            <html lang="fr">
                <head>
                    <title>Calculatrice</title>
                    <meta charset="utf-8">
                </head>
                <body>
                    <h1>Calculatrice</h1>
                    <em>Quelle opération souhaitez vous effectuer ?</em>
                     <form action="/" method="get">
                        <input type="number" value="{nombre1}" name="nombre1" autofocus="autofocus">
                        <select name="operation">
                            <option value="+" {selected[+]}>+</option>
                            <option value="-" {selected[-]}>-</option>
                            <option value="*" {selected[*]}>×</option>
                            <option value="/" {selected[/]}>÷</option>
                        </select>
                        <input type="number" value="{nombre2}" name="nombre2">
                        =
                        <input type="text" value="{resultat}" readonly>
                        <input type="submit" value="Calculer">
                    </form>
                </body>
            </html>
        """.format(
                    nombre1=nombre1,
                    nombre2=nombre2,
                    selected={
                        opération: SELECTED[opération == operation]
                        for opération in ("+", "-", "*", "/")
                    },
                    resultat=calcule(nombre1, nombre2, operation),
                ),
                "UTF-8",
            )
        )


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Server) as httpd:
        print(
            f"Dans un navigateur web, allez à la page http://localhost:{PORT} pour voir le site web."
        )
        httpd.serve_forever()
