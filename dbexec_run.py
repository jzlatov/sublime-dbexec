# -*- coding: utf-8 -*-
import sys
import re

def run(textWithConString, textToExec): 
    m = re.match("(?P<prefix>--connection=)(?P<conString>.*)", textWithConString)
    if m and len(m.groups()) == 2:
        conString = m.group("conString")
    print "Connection: {0}".format(conString)
    print "SQL : {0}".format(textToExec)

#        sys.path.insert(0, "c:\\Python27\\Lib\\site-packages\\")
    from sqlalchemy import create_engine
    engine = create_engine(conString)
    result = engine.execute(textToExec)
    print "|".join(["{0:<20}".format(c) for c in result.keys()])
    print "|".join(["{0:_<20}".format("") for c in result.keys()])
    for row in result:
        print "|".join(["{0:<20}".format(c) for c in row])
    print "|".join(["{0:_<20}".format("") for c in result.keys()])

    result.close()

if __name__ == "__main__":
    print sys.argv[1]
    try:
        with open(sys.argv[1], 'r') as f:
            textToExec = f.read()
            run(textToExec, textToExec)
    except IOError as e:
        print 'Operation failed: %s' % e.strerror
