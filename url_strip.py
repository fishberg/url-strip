#!/usr/bin/env python

import sys
import re
import os
import subprocess
import shlex
import argparse
from urllib.parse import urlparse
from colorama import Fore, Style

################################################################################

USERNAME = os.getlogin()
BASE_AMAZON = 'https://www.amazon.com'
BASE_YOUTUBE = 'https://www.youtube.com'
BASE_GMAIL = 'https://mail.google.com'
BASE_FOLDER = f'/home/{USERNAME}'

def strip_amazon(url):
    base = BASE_AMAZON
    pattern = r"/([A-Z0-9]{10})(?:/|\?|$)" # find 10 character ID after /

    identity = re.findall(pattern,url)
    assert len(identity) == 1
    
    identity = re.search(pattern,url)
    append = identity.group(1) # remove leading / and (optional) trailing character

    return base + '/dp/' + append

def strip_youtube(url):
    base = BASE_YOUTUBE
    pattern = r'[?&]v=[^&]+'

    identity = re.findall(pattern,url)
    assert len(identity) == 1
    append = identity[0][1:] # remove leading ?/&
    return base + '/watch?' + append

def strip_gmail(url):
    base = BASE_GMAIL
    frag = urlparse(url).fragment
    thread_id = frag.split('/')[-1].split('?')[0] # get last part of fragment, remove query parameters

    return base + '/mail/u/0/#inbox/' + thread_id

def strip_folder(url):
    base = BASE_FOLDER
    return re.sub('^' + BASE_FOLDER,'~',url)

PARSERS = {
    BASE_AMAZON: strip_amazon,
    BASE_YOUTUBE: strip_youtube,
    BASE_GMAIL: strip_gmail,
    BASE_FOLDER: strip_folder,
}

def strip(url):
    for key in PARSERS.keys():
        if re.search('^' + key,url):
            return PARSERS[key](url)
    print('ERROR: no matching parser detected for clipboard contents',file=sys.stderr)
    sys.exit(1)

################################################################################

def main():
    CLIPBOARD_MODE = len(sys.argv) == 1
    print(f'{Fore.CYAN}{Style.BRIGHT}CLIPBOARD_MODE: {Style.RESET_ALL}{CLIPBOARD_MODE}')

    if CLIPBOARD_MODE:    
        # xclip -o
        in_url = subprocess.check_output(['xclip', '-o'],universal_newlines=True).strip()
        pass
    else:
        in_url = sys.argv[1]
    print(f'{Fore.GREEN}{Style.BRIGHT}input: {Style.RESET_ALL}{in_url}')

    out_url = strip(in_url)
    print(f'{Fore.RED}{Style.BRIGHT}output: {Style.RESET_ALL}{out_url}')

    if CLIPBOARD_MODE:
        # echo -n '{out_url}' | xclip -selection c
        echo_command = shlex.split(f"echo -n '{out_url}'")
        xclip_command = shlex.split('xclip -selection c')

        echo_proc = subprocess.Popen(echo_command, stdout=subprocess.PIPE)
        xclip_proc = subprocess.call(xclip_command, stdin=echo_proc.stdout)
        pass
    else:
        print(out_url)

################################################################################

if __name__ == '__main__':
    main()
