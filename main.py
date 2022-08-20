from translate import Translator

lang = {
    1: 'en',
    2: 'es',
    3: 'pt',
    4: 'zh',
    5: 'fr',
    6: 'de',
    7: 'ko',
    8: 'ja',
    9: 'hi',
    10: 'ru'
}

languages = {
    1: 'English',
    2: 'Spanish',
    3: 'Portuguese',
    4: 'Chinese',
    5: 'French',
    6: 'German',
    7: 'Korean',
    8: 'Japanese',
    9: 'Hindi',
    10: 'Russian',
}

def console_input(translator,language):
    try:
        result = open('result.txt', mode='w')
        text = input('Enter Your Sentence : ')
        print('Generating result.txt....')
        result.write(f'---{language}---\n')
        result.write(translator.translate(text))
        print('Saving and closing result.txt')
        result.close()
    except IOError as er:
        print("oops IO Error occured!!")
        raise er


def file_input(translator,language):
    while True:
        path = input('Please Enter File Path : ')
        try:
            source = open(path, mode='r')
            result = open('result.txt', mode='w')
            print('Generating result.txt....')
            result.write(f'---{language}---\n')
            result.write(translator.translate(source.read()))
            source.close()
            print('Saving and closing result.txt')
            result.close()
        except FileNotFoundError:
            print("Enter correct File Path!!")
        except IOError as er:
            print("oopps IO Error orrcured!!")
            raise er
        else:
            break


if __name__ == '__main__':
    while True:
        lang_choice = int(input(
            '----Languages----\n1. English(en)\n2. Spanish(es)\n3. Portuguese(pt)\n4. Chinese(zh)\n5. French(fr)\n6. German(de)\n7. Korean(ko)\n8. Japanese(ja)\n9. Hindi(hi)\n10. Russian(ru)\nEnter your choice (1-11) : '))
        if 1 <= lang_choice <= 11:
            translator = Translator(to_lang=lang[lang_choice])
            while True:
                print('----Mode Selection----')
                mode = int(input('1.Console Mode(Single line)\n2.File Mode(Multi line)\nEnter you choice (1-2) : '))
                if mode == 1:
                    console_input(translator, languages[lang_choice])
                    break
                elif mode == 2:
                    file_input(translator, languages[lang_choice])
                    break

            break
