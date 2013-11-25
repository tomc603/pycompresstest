#!/usr/bin/python

import bz2
import gzip
import optparse
import os
import sys
import time


if __name__ == '__main__':
    # Create the option parser, and give a small usage example.
    optionparser = optparse.OptionParser(usage='%prog [options] -f /some/file.bz2')
    optionparser.add_option('-f', '--file', default='', dest='compfile',
                            help='Compressed file to decompress')
    options, args = optionparser.parse_args()

    if not options.compfile:
        print('ERROR: You must provide a compressed file!')
        sys.exit(1)

    try:
        print('Decompressing %s' % options.compfile)
        st = time.time()
        if options.compfile.endswith('.bz2'):
            f = bz2.BZ2File(options.compfile, 'rb')
            f.read()
            print(' Deomcpress time: %0.3f' % (time.time() - st))
            f.close()
        elif options.compfile.endswith('.gz'):
            f = gzip.GzipFile(processitem, 'rb')
            f.read()
            print(' Deomcpress time: %0.3f' % (time.time() - st))
            f.close()
    except Exception, e:
        print(' * ERROR: ', e)
    finally:
        print('Done')
