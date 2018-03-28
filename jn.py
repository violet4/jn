#!/usr/bin/env python3
"""start a jupyter notebook

Version 0.1
2018-02-02
"""
import argparse
from settings import environments

envs = {
    i: env
    for i, env in enumerate(environments)
}

def run_main():
    args = parse_cl_args()

    env = envs.get(int(args.env))
    env.start()

    success = True
    return success

def get_available_environments_help():
    result = list()
    for k in sorted(envs.keys()):
        env = envs[k]
        result.append('{}. {}'.format(k, env))
    return '\n'.join(result)

def parse_cl_args():
    argParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    argParser.add_argument(
        'env', nargs='?', default=0,
        help='available environments:\n' + get_available_environments_help()
    )

    args = argParser.parse_args()
    return args


if __name__ == '__main__':
    success = run_main()
    exit_code = 0 if success else 1
    exit(exit_code)

