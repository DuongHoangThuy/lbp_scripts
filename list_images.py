import cv2
import glob2
import sys
import os
import cPickle as pickle

dir = "./"

images = []
for type in ['jpg', 'png']:
    search = os.path.abspath(os.path.join(dir, '**/*.' + type))
    print search
    images.extend(glob2.glob(search))

pickle.dump(images, open(os.path.join(dir, 'images.p'), 'wb'))

images = pickle.load(open(os.path.join(dir, 'images.p'), 'rb'))

with open('images.txt', 'w') as f:
    for image in images:
        f.write(image + '\n')
