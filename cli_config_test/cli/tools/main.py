from argparse import ArgumentParser, _SubParsersAction


def add_arguments(parser: ArgumentParser) -> ArgumentParser:

    subparsers: _SubParsersAction = parser.add_subparsers()

    add_test1(subparsers)
    add_test2(subparsers)
    add_test3(subparsers)

    return parser


def add_test1(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import test1
    parser: ArgumentParser = subparsers.add_parser("test1")
    parser: ArgumentParser = test1.add_arguments(parser)

    def callback(*args, **kwargs):
        from ...tools import test1_2
        test1_2.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser


def add_test2(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import test2
    parser: ArgumentParser = subparsers.add_parser("test2")
    parser: ArgumentParser = test2.add_arguments(parser)

    def callback(*args, **kwargs):
        from ...tools import test2
        test2.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser


def add_test3(subparsers: _SubParsersAction) -> ArgumentParser:
    from . import test3
    parser: ArgumentParser = subparsers.add_parser("test3")
    parser: ArgumentParser = test3.add_arguments(parser)

    def callback(*args, **kwargs):
        from ...tools import test3
        test3.main(**kwargs)

    parser.set_defaults(callback=callback)

    return parser