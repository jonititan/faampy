# -*- coding: utf-8 -*-
"""
Script for downloading faampy data, which are updated regularly
"""

import faampy
import os
import tempfile
import urllib2
import sys
import zipfile

FAAMPY_DATA_URL = 'http://www.faam.ac.uk/axel_share/faampy_data.zip'


def dlfile(url, local_zipfile):
    # Open the url
    try:
        sys.stdout.write("downloading %s\n" % url)
        f = urllib2.urlopen(url)
        
        # Open our local file for writing
        with open(local_zipfile, "wb") as local_file:
            local_file.write(f.read())

    # handle errors
    except (urllib2.HTTPError, e):
        print("HTTP Error:", e.code, url)
    except (urllib2.URLError, e):
        print("URL Error:", e.reason, url)
    return


def _argparser():
    import argparse
    from argparse import RawTextHelpFormatter
    sys.argv.insert(0, 'faampy data_download')
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('password',
                        action="store",
                        type=str,
                        help='zip file password')
    return parser


def main():
    parser = _argparser()
    args = parser.parse_args()
    passwd = args.password
    if not os.path.exists(faampy.FAAMPY_DATA_PATH):
        os.mkdir(faampy.FAAMPY_DATA_PATH)
        sys.stdout.write('Created %s ...\n' % faampy.FAAMPY_DATA_PATH)
    local_zipfile = tempfile.mktemp(suffix='.zip')
    dlfile(FAAMPY_DATA_URL, local_zipfile)

    _zip = zipfile.ZipFile(local_zipfile)
    _zip.extractall(path=faampy.FAAMPY_DATA_PATH, pwd=passwd)
    return


if __name__ == '__main__':
    main()
