from gtts import gTTS
import os
from googletrans import Translator
import subprocess

print("Welcome to the Text to Speech translator Programme")


# Prompt for input of output file path

Output_File_path = input("Please specify exact path on Local Machine where file is to be saved:")


# Specify the directory where the Output file has to be saved.

os.chdir(Output_File_path)

# Taking Input in English and translating to either Hindi or Nepali (Google Language code ="ne")

translator = Translator()

# Instantiating input to capture entry for translation in English and then translating to either Hindi or Nepali Devnagiri

English_text = input("Please enter the English sentence that you need translated:")
Select_language= input("Please enter ne in lower case for Nepali and hi , in lower case, for Hindi and be for Bengali and of course en for English:")
translator.translate(English_text, dest=Select_language)
translation=translator.translate(English_text, dest=Select_language)
print("Here's your translation:"+translation.text)


# Text block to convert translated Nepali text into either Hindi or Nepali speech and saving the output file(s) in wave format onto a specified path on LOCAL_MACHINE

tts = gTTS(text=translation.text, lang=Select_language)


# Prompt for the specification of the Output file name

Output_File_Name = input("Please specify the name of the Output file:")



# Code block for the output file

tts.save(Output_File_Name + ".wav")
os.system("mpg321"+Output_File_Name + ".wav")


# Confirm generation of output file with file name and location

print("Your saved file name is "+Output_File_Name+".wav")
