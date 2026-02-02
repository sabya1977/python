import re
# demonstrate group and escape characte pattern
def match_phone(srch_string):
    pattern = re.compile(r'(\(\d{5}\))\s(\d{3})\s(\d{2})') # escape character to accept () format
    mo = pattern.search(srch_string)
    excp_str = 'Hi Sabyasachi, your mobile number is not valid'
    fnd_str = 'Hi Sabyasachi your phone number is:  '
    try:
        text = mo.group()
        fnd_str += text
    except AttributeError:
        # print (excp_str)
        return excp_str
    else:
        # print (fnd_str)
        return fnd_str
    
def match_altg(srch_string):
    pattern=re.compile(r'\((^6|7|8|9)\d{4}\)\s\d{3}\s\d{2}') # alternate group by pipe to validate indian number
    mo = pattern.search(srch_string)
    excp_str = 'Hi Sabyasachi, your mobile number is not a valid Indian number!'
    fnd_str = 'Hi Sabyasachi your phone number is:  '
    try:
        text = mo.group()
        fnd_str += text
    except AttributeError: # error if no match found
        return excp_str    # return error message if no match found
    else:
        return fnd_str     # return phone number if match found

# findall function in python regexp library
def match_all (srch_string):
    pattern = re.compile(r'\d{5}\s\d{3}\s\d{2}')
    list_of_numbers = pattern.findall(srch_string)
    return list_of_numbers

# find all functions for grouped items in python regexp library
def match_all_grp(srch_string):
    pattern = re.compile(r'(\d{5})\s(\d{3})\s(\d{2})')
    list_of_numbers = pattern.findall(srch_string)
    return list_of_numbers

# Character class
def count_vowels(srch_string):
    pattern = re.compile(r'[aeiouAEIOU]')
    list_vowels = pattern.findall(srch_string)
    return len(list_vowels)

def count_consonants(srch_string):
    pattern = re.compile(r'[^aeiouAEIOU]')
    list_cons = pattern.findall(srch_string)
    return len(list_cons)

# Shorthand of character class





