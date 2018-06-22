import os
import cv2
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--db', default = 'db')
parser.add_argument('--images', default = 'images')
parser.add_argument('--patches', default = 'patches')
args = parser.parse_args()

for filename in os.listdir(args.db):
	boxes = json.loads(open(os.path.join(args.db, filename)).read())
	img = cv2.imread(os.path.join(args.images, filename))
	for i, box in enumerate(boxes):
		if len(box) != 4:
			continue
		x1, y1, x2, y2 = box
		patch = img[int(y1 * img.shape[0]) : int(y2 * img.shape[0]), int(x1 * img.shape[1]) : int(x2 * img.shape[1])]
		filepath = os.path.join(args.patches, '{}_{}.jpg'.format(filename, i))
		cv2.imwrite(filepath, patch)
		if os.path.getsize(filepath) == 0:
			os.remove(filepath)
