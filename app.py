from flask import Flask, render_template, url_for, request


app = Flask(__name__)
__name__ = "__main__"

spanishquestions = [
    {
        "id": "1",
        "question": "How do you say 'Good Morning' in Spanish?",
        "answers": ["a) Buenos Dias", "b) Buenas Tardes", "c) Buenas Noches"],
        "correct": "a) Buenos Dias"
    },
    {
        "id": "2",
        "question": "How do you say 'Good Night' in Spanish?",
        "answers": ["a) Buenos Dias", "b) Buenas Tardes", "c) Buenas Noches"],
        "correct": "c) Buenas Noches"
    },
    {
        "id": "3",
        "question": "How do you say 'breakfast' in Spanish?",
        "answers": ["a) Leche", "b) Pan", "c) Desayuno"],
        "correct": "c) Desayuno"
    },
    {
        "id": "4",
        "question": "How do you say 'bread' in Spanish?",
        "answers": ["a) Leche", "b) Pan", "c) Desayuno"],
        "correct": "b) Pan"
    },
]

englishquestions = [
    {
        "id": "1",
        "question": "What is the Capital of Syria?",
        "answers": ["a) Beirut", "b) Damascus", "c) Baghdad"],
        "correct": "b) Damascus"
    },
    {
        "id": "2",
        "question": "What is the square root of Pi?",
        "answers": ["a) 1.7724", "b) 1.6487", "c) 1.7872"],
        "correct": "a) 1.7724"
    },
    {
        "id": "3",
        "question": "How many counties are there in England?",
        "answers": ["a) 52", "b) 48", "c) 45"],
        "correct": "b) 48"
    }
]

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/learnenglish',methods=['POST', 'GET'])
def learnenglish():
    if request.method == 'GET':  
        return render_template('/learnenglish.html',data=englishquestions)
    else:
        questionright = 0
        for question in englishquestions:
            print()
            if request.form[question.get('id')] == question.get('correct'):
                questionright += 1
        return render_template('englishresults.html', total=len(englishquestions), result=questionright)

@app.route('/learnspanish',methods=['POST', 'GET'])
def learnspanish():  
    if request.method == 'GET': 
        return render_template('/learnspanish.html',data=spanishquestions)
    else:
        questionright = 0
        for question in spanishquestions:
            if request.form[question.get('id')] == question.get('correct'):
                questionright += 1
        return render_template('spanishresults.html', total=len(spanishquestions), result=questionright)

if __name__ == "__main__":
    
    
    app.run(debug=True)

    