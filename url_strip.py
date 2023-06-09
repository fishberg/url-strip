#!/usr/bin/env python

import sys
import re
import os
import subprocess
import shlex

################################################################################

BASE_AMAZON = 'https://www.amazon.com/'
BASE_YOUTUBE = 'https://www.youtube.com/'

def strip_amazon(url):
    base = BASE_AMAZON
    pattern = '/dp/\w+/'

    identity = re.findall(pattern,url)
    assert len(identity) == 1
    append = identity[0][1:-1] # remove leading/trailing /
    return base + append

def strip_youtube(url):
    base = BASE_YOUTUBE
    pattern = '[?&]v=\w+&'

    identity = re.findall(pattern,url)
    assert len(identity) == 1
    append = identity[0][1:-1] # remove leading/trailing ?/&
    return base + 'watch?' + append

PARSERS = {
    BASE_AMAZON: strip_amazon,
    BASE_YOUTUBE: strip_youtube
}

def strip(url):
    for key in PARSERS.keys():
        if key in url:
            return PARSERS[key](url)
    print('ERROR: no matching parser detected for clipboard contents',file=sys.stderr)
    sys.exit(1)

################################################################################

in_url = subprocess.check_output(['xclip', '-o'],universal_newlines=True)
print(f'input: {in_url}')

out_url = strip(in_url)
print(f'output: {out_url}')

# echo -n '{out_url}' | xclip -selection c
echo_command = shlex.split(f"echo -n '{out_url}'")
xclip_command = shlex.split('xclip -selection c')

echo_proc = subprocess.Popen(echo_command, stdout=subprocess.PIPE)
xclip_proc = subprocess.call(xclip_command, stdin=echo_proc.stdout)
