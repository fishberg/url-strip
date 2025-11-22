import url_strip as S
import yaml

with open('test_cases.yaml', 'r') as f:
    data = yaml.safe_load(f)

amazon_dp = [ (x['input'], x['output']) for x in data['amazon_dp']]
amazon_gp = [ (x['input'], x['output']) for x in data['amazon_gp']]
youtube = [ (x['input'], x['output']) for x in data['youtube']]
gmail = [ (x['input'], x['output']) for x in data['gmail']]
folder = [ (x['input'], x['output']) for x in data['folder']]

def test_amazon_dp():
    for test_input, test_output in amazon_dp:
        assert S.strip(test_input) == test_output

def test_amazon_gp():
    for test_input, test_output in amazon_gp:
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