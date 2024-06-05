""" 呼び出しプログラムの呼び出しプログラム（READMEでいうところの二重呼び出しプログラム）
"""
from argparse import ArgumentParser

import __add_rootpath
from cli_config_test.cli.tools.test1_cli import add_arguments


def main(*args, **kwargs):
    from cli_config_test.tools import test1_1

    test1_1.main(**kwargs)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))


