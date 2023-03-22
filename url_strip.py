#!/usr/bin/env python

import sys
import re
import os
import subprocess

################################################################################

BASE_AMAZON = 'https://www.amazon.com/'

def strip_amazon(url):
    base = BASE_AMAZON
    pattern = '/dp/\w+/'

    ident = re.findall(pattern,url)
    assert len(ident) == 1
    append = ident[0][1:-1] # remove leading/trailing /
    return base + append

PARSERS = {
    BASE_AMAZON: strip_amazon
}

def strip(url):
    # TODO detect which parser to use
    return PARSERS[BASE_AMAZON](url)

################################################################################

if len(sys.argv) == 1:
    print('no command line input provided, grabbing input from clipboard')
    in_url = subprocess.check_output(['xclip', '-o'],universal_newlines=True)
elif len(sys.argv) == 2:
    print('command line input')
    in_url = sys.argv[1]
else:
    print('ERROR: incorrect command line arguments',file=sys.stderr)
    sys.exit(1)

print(f'input: {in_url}')
out_url = strip(in_url)
print(f'output: {out_url}')

command = f"echo -n '{out_url}' | xclip -selection c"
print(f'command: {command}')
os.system(command)
