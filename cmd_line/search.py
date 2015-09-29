from descriptor.descriptor import Descriptor
from searcher.searcher import Searcher
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--index', required = True, help = 'Path to computed computed index')
ap.add_argument('-q', '--query', required = True, help = 'Path to query image')
ap.add_argument('-r', '--result', required = True, help = 'Path to picture database')
args = vars(ap.parse_args())

d = Descriptor((8, 12, 3))

query = cv2.imread(args['query'])
query = cv2.resize(query, (540, 360), cv2.INTER_AREA)
features = d.describe(query)

searcher = Searcher(args['index'])
results = searcher.search(features)

cv2.imshow('Query', query)

for (score, id) in results:
  result = cv2.imread(args['result'] + '/' + str(id))
  result = cv2.resize(result, (540, 360), cv2.INTER_AREA)
  cv2.imshow('Result', result)
  cv2.waitKey(0)