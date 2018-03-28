from environment import Environment

environments = [
    Environment(
        title='default (current directory)',
    ),
    Environment(
        directory='~/jupyter-notebooks',
        title='main',
        port=8888,
    ),
]
