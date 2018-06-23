import argparse
import numpy as np
import cv2
import cv2.ximgproc
import cv2.saliency

parser = argparse.ArgumentParser()
parser.add_argument('-i', required = True)
parser.add_argument('-o', required = True)
parser.add_argument('-k', default = 128, type = int)
parser.add_argument('--method', choices = ['selectivesearch', 'edgeboxes', 'bing'], default = 'edgeboxes')
parser.add_argument('--threads', default = 8, type = int)
parser.add_argument('--vis', action = 'store_true')
args = parser.parse_args()

cv2.setUseOptimized(True);
cv2.setNumThreads(4);

img = cv2.imread(args.i)

if args.method == 'selectivesearch':
	prop = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
	prop.setBaseImage(img)
	prop.switchToSelectiveSearchQuality()
	rects = prop.process()
	rects = rects[(rects[:, 2] > 20) & (rects[:, 3] > 20)]
elif args.method == 'edgeboxes':
	edge_detection = cv2.ximgproc.createStructuredEdgeDetection('model.yml.gz')
	edges = edge_detection.detectEdges(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0)
	orimap = edge_detection.computeOrientation(edges)
	edges = edge_detection.edgesNms(edges, orimap)
	prop = cv2.ximgproc.createEdgeBoxes()
	prop.setMaxBoxes(args.k)
	rects = prop.getBoundingBoxes(edges, orimap)
elif args.method == 'bing':
	saliency = cv2.saliency.ObjectnessBING_create()
	saliency.setTrainingPath('ObjectnessTrainedModel')
	rects = saliency.computeSaliency(img)[1].squeeze(1)
	rects[:, 2] = rects[:, 2] - rects[:, 0]
	rects[:, 3] = rects[:, 3] - rects[:, 1]

if args.vis:
	jmg = img.copy()
	for x, y, w, h in rects[:args.k]:
		cv2.rectangle(jmg, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
	cv2.imwrite(args.o, jmg)
else:
	np.savetxt(args.o, rects[:1024], fmt = '%.0f')
