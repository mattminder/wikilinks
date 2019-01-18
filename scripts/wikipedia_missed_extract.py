import wikipedia
import string
import urllib
import numpy as np
import pandas as pd
import os.path
import requests

def extract_text(page_name):
    page = wikipedia.page(page_name)
    art_text = page.content
    art_text1 = art_text.replace("=","")
    art_text2 = art_text1.replace("edit","")
    art_text3 = art_text2.replace("/","")
    art_text4 = art_text3.replace("\n","")
    art_textf = art_text4.replace("/","")
    return art_textf

##----------------------------------------------------------------------------------------

# Definitions and loading data
DATA_FOLDER = '../data/'

missed = pd.read_csv(DATA_FOLDER + 'missed.csv')


# get all wikipedia texts and save them to text, don't do files that already exist
i = 1
for ind,row in missed.iterrows():
    if (os.path.exists(DATA_FOLDER + 'articles/' + row.Original + '.txt')):
        # print removed for easier analysis of errors
        # print('Iteration ' + str(i) + ' of ' + str(len(lc_index)) + '; File already Exists!')
        pass
    else:
        try:
            print('Iteration ' + str(i))
            text = extract_text(urllib.parse.unquote(row[1]).replace('_',' '))
            file_name = DATA_FOLDER + 'articles/' + row.Original + '.txt'
            with open(file_name, "w", encoding='utf-8') as text_file:
                text_file.write(text)
        except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.WikipediaException,requests.exceptions.ChunkedEncodingError) as err:
            with open(DATA_FOLDER + 'error_sites_2.txt', "a", encoding='utf-8') as text_file:
                text_file.write('Page '+ urllib.parse.unquote(row.Original) + ' not found! \n')
            print('Page '+ urllib.parse.unquote(row[1]) + ' not found!') 
            print(err)  
    i = i+1