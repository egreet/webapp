# # from threading import Timer
# # from after import start_scheduling
# #
# #
# # if __name__=="__main__":
# #     Timer(0,start_scheduling).start()
# #
# #
# #
# #
# #
# #
# #
# # # select * from Employee_data where Emp_DOB='1991-04-18';
# # # SELECT * from Employee_data where Team_name='TESCO' and Emp_ID!=690795;
# # #
# # from mailer import get_data
# # x=""
# # y=open('./test/index.html')
# # for i in y:
# #     x=x+i
# #
# # get_data('rohitpatel.se@gmail.com','Party!!!!',x)
# from emoji import emojize
# from flask import Flask
# app=Flask(__name__)
#
# @app.route('/')
# def index():
#     x=emojize(':birthday:',use_aliases=True)
#     return x
#
# if __name__=="__main__":
#     app.run(debug=True,port='3000')

import sqlite3
from generate_url import url_generator
from mailer import create_mail
import sys
from datetime import datetime,timedelta

def before_five(x):
    # Following 3 lines are for testing
    yy,mm,dd=str(x).split('-')
    dat=str(1996)+'-'+mm+'-'+dd
    try:
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:
            print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            sql='select Emp_Id,emp_name,team_name from employee_data where emp_dob= date(\''+dat+'\')'
            print(sql)
            cur=conn.cursor()
            result=cur.execute(sql)
            for i in result:
                print(i)
                sql2='select emp_id,emp_email from employee_data where team_name=\''+i[2]+'\' and emp_id!='+str(i[0])
                print(sql2)
                res=cur.execute(sql2)
                for j in res:
                    x=url_generator(str(i[0]),str(j[0]))
                    create_mail(j[1],'Please send your wishes to'+i[1],x)

            conn.commit()
    except:
        print('Error',sys.exc_info()[0])
        return 0


before_five(datetime.now().date()+timedelta(5))
