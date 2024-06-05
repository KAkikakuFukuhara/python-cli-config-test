from argparse import ArgumentParser

if __name__ == "__main__":
    import __add_rootpath
else:
    from . import __add_rootpath
from cli_config_test.cli import add_arguments
from cli_config_test.tools import main as main_


def main(*args, **kwargs):
    main_(**kwargs)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))
