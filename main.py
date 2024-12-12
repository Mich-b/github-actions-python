from os import name


def greet():
    print('Hello, GitHub Actions!')
    if name == 'main': greet()