import os
import argparse
from argparse import RawTextHelpFormatter

from DataLoader import DataLoader
from ModelLoader import ModelLoader
from Summarizer import Summarizer
from Translator import TranslatorY
from LangFactory import LangFactory

import sys


os.chdir('./')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description="""
    Intro:   This is an one-touch extractive summarization machine.
             using BertSum as summatization model, extract top N important sentences.

    Note:    Since Bert only takes 512 length as inputs, this summarizer crop articles >512 length.
             If --super_long option is used, summarizer automatically parse to numbers of 512 length
             inputs and summarize per inputs. Number of extraction might slightly altered with --super_long used.

    Example: youyakuman.py --txt_file YOUR_FILE -n 3
    """)

    parser.add_argument("--txt_file", default='test.txt',
                        help='Text file for summarization (encoding:"utf-8_sig")')
    parser.add_argument("-n", default=3, type=int,
                        help='Numbers of extraction summaries')
    parser.add_argument("--lang", default='en', type=str,
                        help='If language of article isn\'t Englisth, will automatically translate by google')
    parser.add_argument("--super_long", action='store_true',
                        help='If length of article >512, this option is needed')

    args = parser.parse_args()

#    if args.super_long:
#        sys.stdout.write('\n<Warning: Number of extractions might slightly altered since with --super_long option>\n')

    # Language initiator
    print('Language initializing...')
    lf = LangFactory(args.lang)
    translator = None if args.lang in lf.support_lang else TranslatorY()

    print('Data loading...')
    data = DataLoader(args.txt_file, args.super_long, args.lang, translator).data
    print('Model loading...')
    model = ModelLoader(lf.toolkit.cp, lf.toolkit.opt, args.lang)
    print('Summarizing...')
    summarizer = Summarizer(data, model, args.n, translator)
