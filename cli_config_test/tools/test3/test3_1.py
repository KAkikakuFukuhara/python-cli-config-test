""" test3_1
"""
from argparse import ArgumentParser

import __add_rootpath
from cli_config_test.cli.tools.test3.test3_1 import add_arguments
from cli_config_test.lib import testlib


def main(*args, **kwargs):
    print("test3_1")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))