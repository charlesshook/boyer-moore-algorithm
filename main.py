import pdfplumber
import sys


def main():
    pdf = None

    if len(sys.argv) > 1:
        pdf = pdfplumber.open(sys.argv[1])

    for page in pdf.pages:
        print(page.extract_text())


if __name__ == "__main__":
    main()
