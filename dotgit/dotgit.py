#! /usr/bin/env python3

__version__ = '2.0.0-alpha'
__author__ = 'Kobus van Schoor'
__author_email__ = 'v.schoor.kobus@gmail.com'
__url__ = 'https://github.com/kobus-v-schoor/dotgit'
__license__ = 'GNU General Public License v2 (GPLv2)'

import logging

from args import Arguments

if __name__ == '__main__':
    args = Arguments()
    logging.basicConfig(format='%(message)s ', level=args.verbose_level)
