from descriptor.descriptor import Descriptor
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--data', required = True, help = 'Path to the directory of images')
ap.add_argument('-i', '--index', required = True, help = 'Path to store computed index')
args = vars(ap.parse_args())

desc = Descriptor((8, 12, 3))

output = open(args['index'], 'w')

for img_path in glob.glob(args['data'] + '/*.jpg'):
  id = img_path[img_path.find('/') + 1:]
  img = cv2.imread(img_path)

  features = desc.describe(img)

  features = [str(f) for f in features]
  output.write('%s, %s\n' % (id, ','.join(features)))

output.close()