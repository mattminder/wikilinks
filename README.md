# wikilinks
## Authors
Marc Glettig - Matthias Minder - Yves Rychener - Charles Trotin

## Description
This code is for the project in the course Network Tour of Data Science at EPFL. 
Using text similarity, we construct networks of Wikipedia articles and compare them to the Wikipedia Hyperlink Network. 
After assessing the different netrwork creation methods, we seek to recommend new possible hyperlinks. For more detailed description refer to the annotated jupyter notebook and the project report.

## Requirements
### Data
The root folder should contain a folder "data", which itself contains the SNAP Wikipedia dataset. <br>
(https://snap.stanford.edu/data/wikispeedia.html)
Before running the notebook, a folder "articles" should be created in the "data" folder. Then, the scripts should be run (first wikipedia_text_extract, then wikipedia_missed_extract) to fetch the article texts.
### Packages
The following (non standard python) Packages are required:
- numpy
- scipy
- matplotlib
- pandas
- sklearn
- wikipedia
- gensim
- nltk

## Instructions
- Run scripts wikipedia_text_extract, then wikipedia_missed_extract
- Run Notebook project.ipynb
