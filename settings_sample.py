from environment import Environment

environments = [
    Environment(
        title='default (current directory)',
    ),
    Environment(
        directory='~/jupyter-notebooks',
        title='main',
        ip='localhost',
        port=8888,
    ),
]
