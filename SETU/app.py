from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    lang = request.args.get('lang', 'en')
    return render_template('index.html', lang=lang)

@app.route('/braille')
def braille():
    lang = request.args.get('lang', 'en')
    return render_template('braille.html', lang=lang)

@app.route('/sign')
def sign():
    lang = request.args.get('lang', 'en')
    return render_template('sign.html', lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
