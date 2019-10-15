from flask import Flask,render_template,request
# from mailer import get_data
from threading import Timer
from after import start_scheduling
from data_access import create_user,select_user,fetch_name,save_message,fetch_messages
import random
app=Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    print(request.remote_addr)
    return render_template('index.html')

@app.route('/send_email',methods=['POST'])
def send_email():
    if request.method=='POST':
        to=request.form['to']
        mail=request.form['mail']
        sub=request.form['subject']
        # get_data(to,sub,mail)
        return '<h1>Mail Send Successfully</h1>'

@app.route('/a')
def a():
    return render_template('sel_index.html')

@app.route('/send_data',methods=['POST'])
def send_data():
    if request.method=='POST':
        empid=request.form['empid']
        name=request.form['name']
        email=request.form['email']
        dob=request.form['dob']
        team_name=request.form['team_name']
        designation=request.form['designation']
        n1=request.form['n+1_manager']
        n2=request.form['n+2_manager']
        du=request.form['du_head']
        a=create_user(empid,name ,email,dob ,team_name,designation,n1,n2,du)
        if a==0:
            return render_template('something_went_wrong.html')
        return render_template('success.html')

@app.route('/select_data',methods=['POST'])
def select_data():
    if request.method=='POST':
        empid=request.form['id']
        a=select_user(empid)

        if a==0:
            return render_template('something_went_wrong.html')
        return 'Welcome'+a+'Back'


@app.route('/message/bdfconskabffdjkghbdskfhbsdfbsddioerbcxvmnrweoiher857648766765454/<for_id>/8975677sdscsuidhjsdhbi345455653/<from_id>')
def message_send(for_id,from_id):
    # select emp_name from employee_data where emp_id=from_id
    name=fetch_name(from_id)
    name_rec=fetch_name(for_id)
    return render_template('fetch_data.html',name=name,emp_id=for_id,s_emp_id=from_id,name_rec=name_rec)


@app.route('/message', methods=['POST'])
def read_message():
    for_id=request.form['for_id']
    msg=request.form['mssg']
    from_id=request.form['from_id']
    name=request.form['name']
    save_message(for_id,name,from_id,msg)
    return 'thank you'

@app.route('/view_card/ajdidyhbdjasdioweobkvhiowe21351836293/<for_id>',methods=['get'])
def view_card(for_id):
    lis=fetch_messages(for_id)
    name=fetch_name(for_id)
    # fonts=['Lucida Fax', 'Palatino Linotype', 'Lucida Sans', 'Trebuchet MS', 'Fira Mono', 'Lucida Console', 'Monaco', 'Brush Script Std', 'Lucida Handwriting', 'Herculanum']
    fonts=['Kalam','Sacramento','Handlee','Nothing You Could Do','Charmonman']
    color=['red','orange','balck']
    x=[]
    y=[]
    i=0
    for _ in lis:
        x.append(random.randint(0,len(fonts)-1))
        y.append(i%3)
        i+=1
    lis=zip(lis,x,y)
    return render_template('card.html',lis=lis,fonts=fonts,col=color,name=name,for_id=for_id)


if __name__ == '__main__':
    Timer(0,start_scheduling).start()
    app.run()

