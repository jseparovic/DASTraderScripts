from lib.common import *
from os import path
import argparse
import sys


class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help()
        sys.exit(2)

    def _print_message(self, message, file=None):
        print(message)

    def add_args(self):
        self.add_argument('-s', '--script',
                          help='Python DAS Script name without py extension',
                          action='store', required=True)
        self.add_argument('-p', '--print',
                          help='Print DAS Format',
                          action='store_true')
        self.add_argument('-t', '--test',
                          help='Print DAS Format',
                          action='store_true')


if __name__ == '__main__':
    parser = ArgParser(description='DAS Scripts')
    parser.add_args()
    args = parser.parse_args()
    script = args.script + '.py'

    if path.isfile(SCRIPT_DIR + "/" + script):
        if args.print:
            print(format_das_script(script))
        elif args.test:
            test(args.script)

    else:
        print("Usage: python dasscript.py script_without_py_extension")
