import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []                          # empty list for storage
    source_code = requests.get(url).text    # get url contents in text
    soup = BeautifulSoup(source_code)       #
    for post_text in soup.findAll('a', {'class': 'hdrlnk'}):    # look for hdrlnk class in links
        content = post_text.string
        words = content.lower().split()      # convert all text to lower case and split by space
        for each_word in words:
            # print(each_word)
            word_list.append(each_word)         # store words in empty word_list
    clean_up_list(word_list)                    # clean up unwanted characters


def clean_up_list(word_list):
    clean_word_list = []                           # empty list for storage
    for word in word_list:
        symbols = "!@#$%^&*♥(){}\":?_-<>,.[]▓௵=|\/~`'"   # all symbols to be replaced
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")         # remove symbols
        if len(word) > 0:                               # append word to clean_word_list if len > 0
            # print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)                  # pass clean_word_list to create_dictionary

def create_dictionary(clean_word_list):
    word_count = {}                             # empty dict for storage
    for word in clean_word_list:                # every word in the clean_word_list
        if word in word_count:
            word_count[word] +=1                    # if word is already in the list, add 1 to it
        else:
            word_count[word] = 1                    # if not, counts it
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):       # 1 is sorted by value, 0 for key
        print(key, value)

start('http://sfbay.craigslist.org/search/sss?sort=rel&query=iphone')