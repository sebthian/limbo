# -*- coding: UTF-8 -*-
import os
import sys

import vcr

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(DIR, '../../limbo/plugins'))

from translate import on_message

def test_translate():
    with vcr.use_cassette('test/fixtures/translate_basic.yaml'):
        ret = on_message({"text": u"!translate ATAATA"}, None)
        assert 'II' in ret
