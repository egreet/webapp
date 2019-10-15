import sqlite3
import schedule
import sys
import time
from threading import Timer
from datetime import datetime, timedelta
from generate_url import url_generator
from mailer import create_mail,send_card



def before_five(x):
    # Following 3 lines are for testing
    yy,mm,dd=str(x).split('-')
    dat='%%%%'+'-'+mm+'-'+dd
    try:
        print('HELLO')
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:
            # print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            sql='select Emp_Id,emp_name,team_name from employee_data where emp_dob like \''+dat+'\''
            # print(sql)
            # print('--------------------------------------')
            cur=conn.cursor()
            result=cur.execute(sql)
            for i in result:
                # print(i)
                # print('--------------------------------------')
                sql2='select emp_id,emp_email from employee_data where team_name=\''+i[2]+'\' and emp_id!='+str(i[0])
                print(sql2)
                # print('--------------------------------------')
                res=cur.execute(sql2)
                for j in res:
                    x=url_generator(str(i[0]),str(j[0]))
                    # print(x)
                    # print('--------------------------------------')
                    print(j[1])
                    print('--------------------------------------')
                    create_mail(j[1],'Please send your birthday wishes to '+i[1],x)

            conn.commit()
    except:
        print('Error',sys.exc_info()[0])
        return 0


def on_day(x):
    yy,mm,dd=str(x).split('-')
    dat='%%%%'+'-'+mm+'-'+dd
    try:
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:
            # print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            sql='select emp_id,emp_name,emp_email from employee_data where emp_dob like \''+dat+'\''
            # print(sql)
            # print('--------------------------------------')
            cur=conn.cursor()
            result=cur.execute(sql)
            for i in result:
                # print('yhdrkkieyyttoliykti')
                data='10.133.48.6:5000/view_card/ajdidyhbdjasdioweobkvhiowe21351836293/{}'.format(str(i[0]))
                send_card(i[2],'Happy Birthday'+i[1],data,i[1])
            conn.commit()
    except:
        print('Error*********************************** ',sys.exc_info()[0])
        return 0


def job():
    x = datetime.now().date()
    print(x)
    Timer(0,before_five,[x+timedelta(3)]).start()
    Timer(0, on_day,[x+timedelta(1)]).start()


def start_scheduling():
    interval=1
    schedule.every(interval).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(interval*24*60*60)



