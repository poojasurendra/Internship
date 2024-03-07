#!/usr/bin/env python
# coding: utf-8

# In[20]:


def replace_characters(text):
    replacements = {' ': ':', ',': ':', '.': ':'}
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

sample_text1 = 'Python Exercises, PHP exercises.'
result = replace_characters(sample_text)
print(result)


# In[12]:


import pandas as pd
import re
data = {'SUMMARY':['hello, world!', 'XXXXX test', '123four, five:; six...']}

df1 = pd.DataFrame(data)
df1['SUMMARY'] = df1['SUMMARY'].apply(lambda x: re.sub(r'\W+', ' ', x))
print (df1)


# In[18]:


def find_long_words(text):
    
    pattern = re.compile(r'\b\w{4,}\b')
    
    long_words = pattern.findall(text)
    return long_words

input_text = "words that are at least 4 characters long in a string"
result = find_long_words(input_text)
print(result)


# In[19]:


def find_short_words(text):
    
    pattern = re.compile(r'\b\w{3,5}\b')
   
    short_words = pattern.findall(text)
    return short_words

input_text = "find all three, four, and five character words in a string"
result = find_short_words(input_text)
print(result)


# In[23]:


def remove_parantheses(strings):
    pattern = re.compile(r'\((.*/?)\)')
    modified_strings = []
    for string in strings:
        modified_string= pattern.sub(' ',string)
        modified_strings.append(modified_string.strip())
    return modified_strings
sample_text2 = ["example (.com)", "hr@fliprobo (.com)","github.com","Hello(Data Science World)","Data (Scientist)"]
output = remove_parantheses(sample_text)
for string in output:
        print(string)
                     
                        


# In[27]:


def split_uppercase(text):
    pattern = r'[A-Z][a-z]*'
    result = re.findall(pattern, text)
    return result
sample_text3 = "ImportanceOfRegularExpressionsInPython"
output = split_uppercase(sample_text3)
print(output)




# In[28]:


def insert_space_before_numbered_words(text):

    pattern = r'(?<=\d)(?=[A-Za-z])'
    result = re.sub(pattern, ' ', text)
    
    return result
sample_text4 = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_space_before_numbered_words(sample_text4)
print(output)


# In[29]:


def insert_space_before_capital_or_number_words(text):
    pattern = r'(?<=\b)(?=[A-Z0-9])'
    result = re.sub(pattern, ' ', text)
    return result
sample_text5 = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_space_before_capital_or_number_words(sample_text5)
print(output)


# In[30]:


url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)
df['first_five_letters'] = df['Country'].str[:6]
print(df.head())


# In[39]:


def remove_leading_zeros(ip_address):
    pattern = r'\b0+(\d+)'
    result = re.sub(pattern, r'\1', ip_address)
    return result
sample_ips = ["102.188.051.091", "001.902.873.004", "010.020.030.040"]

for ip in sample_ips:
    print(f'IP without leading zeros: {remove_leading_zeros(ip)}')


# In[41]:


def search_words(text, words):
    found_words = []
    for word in words:
        if word in text:
            found_words.append(word)
    return found_words


sample_text6 = 'The quick brown fox jumps over the lazy dog.'

searched_words = ['fox', 'dog', 'horse']

found_words = search_words(sample_text6, searched_words)

print("Found words:", found_words)


# In[43]:


from datetime import datetime

def convert_date_format(date_string):
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%d-%m-%Y')

    return formatted_date

date_string = '2001-11-15'

converted_date = convert_date_format(date_string)

print("Original date (yyyy-mm-dd):", date_string)
print("Converted date (dd-mm-yyyy):", converted_date)


# In[45]:


def find_decimal_numbers(text):
    
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    decimal_numbers = pattern.findall(text)

    return decimal_numbers

sample_text7 = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

output = find_decimal_numbers(sample_text7)
print( output)


# In[46]:


def extract_maximum_numeric_value(text):
    
    pattern = re.compile(r'\b\d+\b')
    numeric_values = [int(match) for match in pattern.findall(text)]
    if numeric_values:
        max_value = max(numeric_values)
        return max_value
    else:
        return None

sample_text8 = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
output = extract_maximum_numeric_value(sample_text8)
print(output)


# In[47]:


def insert_spaces(text):
    
    modified_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return modified_text
sample_text9 = "RegularExpressionIsAnImportantTopicInPython"
output = insert_spaces(sample_text9)
print(output)


# In[48]:


def remove_continuous_duplicates(sentence):
    
    modified_sentence = re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', sentence)
    return modified_sentence

sample_text10 = "Hello hello world world"
output = remove_continuous_duplicates(sample_text10)
print(output)


# In[49]:


def extract_hashtags(text):
    
    pattern = r'#\w+'
    hashtags = re.findall(pattern, text)
    
    return hashtags

sample_text11 = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same
has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

output = extract_hashtags(sample_text11)
print( output)


# In[ ]:




