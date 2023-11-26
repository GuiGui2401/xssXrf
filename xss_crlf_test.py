import argparse
import requests
import re
import openpyxl
from fpdf import FPDF

def check_xss(url, input):
    response = requests.get(url, params={"input": input})
    if re.search(r"<script>", response.text):
        return True
    return False

def check_crlf(url, input):
    response = requests.get(url, params={"input": input})
    if re.search(r"\r\n", response.text):
        return True
    return False

def generate_excel_report(results):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Rapport de vulnérabilités XSS et CRLF"
    sheet.append(["URL", "Faille", "Description"])
    for result in results:
        sheet.append(result)
    wb.save("rapport_vulnerabilites.xlsx")

def generate_pdf_report(results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write("Rapport de vulnérabilités XSS et CRLF")
    pdf.ln()
    for result in results:
        pdf.write("URL: " + result[0])
        pdf.ln()
        pdf.write("Faille: " + result[1])
        pdf.ln()
        pdf.write("Description: " + result[2])
        pdf.ln()
    pdf.output("rapport_vulnerabilites.pdf")

def main():
    parser = argparse.ArgumentParser(description="Test de failles XSS et CRLF")
    parser.add_argument("url", help="URL à tester")
    parser.add_argument("input_file", help="Fichier texte contenant les entrées à tester (une par ligne)")
    parser.add_argument("-t", "--report-type", choices=["excel", "pdf"], default="excel", help="Type de rapport (excel ou pdf)")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        inputs = file.readlines()

    url = args.url
    results = []

    for input in inputs:
        input = input.strip()  # Supprimer les espaces et les sauts de ligne supplémentaires
        if check_xss(url, input):
            results.append([url, "XSS", "Faille XSS trouvée pour l'entrée : " + input])
        if check_crlf(url, input):
            results.append([url, "CRLF", "Faille CRLF trouvée pour l'entrée : " + input])

    if args.report_type == "excel":
        generate_excel_report(results)
    elif args.report_type == "pdf":
        generate_pdf_report(results)

if __name__ == "__main__":
    main()
