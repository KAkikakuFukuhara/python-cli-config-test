from argparse import ArgumentParser, _SubParsersAction


def add_arguments(parser: ArgumentParser) -> ArgumentParser:

    subparsers: _SubParsersAction = parser.add_subparsers()

    add_test1(subparsers)
    add_test2(subparsers)

    return parser


def add_test1(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import test1_cli
    parser: ArgumentParser = subparsers.add_parser("test1")
    parser: ArgumentParser = test1_cli.add_arguments(parser)

    def callback(*args, **kwargs):
        from ...tools import test1_2
        test1_2.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser


def add_test2(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import test2_cli
    parser: ArgumentParser = subparsers.add_parser("test2")
    parser: ArgumentParser = test2_cli.add_arguments(parser)

    def callback(*args, **kwargs):
        from ...tools import test2
        test2.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser