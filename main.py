

def list():
    article_list = []

    exit = "exit"
    show_list = "fertig"

    print("\n\nDeine eigene Einkaufsliste, die sich automatisch nach dem Alphabet sortiert.\nTippe enfach einen Artikel ein und drücke auf ENTER.\nMöchtest du mich beenden, sage einfach 'exit'.\n")

    while True:

        input_str = input()

        if input_str.lower() == exit:
            break
            
        else:
            print(chr(27) + "[2J]")
            article_list.append(input_str)
            print("\n\nDeine Einkaufsliste:")
            print('\n'.join(map(str, sorted(article_list, key=str.lower))))
            print('\n')
           


if __name__ == '__main__':
    list()
