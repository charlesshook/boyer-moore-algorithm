# boyer-moore-algorithm
This program implements the boyer moore algorithm. You can place pdfs in the pdfs/ folder. Then you can run the program 
and type a message to search. The program will then rank the pdf files based on the number of matches to words in your
message. More matches means that the pdf should be shown higher in your search results.

### Installing Dependencies
```
pip3 install -r .\requirements.txt
```

### Running The Project
Make sure to put at least one pdf in the pdfs/ folder and then run: 
```
python3 main.py
```

### Running The Tests
```
python3 -m unittest discover tests
```