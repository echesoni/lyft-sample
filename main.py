from flask import Flask, flash, g, jsonify, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import Form, TextField
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.config['SECRET_KEY'] = config['DEFAULT']['SECRET_KEY']


class TextMessageForm(FlaskForm):
    text_message = TextField('text_message')


@app.route("/", methods=['GET','POST'])
def home():
    form = TextMessageForm()

    if form.validate_on_submit():
        if request.method == 'POST':
            text_message = form.text_message.data
            response_message = text_message[2::3]
            flash(response_message)

            return redirect(url_for('home'))

    return render_template("home.html", form=form)

@app.route("/test", methods=['POST'])
def test():
    data = request.get_json()
    string_to_cut = data['string_to_cut']
    return_string = data['string_to_cut'][2::3]

    return jsonify({'return_string' : return_string})

if __name__ == "__main__":
    app.run(debug=True)
