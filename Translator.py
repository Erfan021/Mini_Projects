from translate import Translator

translator= Translator(to_lang='zh') # Chinese Language

try:
    with open('Test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        
except FileNotFoundError:
        print('No file present')
        

