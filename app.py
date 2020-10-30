from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def homepage2():
    return "Penguins are cute!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f"How did you know I liked, {users_dessert}"

@app.route('/madlibs/<adjective>/<noun>')
def user_madlibs(adjective, noun):
    return f"Look! that has, {adjective} in the, {noun},! "

@app.route('/multiply/<x>/<y>')
def user_number(x,y):
    numb1 = int(x)
    numb2 = int(y)
    result = numb1 * numb2
    return f"{x} times {y} is {result}"


if __name__ == '__main__':
    app.run(debug=True)