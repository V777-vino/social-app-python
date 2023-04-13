#!/usr/bin/env python
# coding: utf-8

# In[4]:


from mysql.connector import MySQLConnection, Error
import os
import pymysql
import getpass
from tabulate import tabulate

# import pandas as pd

host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

conn = pymysql.connect(
host= host,
port = int(3306),
user = "root",
password = "U17cs2011@",
db ="social_app",
charset ='utf8mb4')

def show_user_detail_by_id(user_id):
    query = "select *from users where user_id=%s"
    data = (user_id)
    try:
        cursor = conn.cursor()
        cursor.execute(query,data)
        row = cursor.fetchall()
        
        print(tabulate(row,headers=['User id','First name','Last name','Mail id','Phone number','Gender','DOB','Password'])) 
    except Error as e:
        print(e)
    finally:
        
        cursor.close()
def insert_user_details(fname,lname,mail_id,phone_number,gender,dob,pword):
    query = "insert into users(fname,lname,mail_id,phone_number,gender,dob,pword) values(%s,%s,%s,%s,%s,%s,%s)"
    args = (fname,lname,mail_id,phone_number,gender,dob,pword)
    try:
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
        print("\n***User account is created!***")
    except Error as error:
        print(error)
    finally:
        cursor.close()
def update_password(user_id,password):
    query="update users set pword=%s where user_id=%s"
    data = (password,user_id)
    try:
        cursor = conn.cursor()
        cursor.execute(query,data)
        conn.commit()
        print("\n***"+password," password is updated!***")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        
def update_phone_number(user_id,phone_number):
    query = "update users set phone_number =%s where user_id =%s"
    data = (phone_number,user_id)
    try:
        cursor = conn.cursor()
        cursor.execute(query,data)
        conn.commit()
        print("\n***"+phone_number," phone number is updated!***")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        
def update_mail_id(user_id, mail_id):
    query = "update users set mail_id =%s where user_id = %s; "
    data = (mail_id, user_id)
    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        print("\n***"+mail_id," mail id is updated!***")
    except Error as error:
        print(error)
    finally:
        cursor.close()
        
        
def delete_user(user_id):
    query = "delete from users where user_id =%s"
    try:
        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        count = cursor.rowcount
        conn.commit()
        if(count ==1):
            print("\n***user id "+str(user_id)+" is deleted!***")
        else:
            print("\n***user_id "+str(user_id)+" not found***")
    except Error as error:
        print(error)
    finally:
        cursor.close()
        
def search_user_by_name(fname):
    query = "select fname from users where fname like '{}%'".format(fname)
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(tabulate(rows,headers=['Name']))
    except Error as e:
        print(e)
    finally:
        cursor.close()

def post_message(user_id,message):
    query = "insert into posts(user_id,message) values (%s,%s)"
    data = (user_id,message)
    try:
        cursor = conn.cursor()
        cursor.execute(query,data)
        conn.commit()
        print("\n***Your message posted***")
    except Error as e:
        print(e)
    finally:
        cursor.close()
def your_posts(user_id):
    query = "select * from posts where user_id =%s"
    data = (user_id)
    try:
        cursor = conn.cursor()
        cursor.execute(query,data)
        row = cursor.fetchall()
        
        print(tabulate(row,headers=['post id','user id','message','posted date'])) 

    except Error as e:
        print(e)
    finally:
        cursor.close()
        
def delete_post(post_id):
    query = 'delete from posts where post_id=%s'
    data = post_id
    try:
        cursor = conn.cursor()
        cursor.execute(query,data)
        count = cursor.rowcount
        conn.commit()
        if(count == 1):
            print("post id:"+str(post_id)+" is deleted!")
        else:
            print("\n***This post not found***")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        
def login(mail_id,password):
    query = "select mail_id from users where mail_id = %s and pword =%s"
    data = (mail_id,password)
    try:
        cursor = conn.cursor()
        cursor.execute(query,data)
        field1 = cursor.fetchone()
        if field1 is not None:
            if mail_id == str(field1[0]):
                return True
        else:
            return False
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
def see_all_posts():
    query = "select u.user_id,u.fname,p.message,p.posted_date from users as u inner join posts as p on u.user_id = p.user_id"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        
        print(tabulate(rows,headers=['user id','first name','message','posted date']))

    except Error as e:
        print(e)
    finally:
        cursor.close()
def is_registered(mail):
    query = "select mail_id from users where mail_id =%s"
    data = (mail)
    try:
        cursor = conn.cursor()
        cursor.execute(query,data)
        row = cursor.fetchone()
        
        if row is None:
            return True
        else:
            print("\n***This mail id already registered!***")
            False
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        
# print(is_registered("a@gmail.com"))        
    
# see_all_posts()
        
# print(login("jaga@gmail.com","Jaga@1234"))
        
# delete_user(12)
        
# update_mail_id(8,"ravalika@gmail.com")
        
# insert_user_details("jagadesh","kongara","jaga@gmail.com",8189770589,"M","2000-07-16","U17cs99")
    
# query_with_fetchall()

# update_phone_number(8,8189880599)

# update_password(14,"Jaga@1234")

# show_user_detail_by_id(8)

# search_user_by_name("z")

# post_message(2,"you have to fight for your life")

# your_posts(1)

# delete_post(2)


# In[1]:




