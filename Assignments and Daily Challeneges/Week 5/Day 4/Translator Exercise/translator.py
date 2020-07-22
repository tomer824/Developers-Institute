from translate import Translator

translator = Translator(to_lang = "ja")

with open('something.txt') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    with open('./test-ja.txt', mode='w') as my_file2:
        my_file2.write(translation)