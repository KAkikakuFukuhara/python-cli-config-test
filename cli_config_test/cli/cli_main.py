from argparse import ArgumentParser, _SubParsersAction


def add_arguments(parser: ArgumentParser) -> ArgumentParser:

    subparsers: _SubParsersAction = parser.add_subparsers()

    add_test1(subparsers)
    add_test2(subparsers)

    return parser


def add_test1(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import cli_test1
    parser: ArgumentParser = subparsers.add_parser("test1")
    parser: ArgumentParser = cli_test1.add_arguments(parser)

    def callback(*args, **kwargs):
        from cli_config_test.tools import test1_1
        test1_1.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser


def add_test2(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import cli_test1
    parser: ArgumentParser = subparsers.add_parser("test2")
    parser: ArgumentParser = cli_test1.add_arguments(parser)

    def callback(*args, **kwargs):
        from cli_config_test.tools import test2
        test2.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser
