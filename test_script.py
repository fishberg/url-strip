import url_strip as S

amazon_dp = [
        ('https://www.amazon.com/Logitech-Wireless-Keyboard-Touchpad-PC-connected/dp/B014EUQOGK/ref=sr_1_4?crid=PBGHN9ESFPE&keywords=keyboard+and+touchpad&qid=1677459820&s=electronics&sprefix=keyboard+and+touchpa%2Celectronics%2C107&sr=1-4', 'https://www.amazon.com/dp/B014EUQOGK'),
        ('https://www.amazon.com/Brother-P-touch-PTD210-Bundle-included/dp/B09QXZ7ZRD/ref=sr_1_8?crid=1BZJ6M311IJOG&keywords=label%2Bmaker&qid=1677600206&sprefix=label%2Bmake%2Caps%2C113&sr=8-8&th=1', 'https://www.amazon.com/dp/B09QXZ7ZRD'),
        ('https://www.amazon.com/dp/B075ZH5Z9F?ref_=cm_sw_r_apin_dp_KBE6K9CW71TM71HTEDKE','https://www.amazon.com/dp/B075ZH5Z9F'),
        ('https://www.amazon.com/dp/B0BT3LRPQM?ref_=cm_sw_r_apin_dp_MH64NP802FB4ENF9RR4T','https://www.amazon.com/dp/B0BT3LRPQM'),
        ('https://www.amazon.com/dp/B0BQ54DQNM?ref_=cm_sw_r_apin_dp_VEMDD19QDPRB5NBGKFK6','https://www.amazon.com/dp/B0BQ54DQNM'),
        ('https://www.amazon.com/dp/B06XFVBVQ5?ref_=cm_sw_r_apin_dp_5Y8D9KKZSZREVNJN3T9X','https://www.amazon.com/dp/B06XFVBVQ5'),
        ('https://www.amazon.com/dp/B0798V3CGC?ref_=cm_sw_r_apin_dp_QRQYXEPFSH08AFMRG6SF','https://www.amazon.com/dp/B0798V3CGC'),
        ('https://www.amazon.com/StarTech-com-Duplicator-Standalone-Docking-SDOCK2U33RE/dp/B00KT3BEAS?th=1','https://www.amazon.com/dp/B00KT3BEAS'),
        ('https://www.amazon.com/Introduction-Computation-Programming-Using-Python/dp/0262529629','https://www.amazon.com/dp/0262529629'),
]

amazon_gp = [
        ('https://www.amazon.com/gp/product/0521679710/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1','https://www.amazon.com/dp/0521679710')
]

youtube = [
]

def test_amazon_dp():
    for test_input, test_output in amazon_dp:
        assert S.strip(test_input) == test_output

def test_amazon_gp():
    for test_input, test_output in amazon_gp:
        assert S.strip(test_input) == test_output

def test_youtube():
    for test_input, test_output in youtube:
        assert S.strip(test_input) == test_output
