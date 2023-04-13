#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
from datetime import datetime

def name_validation(name):
    if(re.fullmatch('[A-Za-z]{2,25}([A-Za-z]{2,25})?',name)):
        return True
    else:
        print("\n***Enter a valid name***")
        return False
def age_validation(age):
    if(int(age)>=10 and int(age)<=99):
        return True
    else:
        print("\n***Enter a valid age***")
        return False
def mail_validation(email):
    
    if(re.fullmatch(r'[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]+',email)):
        return True
    else:
        print("\n***Enter a valid mail id***")
        return False
def phone_number_validation(phone_num):
    if(re.fullmatch('[0-9]+',phone_num) and len(phone_num)==10):
        return True
    else:
        print("\n***Invalid phone number***")
        return False
def gender_validation(gender):
    if(re.fullmatch(r'[M|F]',gender.upper())):
        return True
    else:
        print("\n***Enter a valid gender***")
        return False
def password_validation(password):
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$",password):
        return True
    else:
        print("\n***The password length should be 8 and must contain one upper and one lower case***")
        return False
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string,'%Y-%m-%d')
        return True
    except ValueError:
        print("\n***Enter the date 'YYYY-MM-DD' this format!***")
        return False
# password_validation("U17cs2011@")
# print(name_validation("john"))
# print(age_validation("62"))
# print(mail_validation("antony@gmail.com"))
# print(gender_validation('d'))
# print(phone_number_validation("8189880516"))
# print(is_valid_date("1999-06-204"))

