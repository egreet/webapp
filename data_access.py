import sqlite3
from datetime import datetime
import random
import sys

def insert_link(empl_for):
    url='localhost:3000/'+empl_for+'/'+str(random.getrandbits(128))

def create_user(Emp_ID,Emp_Name ,Emp_Email,Emp_DOB ,Team_Name,Emp_Designation,Emp_N1_Manager="",Emp_N2_Manager="",Emp_DU_Head=""):

    Team_Name=Team_Name.upper()
    Emp_Designation=Emp_Designation.upper()
    Emp_Name=Emp_Name.upper()
    sql='insert into Employee_Data values({},\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');'.format(Emp_ID,Emp_Name ,Emp_Email,Emp_DOB ,Team_Name,Emp_Designation,Emp_N1_Manager,Emp_N2_Manager,Emp_DU_Head)
    try:
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:
            print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            print(datetime.today().date())
            print(sql)
            cur=conn.cursor()
            cur.execute(sql)
            conn.commit()

    except:
        print('Error',sys.exc_info()[0])
        return 0
# conn.close()

def select_user(Emp_ID):


    sql='select * from Employee_Data where emp_id='+str(Emp_ID)+';'
    try:
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:
            # print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            # print(datetime.today().date())
            print(sql)
            cur=conn.cursor()
            x=cur.execute(sql)
            for i in x:
                return i
            conn.commit()

    except:
        print('Error',sys.exc_info()[0])
        return 0

# create_user(1,'abc','abc','20-09-2018','dsf','dsad',1,2,3)

def fetch_name(emp_id):
    sql='select emp_name from Employee_Data where emp_id='+str(emp_id)+';'
    try:
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:
            # print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            # print(datetime.today().date())
            print(sql)
            cur=conn.cursor()
            x=cur.execute(sql)
            for i in x:
                return i[0]
            conn.commit()

    except:
        print('Error',sys.exc_info()[0])
        return 0


def save_message(for_id,name,from_id,msg):
    mg=list(msg)

    while '\'' in mg:
        mg[mg.index('\'')]='\'\''
    msg="".join(mg)
    sql='insert into Messages values({},\'{}\',{},\'\',\'{}\');'.format(from_id,name ,for_id,msg)
    try:
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:

            print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            print(datetime.today().date())
            print(sql)
            cur=conn.cursor()
            cur.execute(sql)
            conn.commit()
    except:
        print('Error',sys.exc_info()[0])
        return 0


def fetch_messages(emp_id):
    sql='select sender_name,message from messages where receiver_emp_id='+str(emp_id)+';'
    try:
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:
            # print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            # print(datetime.today().date())
            print(sql)
            cur=conn.cursor()
            x=cur.execute(sql)
            lis=[]
            for i in x:
                lis.append(i)
            return lis
            conn.commit()

    except:
        print('Error',sys.exc_info()[0])
        return 0
