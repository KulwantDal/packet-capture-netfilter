from netfilterqueue import NetfilterQueue
import binascii
from struct import *

def print_and_accept(args):
    count = len(args.get_payload()[52:])
    print(unpack("!{count}s".format(count=count),args.get_payload()[52:]))
    args.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
