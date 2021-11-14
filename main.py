import pdfplumber
import sys
import glob
from Algorithm.boyer_moore import search


def sort_compare(rank):
    return rank[1]


def main():
    pdfs = []
    ranks = []
    count = 0

    try:
        files = glob.glob("pdfs/*.pdf")

        for file_name in files:
            pdfs.append([file_name, pdfplumber.open(file_name)])

        while True:
            val = str(input("Search: "))

            for file in pdfs:
                for page in file[1].pages:
                    words = val.split(" ")

                    for word in words:
                        count += search(page.extract_text().upper(), word.upper())

                ranks.append([file[0], count])
                count = 0

                ranks.sort(key=sort_compare, reverse=True)

            i = 1
            for rank in ranks:
                print(f"     Rank {i}  File: {rank[0]}  Score: {rank[1]}")
                i += 1

            ranks.clear()

    except EOFError:
        exit(0)


if __name__ == "__main__":
    main()
