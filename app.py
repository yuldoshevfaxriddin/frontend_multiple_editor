from flask import Flask, render_template, request

app = Flask(__name__)
host = 'localhost'
port = 80
demo = True
users = []
ip_adress = set()
time = 60

@app.get('/')
def index():
    ip = request.remote_addr
    if ip in ip_adress and not demo:  
       return 'Siz test Topshirgansiz !...'
    return render_template('idex.html',time_limit = time)

@app.post('/')
def home():
    username = request.form.get('username','anomim') 
    content = request.form.get('content','No content') 
    time = request.form.get('time','no time') 
    user = {
        'ip':request.remote_addr,
        'username':username,
        'content':content,
        'length':len(set(content.replace('\n',' ').split())),
        'tags':content.replace('\n',' ').split(),
        'time':time
    }
    ip_adress.add(request.remote_addr)
    users.append(user)
    return "Barcha ishtirokchilar yakunlashini kuting!..."

@app.get('/view')
def view():
    return render_template('view.html',users=users)

@app.get('/clear')
def clear():
    global users,ip_adress,demo,time
    demo = True if request.args.get('demo',None) else False
    time = int(request.args.get('time',None)) if request.args.get('time',None) else 60
    users = []
    ip_adress = set()
    print(request.remote_addr,users,ip_adress,demo,time)
    return str(demo)+str(users)+str(ip_adress)+str(time)


app.run(debug=True,host=host,port=port)
