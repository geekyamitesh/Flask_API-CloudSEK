from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
import time as t


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///average.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




class Avg(db.Model):
    unique_Identifier = db.Column(db.Integer, primary_key=True)
    num_1 = db.Column(db.Integer, nullable=False)
    num_2 = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.Float,  default= (num_2+num_1)/2)

    def __repr__(self) -> str:
        return f"{self.unique_Identifier}"

@app.route('/', methods=['GET'])
def greeting():
    return "Hi from Test Api"

@app.route('/calculate/<int:num_1>/<int:num_2>', methods=['GET'])
def average(num_1,num_2):
    if request.method=='GET':
        num1 = int(num_1)
        num2 = int(num_2)
        average = Avg(num_1= num1,num_2=num2,answer=(num_1+num_2)/2)
        db.session.add(average)
        db.session.commit()
        
    allTodo = Avg.query.all()
    return f"{allTodo[-1]}"


def target_result(avg):
    t.sleep(10)
    return f"{avg.answer}"
    
@app.route('/get_answer/<int:id>', methods=['GET','POST'])
def agetAnswer(id):
    if request.method=='GET':
        num1 = int(id)
        avg = Avg.query.filter_by(unique_Identifier=id).first()
        print(avg)
    # return f"{avg}",400
    if avg ==  None:
        return Response("", status= 404, mimetype='application/json')
    else:
        def eventStream():
            text = "Please wait"
            yield str(text)
            yield "\nThank you, result is "+ str(target_result(avg))
        
        resp = Response(eventStream(), status=200)
        resp.headers['Content-Type'] = 'text/event-stream'
        resp.headers['Cache-Control'] = 'no-cache'
        resp.headers['Connection'] = 'keep-alive'
        return resp




if __name__ == "__main__":
    app.run( port = 5001, debug = True)