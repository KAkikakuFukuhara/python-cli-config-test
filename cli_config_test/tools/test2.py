""" test1_1と同じ内容。__main__.pyの説明用
"""
import __add_rootpath
from argparse import ArgumentParser
import pprint

import __add_rootpath
from cli_config_test.cli.tools.test2_cli import add_arguments
from cli_config_test import lib as cli_config_test


def main(*args, **kwargs):
    # 入力の確認
    pprint.pprint(kwargs)

    # sys.moduleの確認
    print(cli_config_test)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))
