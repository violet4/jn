# jn
jupyter notebook launcher and launch manager

write jupyter launch configurations as simple python object instantiations, and then easily launch them using simple command-line options

Sample configuration:

    Environment(
        directory='~/jupyter-notebooks',
        conda_env='python3.6',
        title='main',
        port=8891,
    )

then run `python jn.py -h`:

	...
	positional arguments:
	  env         available environments:
	              0. default (current directory)
	              1. main
	...

then run the chosen environment:

	python jn.py 0
	running commands: ...
	...
	[I 17:40:00.075 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/?token=...
	[I 17:40:00.075 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
	...

# Setup

copy settings_sample.py to settings.py, then update settings.py as desired. See environment.py for the options that are available for instantiating an `Environment` object.
