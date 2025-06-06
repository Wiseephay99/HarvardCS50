def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "French": "Bonjour",
        "Italian": "Ciao",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name} "
    print(msg)
    
if __name__ == "__main__":
    import argparse 
    parser = argparse.ArgumentParser(
        description = 'Provides a personal greeting'
    )
    parser.add_argument(
        "name", metavar='name',
        help="The name of the person to greet"
    )
    parser.add_argument(
        "-l", "--lang", metavar='language',
        required=True, choices=['English', 'Spanish', 'French', 'Italian', 'German'],
        help="The Language of the greeting"
    )
    args = parser.parse_args()
    hello(args.name, args.lang)
    # msg = f'Hello, {args.name}!'
    # print(msg) 