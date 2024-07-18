#!/usr/bin/env python

import sys
import re
import os
import subprocess
import shlex

################################################################################

USERNAME = os.getlogin()
BASE_AMAZON = 'https://www.amazon.com'
BASE_YOUTUBE = 'https://www.youtube.com'
BASE_GMAIL = 'https://mail.google.com'
BASE_FOLDER = f'/home/{USERNAME}'

def strip_amazon(url):
    if '/dp/' in url:
        f = strip_amazon_dp
    elif '/gp/' in url:
        f = strip_amazon_gp
    return f(url)

def strip_amazon_dp(url):
    base = BASE_AMAZON
    pattern = r'/dp/[^/?]+'

    identity = re.findall(pattern,url)
    assert len(identity) == 1, str(len(identity))
    append = identity[0]
    return base + append

def strip_amazon_gp(url):
    base = BASE_AMAZON
    pattern = r'/gp/product/[^/?]+'

    identity = re.findall(pattern,url)
    assert len(identity) == 1
    append = identity[0].split('/')[3] # only product id number
    return base + '/dp/' + append

def strip_youtube(url):
    base = BASE_YOUTUBE
    pattern = r'[?&]v=[^&]+'

    identity = re.findall(pattern,url)
    assert len(identity) == 1
    append = identity[0][1:] # remove leading ?/&
    return base + 'watch?' + append

def strip_gmail(url):
    base = BASE_GMAIL
    pattern = r'\/mail\/u\/\d+\/\#\w+\/([^\?]+)'

    identity = re.findall(pattern,url)
    assert len(identity) == 1
    return base + '/mail/u/0/#inbox/' + identity[0]

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
    in_url = subprocess.check_output(['xclip', '-o'],universal_newlines=True)
    print(f'input: {in_url}')

    out_url = strip(in_url)
    print(f'output: {out_url}')

    # echo -n '{out_url}' | xclip -selection c
    echo_command = shlex.split(f"echo -n '{out_url}'")
    xclip_command = shlex.split('xclip -selection c')

    echo_proc = subprocess.Popen(echo_command, stdout=subprocess.PIPE)
    xclip_proc = subprocess.call(xclip_command, stdin=echo_proc.stdout)

################################################################################

if __name__ == '__main__':
    main()
