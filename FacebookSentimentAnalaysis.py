# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:10:02 2019

@author: Nikki
"""

import pandas as pd
import nltk
import nltk.sentiment.vader  import SentimentIntensityAnalyzer
n;tk.downloader.download('vader_lexicon')
file='data.file.xslsx'
xl=pd.ExcelFile(file)   #Read from Excel
