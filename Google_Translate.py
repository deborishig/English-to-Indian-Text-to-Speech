#Test to see if the translator is working

from googletrans import Translator
translator = Translator()
translator.translate('I like eating')
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
g=translator.translate('I like eating', dest='ne')
print(g);
