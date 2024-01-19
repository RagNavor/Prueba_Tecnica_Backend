import re
from unicodedata import normalize
from datetime import datetime
import pandas as pd


def items_counter(df:pd)->dict:
    hashtags:int =0
    tags:int =0
    for i in range(len(df)):
        hashtag =re.findall('\#\w{1,}',df.loc[i,'text'])
        hashtags += len(hashtag) 
        tag = re.findall('\@\w{1,}',df.loc[i,'text'] )
        tags += len(tag) 
    return {
        'Post':len(df),
        'Hashtags':hashtags,
        'Tags':tags
        
    }
    
def top_hastags():
    pass

def top_emojis():
    pass

def top_words():
    pass



def normalize(string_a:str)->str:
    string_a = re.sub('á','a',string_a)
    string_a = re.sub('é','e',string_a)
    string_a = re.sub('í','i',string_a)
    string_a = re.sub('ó','o',string_a)
    string_a = re.sub('ú','u',string_a)
    return string_a




    
    