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
        "question": "Como se dice 'Buenos Dias' en Ingles?",
        "answers": ["a) Good Morning", "b) Good Afternoon", "c) Good Nigth"],
        "correct": "a) Good Morning"
    },
    {
        "id": "2",
        "question": "Como se dice 'Buenas Noches' en Ingles?",
        "answers": ["a) Good Morning", "b) Good Afternoon", "c) Good Nigth"],
        "correct": "c) Good Nigth"
    },
    {
        "id": "3",
        "question": "Como se dice 'desayuno' en Ingles?",
        "answers": ["a) Milk", "b) Bread", "c) Breakfast"],
        "correct": "c) Breakfast"
    },
    {
        "id": "4",
        "question": "Como se dice 'pan' en Ingles",
        "answers": ["a) Milk", "b) Bread", "c) Breakfast"],
        "correct": "b) Bread"
    },
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

    