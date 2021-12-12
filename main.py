from pdfminer.high_level import extract_text
import glob
from Algorithm.boyer_moore import search
import time


def sort_compare(rank):
    return rank[1]


def main():
    pdfs = []
    ranks = []
    count = 0

    try:
        files = glob.glob("pdfs/*.pdf")

        for file_name in files:
            pdfs.append([file_name, extract_text(file_name).upper()])

        while True:
            val = str(input("Search: "))
            words = val.split(" ")

            t0 = time.time()

            for file in pdfs:
                for word in words:
                    count += search(file[1], word.upper())

                ranks.append([file[0], count])
                count = 0

                ranks.sort(key=sort_compare, reverse=True)

            i = 1

            t1 = time.time()

            print(f"Rank completed in {t1-t0} seconds")
            for rank in ranks:
                print(f"     Rank {i}  File: {rank[0]}  Score: {rank[1]}")
                i += 1

            ranks.clear()

    except EOFError:
        exit(0)


if __name__ == "__main__":
    main()
