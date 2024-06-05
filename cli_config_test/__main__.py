from argparse import ArgumentParser

import __add_rootpath
from cli_config_test.cli.main_cli import add_arguments
from cli_config_test.tools.__main__ import main as main_


def main(*args, **kwargs):
    main_(**kwargs)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))
