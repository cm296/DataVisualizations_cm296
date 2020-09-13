import os
from PIL import Image
import numpy as np


def load_images(PathToImg):
	images = []
	labels = []
	conditions = listdir(PathToImg)
	condition_features = {}
	for c in conditions:
		c_name = c.split('/')[-1]
		stimuli = listdir(c)
		example_stim = stimuli[0]
		image = Image.open(example_stim).convert('RGB')
		image = image.resize((150, 150))
		images.append(image)
		labels.append(c.split('/')[-1])

	labels = np.array(labels)
	return images, labels




def listdir(dir, path=True):
    files = os.listdir(dir)
    files = [f for f in files if f != '.DS_Store']
    files = sorted(files)
    if path:
        files = [os.path.join(dir, f) for f in files]
    return files