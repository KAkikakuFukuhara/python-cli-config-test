from argparse import ArgumentParser


def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument("input", type=str, help="input path")
    return parser


