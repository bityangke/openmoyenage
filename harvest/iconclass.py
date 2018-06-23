import os
import json
import collections
import xml.dom.minidom
import urllib.request
import urllib.parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--oaixml')
parser.add_argument('--iconclass', default = 'iconclass')
parser.add_argument('--cut', type = int, default = 100)
args = parser.parse_args()
if not os.path.exists(args.iconclass):
	os.makedirs(args.iconclass)

stats = collections.defaultdict(int)

for i, filename in enumerate(os.listdir(args.oaixml)):
	doc = xml.dom.minidom.parse(os.path.join(args.oaixml, filename))
	for rec in doc.getElementsByTagName('dc:subject'):
		iconclass_ = rec.firstChild.data
		iconclass = iconclass_[:args.cut]
		if iconclass.count('(') != iconclass.count(')'):
			iconclass_ += ')'
			iconclass = iconclass_[:iconclass_.index(')') + 1]
		stats[iconclass.strip()] += 1


def iconclass_describe(cat, cache):
	cachepath = os.path.join(cache, cat + '.json')
	if not os.path.exists(cachepath):
		with open(cachepath, 'w') as f:
			url = 'http://www.iconclass.org/{}.json'.format(urllib.parse.quote(cat))
			json.dump(json.load(urllib.request.urlopen(url)), f)
	return json.load(open(cachepath))['txt']['en']

top = list(reversed(sorted([(v, k) for k, v in stats.items()])))[:200]
print('\n'.join('{: 6}\t{}\t{: <40}\t{: <40}\t{}'.format(k, v, iconclass_describe(v[:1], args.iconclass), iconclass_describe(v[:2], args.iconclass), iconclass_describe(v, args.iconclass)) for k, v in top))
