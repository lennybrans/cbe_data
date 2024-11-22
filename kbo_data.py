"""
This file loads in the different data sets provided from the KBO Database.
It does preliminary transforming, and later, merges all the sets together to 
an useful data set for sampling.
"""
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

filepath = os.getenv('FILEPATH')
print(filepath)