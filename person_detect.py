import os
import sys
from glob import glob
import argparse
import six.moves.urllib as urllib
import tarfile

import numpy as np
import tensorflow as tf

from PIL import Image

import matplotlib.pyplot as plt

TF_MODELS_PATH = 'external/tensorflow-models/research'

sys.path.append(TF_MODELS_PATH)
sys.path.append(os.path.join(TF_MODELS_PATH, 'slim'))

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


IMAGES_DIR = "data/example"

MODEL_DIR = 'models'

MODEL_TYPE = 'ssd_mobilenet_v1_coco_2017_11_17'
#MODEL_TYPE = 'faster_rcnn_inception_resnet_v2_atrous_coco_2017_11_08'

MODEL_NAME = os.path.join(MODEL_DIR, MODEL_TYPE)

DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
OBJECT_DETECTION_PATH = os.path.join(TF_MODELS_PATH, 'object_detection')
PATH_TO_LABELS = os.path.join(OBJECT_DETECTION_PATH, 'data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90


def restore_boxes(boxes, size):
    (im_width, im_height) = size
    boxes = boxes[:, [1, 0, 3, 2]]  # swap y,x
    boxes[:, [0, 2]] *= im_width
    boxes[:, [1, 3]] *= im_height
    return boxes.astype(np.int32)


def download_models():
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
    print("Downloading models")
    opener = urllib.request.URLopener()
    MODEL_FILE = MODEL_TYPE + '.tar.gz'
    MODEL_FILE_DOWNLOADED = os.path.join(MODEL_DIR, MODEL_FILE)
    opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE_DOWNLOADED)
    tar_file = tarfile.open(MODEL_FILE_DOWNLOADED)
    for file in tar_file.getmembers():
        file_name = os.path.basename(file.name)
        if 'frozen_inference_graph.pb' in file_name:
            tar_file.extract(file, MODEL_DIR)


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


def list_images(images_dir):
    return sorted(glob(os.path.join(images_dir, '*.jpg')))


def person_detect(im_dir, vis=False):
    if not os.path.isfile(PATH_TO_CKPT):
        download_models()

    # Load a (frozen) Tensorflow model into memory
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    # Loading label map
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                                use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    images = list_images(im_dir)

    # Size, in inches, of the output images.
    IMAGE_SIZE = (12, 8)

    PERSON_CLASS_ID = 1

    all_boxes = []
    all_scores = []

    num_frames = len(images)

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            for idx, image_path in enumerate(images):
                print("processing: {}/{} {}".format(idx, num_frames, image_path))
                image = Image.open(image_path)
                # the array based representation of the image will be used later in order to prepare the
                # result image with boxes and labels on it.
                image_np = load_image_into_numpy_array(image)
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)
                # Actual detection.
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                person_idxs = classes == PERSON_CLASS_ID
                boxes = boxes[person_idxs, :]
                classes = classes[person_idxs]
                scores = scores[person_idxs]

                orig_boxes = boxes
                boxes = restore_boxes(boxes, image.size)

                all_scores.append(scores)
                all_boxes.append(boxes)

                if vis:
                    # Visualization of the results of a detection.
                    vis_util.visualize_boxes_and_labels_on_image_array(
                        image_np,
                        np.squeeze(orig_boxes),
                        np.squeeze(classes).astype(np.int32),
                        np.squeeze(scores),
                        category_index,
                        use_normalized_coordinates=True,
                        line_thickness=8)
                    plt.figure(figsize=IMAGE_SIZE)
                    plt.imshow(image_np)
                    plt.show()

    out_name = "person_detections.npz"
    np.savez(out_name, all_boxes, all_scores)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--vis', default=False, action='store_true')
    args, unparsed = parser.parse_known_args()

    person_detect(IMAGES_DIR, args.vis)
