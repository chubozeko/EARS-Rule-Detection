# EARS Rule Detection
This project involves identifying the basic structure of EARS rules used in expressing requirements. Once a text file is loaded, the scripts perform some language processing on each sentence/statement and checks if they follow the EARS requirement structures, such as:
- Ubiquitous requirement
- Event-driven requirement
- State-driven requirement
- Unwanted behaviour requirement
- Optional feature requirement
- Complex requirement

## Running the Scripts
Each of Python scripts can be run individually when the dataset text file (`.txt`) is in the same directory.
```python ears_ubiquitous.py```
```python ears_event_driven.py```
```python ears_state_driven.py```


## Tools Used
This project was developed in Python, using the following libraries:
- NLTK (https://www.nltk.org/api/nltk.html)
- NumPy (https://numpy.org/)
- Textstat (https://pypi.org/project/textstat/)

Further requirements found in `requirements.txt`.

## References
- Template Conformance (https://github.com/armsp/template-conformance)
