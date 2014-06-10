# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys

import logging

import argparse

import tempfile

import atexit
import shutil

import datetime

import subprocess

import tempwork

TEMPDIRS = []
TEMPFILES = []

##    ╻  ┏━┓┏━╸┏━╸╻┏┓╻┏━╸┏━┓┏━╸╺┳╸╻ ╻┏━┓┏━┓┏━╸╺┳╸╻┏━┓┏┓╻
##    ┃  ┃ ┃┃╺┓┃╺┓┃┃┗┫┃╺┓┗━┓┣╸  ┃ ┃ ┃┣━┛┣━┫┃   ┃ ┃┃ ┃┃┗┫
## ╺━╸┗━╸┗━┛┗━┛┗━┛╹╹ ╹┗━┛┗━┛┗━╸ ╹ ┗━┛╹  ╹ ╹┗━╸ ╹ ╹┗━┛╹ ╹

class _LoggingSetupAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


        logger = logging.getLogger()
        logger.setLevel(getattr(logging, values.upper()))

## ┏━╸╻  ┏━╸┏━┓┏┓╻╻ ╻┏━┓
## ┃  ┃  ┣╸ ┣━┫┃┗┫┃ ┃┣━┛
## ┗━╸┗━╸┗━╸╹ ╹╹ ╹┗━┛╹

def cleanup():
    for tempfile in TEMPFILES:
        try:
            os.remove(tempfile)
        except:
            print(sys.exc_info())
    for tempdir in TEMPDIRS:
        try:
            shutil.rmtree(tempdir)
        except:
            print(sys.exc_info())

## ┏┳┓┏━┓╻┏┓╻
## ┃┃┃┣━┫┃┃┗┫
## ╹ ╹╹ ╹╹╹ ╹

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=tempwork.__description__
    )

    parser.register('action', 'logging_setup', _LoggingSetupAction)

    parser.add_argument('--logging', action='logging_setup', default='none', help='debug|info|warning|error|none')

    parser.add_argument('--test', action='append')

    parser.add_argument('command')
    parser.add_argument('command_args', nargs='*')

    args = parser.parse_args()
    logging.info(repr(args))

    return

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        pass

