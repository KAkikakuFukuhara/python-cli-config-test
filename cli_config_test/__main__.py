from argparse import ArgumentParser

import __add_rootpath
from cli_config_test.cli.cli_main import add_arguments


def main(*args, **kwargs):
    if 'callback' in kwargs.keys():
        callback = kwargs.pop('callback')
        callback(**kwargs)
    else:
        parser = ArgumentParser()
        add_arguments(parser)
        parser.print_help()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))
