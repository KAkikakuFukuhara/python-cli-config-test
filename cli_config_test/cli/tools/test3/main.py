from argparse import ArgumentParser, _SubParsersAction


def add_arguments(parser: ArgumentParser) -> ArgumentParser:

    subparsers: _SubParsersAction = parser.add_subparsers()

    add_test3_1(subparsers)
    add_test3_2(subparsers)

    return parser


def add_test3_1(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import test3_1
    parser: ArgumentParser = subparsers.add_parser("test3_1")
    parser: ArgumentParser = test3_1.add_arguments(parser)

    def callback(*args, **kwargs):
        from ....tools.test3 import test3_1
        test3_1.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser


def add_test3_2(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import test3_2
    parser: ArgumentParser = subparsers.add_parser("test3_2")
    parser: ArgumentParser = test3_2.add_arguments(parser)

    def callback(*args, **kwargs):
        from ....tools.test3 import test3_2
        test3_2.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser