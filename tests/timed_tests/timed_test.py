from pdfminer.high_level import extract_text
import glob
from Algorithm.boyer_moore import search
import time
import csv

SEARCH_TERM = "ABOUT"


def main():
    pdfs = []
    header = ["Number of words", "Time in Nanoseconds"]

    try:
        f = open("timed_tests.csv", "w")

        writer = csv.writer(f)
        writer.writerow(header)

        files = glob.glob("test_pdfs/*.pdf")

        for file_name in files:
            pdfs.append([file_name, extract_text(file_name).upper()])

        for file in pdfs:
            t0 = time.time_ns()

            search(file[1], SEARCH_TERM)

            t1 = time.time_ns()

            writer.writerow([file[0].strip("test_pdfs\\ .pdf"), t1-t0])

        f.close()

    except EOFError:
        exit(0)


if __name__ == "__main__":
    main()
