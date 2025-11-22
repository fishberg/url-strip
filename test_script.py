import url_strip as S
import yaml

with open('test_cases.yaml', 'r') as f:
    data = yaml.safe_load(f)

amazon = [ (x['input'], x['output']) for x in data['amazon']]
youtube = [ (x['input'], x['output']) for x in data['youtube']]
gmail = [ (x['input'], x['output']) for x in data['gmail']]
folder = [ (x['input'], x['output']) for x in data['folder']]

def test_amazon():
    for test_input, test_output in amazon:
        assert S.strip(test_input) == test_output

def test_youtube():
    for test_input, test_output in youtube:
        assert S.strip(test_input) == test_output

def test_gmail():
    for test_input, test_output in gmail:
        assert S.strip(test_input) == test_output

def test_folder():
    for test_input, test_output in folder:
        assert S.strip(test_input) == test_output