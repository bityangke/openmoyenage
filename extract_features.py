import sys
import h5py
import cv2
import torch
import torch.nn.functional as F
import torchvision

model = torchvision.models.vgg16(pretrained = True).features
model.cuda()

features = []
filenames = os.listdir(sys.argv[1])

for filename in filenames:
	img = torch.as_tensor(cv2.imread(os.path.join(sys.argv[1], filename))).float().cuda()
	img = (img - torch.tensor([0.485, 0.456, 0.406]).type_as(batch)) / torch.tensor([0.229, 0.224, 0.225]).type_as(batch)
	img = img[None, None, ...].transpose(1, -1).squeeze(-1)
	img = F.upsample(img, (480, 640), mode = 'bilinear')
	output = model(img)
	features.append(output.view(output.size(1), -1).mean(-1))
	
h = h5py.File('extract_features.h5', 'w')
h['features'] = torch.stack(features).numpy()
h.create_dataset('filenames', (len(filenames), 1), 'S50', [filename.encode('ascii') for filename in filenames])
