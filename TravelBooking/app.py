from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

destinations = ["Paris", "New York", "Tokyo"]

@app.route('/')
def index():
    return render_template('index.html', destinations=destinations)

@app.route('/book/<destination>')
def book(destination):
    return render_template('book.html', destination=destination)

@app.route('/confirm_booking', methods=['POST'])
def confirm_booking():
    if request.method == 'POST':
        user_name = request.form['user_name']
        destination = request.form['destination']
        # Logic to store booking details would go here (not implemented in this example)
        return render_template('confirmation.html', user_name=user_name, destination=destination)

if __name__ == '__main__':
    app.run(debug=True)


