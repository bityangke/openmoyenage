#! /usr/bin/python3

import os
import sys
import argparse
import multiprocessing.dummy
import urllib.request
import xml.dom.minidom

def make_filelist(input_dir, output_dir, dc_type, ext):
    for xmlname in os.listdir(input_dir):
        doc = xml.dom.minidom.parse(os.path.join(input_dir, xmlname))
        for srw_dc in doc.getElementsByTagName('srw_dc:dc'):
            recordtype = srw_dc.getElementsByTagName('dc:type')
            recordid = srw_dc.getElementsByTagName('dcx:recordIdentifier')[0].firstChild.data
            recordurl = (srw_dc.getElementsByTagName('dc:identifier') + srw_dc.getElementsByTagName('dcx:illustration') + [None])[0]
            if not recordurl or all(dc_type not in r.firstChild.data for r in recordtype):
                continue
            filename = xmlname + '_' + recordid.replace(':', '__') + '.' + ext
            yield (recordurl.firstChild.data, os.path.join(output_dir, filename))

parser = argparse.ArgumentParser()
parser.add_argument('-i', required = True)
parser.add_argument('-o', required = True)
parser.add_argument('--type', default = 'miniature')
parser.add_argument('--threads', default = 4, type = int)
parser.add_argument('--ext', default = 'jpg')
args = parser.parse_args()

filelist = list(make_filelist(args.i, args.o, args.type, args.ext))
print('Found items:', len(filelist))

if not os.path.exists(args.o):
    os.makedirs(args.o)

print('Downloading...')
multiprocessing.dummy.Pool(args.threads).map(lambda url_path: urllib.request.urlretrieve(*url_path), filelist)
print('Done')
