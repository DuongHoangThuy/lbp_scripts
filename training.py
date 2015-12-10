import cv2
import cPickle as pickle
import os
import subprocess

positive = pickle.load(open('positive.p', 'rb'))
negative = pickle.load(open('negative2.p', 'rb'))
cascade = 'lbp2y8x'
cv_prefix = '../opencv-restricted2_8/release/bin'

# print len(positive)
# print len(negative)

# # create negatives.dat
# with open('negative2.dat', 'w') as f:
#     for i, neg in enumerate(negative):
#         n = os.path.relpath(neg)
#         f.write(n + '\n')

# #create undistorted info
# with open('positive.dat', 'w') as f:
#     for i, pos in enumerate(positive):
#         img = cv2.imread(pos)
#         height, width, _ = img.shape
#         p = os.path.relpath(pos)
#         f.write(p +' 1 0 0 %d %d\n'%(width, height))

# #create undistorted vec
# subprocess.Popen(['opencv_createsamples',
#                   '-info', 'positive.dat',
#                   '-vec', 'positive20.vec',
#                   '-num', str(len(positive)),
#                   '-w', '20',
#                   '-h', '20'
#                   ]).wait()

subprocess.Popen([os.path.join(cv_prefix, 'opencv_traincascade'),
                  '-data', cascade,
                  '-bg', 'negative2.dat',
                  '-vec', 'positive20.vec',
                  '-featureType', 'LBP',
                  '-numStages', '13',
                  '-numPos', '1200',
                  '-numNeg', '1000',
                  '-minHitRate', '0.999',
                  '-maxFalseAlarmRate', '0.2',
                  '-w', '20',
                  '-h', '20',
                  ]).wait()
#create positive samples
# for i, pos in enumerate(positive[0:1]):
#     pos = os.path.relpath(pos)
#     vec = os.path.basename(pos).split('.')[0] + '.vec'
#     img = cv2.imread(pos)
#     print pos
#     height, width, _ = img.shape
#     pargs = ['createsamples',
#              '-img', pos, 
#              '-num', '10',
#              '-bg', 'negatives.dat',
#              '-vec', vec,
#              '-maxxangle', '0.6',
#              '-maxyangle', '0',
#              '-maxzangle', '0.3',
#              '-maxidev', '100',
#              '-bgcolor', '0',
#              '-bgthresh', '0',
#              '-w', '24',
#              '-h', '24',
#              ]
#     print " ".join(pargs)
#     subprocess.Popen(pargs).wait()

