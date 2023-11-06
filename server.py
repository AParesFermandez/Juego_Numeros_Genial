from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
winners = []  # Lista de ganadores

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
    print(f"El número aleatorio es: {session['number']}")
    # Resto del código...

    message = None  # Inicializa el mensaje

    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        session['attempts'] += 1
        if session['attempts'] >= 5:
            message = "Tú pierdes. El número era {}.".format(session['number'])
            session.pop('number')
            session.pop('attempts')
        if user_guess == session['number']:
            winners.append(( session['attempts']))
            session.pop('number')
            session.pop('attempts')
            return redirect(url_for('scoreboard'))
        elif user_guess < session['number']:
            message = "El número es mayor. Intenta de nuevo."
        else:
            message = "El número es menor. Intenta de nuevo."
    return render_template('index.html', message=message)

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html', winners=winners)

if __name__ == '__main__':
    app.run()

