from flask import Flask, session

app = Flask(__name__)

@app.route('/count')
def count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return """
    <html>
    <head><title>Counting...</title></head>
    <body>
    Count %d
    </body>
    </html>
    """ % session['count']

@app.route('/reset')
def reset():
    session.pop('count')
    return "Your session was reset."

app.secret_key = '5au5ag3undhu5ky'

if __name__ == "__main__":
    app.run()
