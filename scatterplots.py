
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def visualize_scatter(data_2d, label_ids, figsize=(20,20)):
	plt.figure(figsize=figsize)
	plt.grid()
	
	nb_classes = len(np.unique(label_ids))
	
	for label_id in np.unique(label_ids):
		plt.scatter(data_2d[np.where(label_ids == label_id), 0],
					data_2d[np.where(label_ids == label_id), 1],
					marker='o',
#					 color= plt.cm.Set1(label_id / float(nb_classes)),
					linewidth='1',
					alpha=0.8,
					label=label_id)
	plt.legend(loc='best')


def visualize_scatter_with_images(X_2d_data, images,layer, saveFig=True,figsize=(45,45), image_zoom=1):
	fig, ax = plt.subplots(figsize=figsize)
	artists = []
	for xy, i in zip(X_2d_data, images):
		x0, y0 = xy
		img = OffsetImage(np.array(i), zoom=image_zoom)
		ab = AnnotationBbox(img, (x0, y0), xycoords='data', frameon=False)
		artists.append(ax.add_artist(ab))
	ax.update_datalim(X_2d_data)
	ax.autoscale()
	fig.suptitle('tSNE of '+layer+' activations', fontsize=60)	
	# plt.title('tSNE of feature layers')
	plt.show()
	return fig