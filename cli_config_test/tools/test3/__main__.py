from argparse import ArgumentParser

if __name__ == "__main__":
    import __add_rootpath
else:
    from . import __add_rootpath
from cli_config_test.cli.tools.test3 import add_arguments


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
