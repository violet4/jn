import os

class Environment:
    def __init__(self, directory=None, conda_env=None, title=None, port=None,
            use_jn_config=True):
        self.directory = (
            os.path.expanduser(directory)
            if directory is not None
            else None
        )
        self.conda_env = conda_env
        self.title = title
        self.port = port
        self.use_jn_config = use_jn_config

    def __str__(self):
        return str(self.title)

    def start(self):
        commands = list()
        if self.directory is not None:
            commands.append("cd '{}'".format(self.directory))

        title = 'jn'
        if self.title is not None:
            title += '-'+self.title

        title = r"\033]0;{title}\007".format(title=title)
        commands.append("echo -en '{}'".format(title))

        if self.conda_env is not None:
            commands.append("source activate '{}'".format(self.conda_env))

        if self.use_jn_config:
            config_file = os.path.expanduser('~/.jupyter/jupyter_notebook_config.json')
            config = "--config='{}'".format(config_file)
        else:
            config = ''

        jn_command = "jupyter notebook {}".format(config)
        if self.port is not None:
            jn_command += ' --port={}'.format(self.port)
        commands.append(jn_command)

        commands = ' ; '.join(commands)
        print('running commands:', commands)
        # I don't know why this prints '-en'; that's part of one of the commands, but it shouldn't be printing that out. anyways, the command still behaves as expected.
        os.system(commands)
