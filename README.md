# boyer-moore-algorithm
This program implements the boyer moore algorithm. You can place pdfs in the pdfs/ folder. Then you can run the program 
and type a message to search. The program will then rank the pdf files based on the number of matches to words in your
message. More matches means that the pdf should be shown higher in your search results.

### Tools
* Pycharm

### Installing Dependencies
```
pip3 install -r .\requirements.txt
```

### Running The Project
The project is pre-loaded with some pdf files loaded with randomly generated text.
You can add your own pdf files to the pdfs/ folder. Once you are ready run:
```
python3 main.py
```

### Running The Tests

#### Unit Tests
```
python3 -m unittest discover tests
```

#### Timed Tests
```
cd tests/timed_tests
python3 timed_test.py
```