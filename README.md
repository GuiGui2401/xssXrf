# Test de failles XSS et CRLF

## Description
Ce script Python teste les failles XSS et CRLF sur une liste d'URLs avec différentes entrées. Il génère des rapports au format Excel ou PDF en fonction des résultats.

## Prérequis

- Python 3.x installé
- Bibliothèques Python nécessaires : requests, re, openpyxl, fpdf

## Utilisation

```
python xss_crlf_test.py -t [excel|pdf] -f [chemin/vers/fichier.txt]
```

- **-t** : Type de rapport à générer (excel ou pdf)
- **-f** : Chemin vers le fichier texte contenant les requêtes SQL

Exemple d'utilisation

```
python xss_crlf_test.py -t pdf -f input.txt
```

## Rapports

- **rapport_vulnerabilites.xlsx** : Rapport au format Excel contenant les résultats des tests.
- **rapport_vulnerabilites.pdf** : Rapport au format PDF contenant les résultats des tests.

## Remarques

Vous pouvez remplacer les requêtes XSS et CRLF du fichier texte avec celles que vous souhaitez tester.

## Auteur
GuiGui2401

## Licence
Ce projet est sous licence GNU. Consultez le fichier LICENSE pour plus de détails.