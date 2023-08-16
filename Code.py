#Importando o módulo flask no projeto
from flask import Flask

#Crie um objeto da classe Flask
app = Flask(__name__)

#A função route() da classe  Flask
@app.route("/student")

# A URL ‘/’ é ligada à função first_flask.
def student_webpage():

    name = 'Alice'

    return render_template('student.html', student_name = name)

# Execute a aplicação no servidor local
app.run()
