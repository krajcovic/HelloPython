 #!/usr/bin/python
 # -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import time

print u'Hello world'

while 1:
    print 'Before pass'
    pass # činné čekání na přerušení
    print 'Past pass'

    time.sleep(1)

