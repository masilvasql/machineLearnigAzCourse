# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:44:30 2019

@author: marce
"""

import pandas as pd
base = pd.read_csv('credit-data.csv')
base.describe()