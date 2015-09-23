#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

d = dict(a = 'a', b = 'b')
js = json.dumps(d)
print type(js)
print js

jo = json.loads(js)
print type(jo)
print jo
