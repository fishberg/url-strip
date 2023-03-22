#!/usr/bin/env python

import sys
import re
import os
import subprocess
import shlex

################################################################################

BASE_AMAZON = 'https://www.amazon.com/'

def strip_amazon(url):
    base = BASE_AMAZON
    pattern = '/dp/\w+/'

    identity = re.findall(pattern,url)
    assert len(identity) == 1
    append = identity[0][1:-1] # remove leading/trailing /
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

# echo -n '{out_url}' | xclip -selection c
echo_command = shlex.split(f"echo -n '{out_url}'")
xclip_command = shlex.split('xclip -selection c')

echo_proc = subprocess.Popen(echo_command, stdout=subprocess.PIPE)
xclip_proc = subprocess.call(xclip_command, stdin=echo_proc.stdout)
