from translate import Translator

l  =input("Enter english text to be translated : ")
translator= Translator(from_lang="english",to_lang="tamil")
translation = translator.translate(l)
print (translation)
