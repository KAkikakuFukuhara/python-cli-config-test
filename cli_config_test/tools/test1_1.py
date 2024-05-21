""" importに時間がかかるライブラリの呼び出しプログラム
"""
import __add_rootpath
from argparse import ArgumentParser
import pprint

import __add_rootpath
from cli_config_test import lib as cli_config_test


def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument("input", type=str, help="input path")
    return parser


def main(*args, **kwargs):
    # 入力の確認
    pprint.pprint(kwargs)

    # sys.moduleの確認
    print(cli_config_test)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))
