#!/usr/bin/env python
"""
Beispiele für die Verwendung des argparse Modules

 * @package   nlsh/argparse
 * @author    Nils Heinold
 * @copyright Nils Heinold © 2022
 * @link      https://github.com/nlsh/nlsh_argparse
 * @version   python 3.9; Lib/argparse.py 3.2
 * @license   LGPL-3.0
"""

# Module importieren
import argparse
from argparse import ArgumentParser

"""
 " argparse Modul initialisieren und Fehler im Aufruf des Programmes abfangen"
 " Dokumentation von argparse unter https://docs.python.org/3.9/library/argparse.html")
"""


def parser():
    # Parser- Objekt mit Beschreibung der Funktion des Programmes erzeugen
    #  mit epilog='wird nach der Beschreibung desProgrammes Text aufgelistet'
    input_parser: ArgumentParser = argparse.ArgumentParser(
        # Beschreibung, wird als erste Zeile der Erläuterung angezeigt
        description='So rufst du mich auf',

        # den originalen Namen der ausführenden Datei ersetzen
        # prog='ersetzt den originalen Namen der aufgerufenen Datei',

        # Schlusssatz
        epilog='Versuchen Sie es bitte erneut.'
    )

    # Definitionen der unbedingt benötigten Parameter in Reihenfolge, ansonsten Fehlerausgabe
    # ohne "-" im String
    input_parser.add_argument('name', type=str, help='Name/ Pfad zur bearbeitenden Datei')
    input_parser.add_argument('zahl', type=int, help="Irgendeine Zahl")

    # Definitionen der obtionalen Parameter
    # mit "-" im String
    input_parser.add_argument('-OptionalString', type=str,  help="Optionale Parameter als String")
    input_parser.add_argument('-OptionalInt', type=int, help="Optionale Parameter als INT")

    # Parameter gemäß argParse Modul zurückgeben, wenn alle Bedingungen erfüllt
    return input_parser.parse_args()


"""
 " Hier geht das Programm los
 " Hauptfunktion, wenn dieses Script direkt aufgerufen wird
"""

if __name__ == "__main__":
    # Kontrolle der Eingabe, ob alle zu übergebenen Parameter korrekt
    # es wird das argparse Modul genutzt
    argParser = parser()

    # Ausgabe des Rückgabewertes
    print(argParser)
