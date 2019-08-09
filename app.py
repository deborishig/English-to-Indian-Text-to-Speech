from flask import Flask, render_template, request , flash , redirect, url_for
from googletrans import Translator
from wtforms import Form, StringField, TextAreaField, SelectField, PasswordField, validators
from wtforms.validators import InputRequired
from gtts import gTTS
import os



app = Flask(__name__)
app.secret_key='secret123'


class RegisterForm(Form):

    Language = SelectField('Specify Language - ne for Nepali, bn for Bengali, hi for Hindi', choices= [('ne','Nepali'), ('bn','Bengali'), ('hi','Hindi'), ('en', 'English')])

    Sentence = StringField('Enter Sentence to be translated', [validators.Length (min=1, max=100)])

    Output_File_Name = StringField('Specify name of Output file', [validators.Length (min=1, max=100)])


    
@app.route('/', methods =['GET', 'POST'])
def home():
     form = RegisterForm(request.form)
     if request.method == 'POST' and form.validate():
        
        Language = form.Language.data
        Language = request.form['Language']
        Sentence = request.form['Sentence']
        Output_File_Name = request.form['Output_File_Name']

        form.Language.choices= [('ne','nepali'), ('bn','Bengali'), ('hi','Hindi')]

        translator = Translator()
        translator.translate(Sentence, dest=Language)
        translation = translator.translate(Sentence, dest=Language)

        tts = gTTS(text=translation.text, lang=Language)
        
        tts.save(Output_File_Name+'.mp3')
        
        flash (translation.text)
        flash("Please look for Output file in your app source folder/desktop")
        return redirect(url_for('success'))
            
     else:

        flash('Please enter an English Sentence in the field above')
     return render_template('home.html', form=form)


@app.route('/success', methods=['GET','POST'])
def success():
       return render_template('success.html')



# Specifying the local host path with debugging = true

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

