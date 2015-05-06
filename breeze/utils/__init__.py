def snake_to_camel(text):
    text = text.split('_')

    camel = text.pop()

    for chunk in text:
        camel += text.capitalize()


def camel_to_snake(text):
    snake = ''

    for letter in text:
        if letter.isupper():
            snake += '_'
        snake += letter.lower()

    return snake
