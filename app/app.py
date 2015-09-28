from flask import Flask, render_template, request, jsonify
from descriptor.descriptor import Descriptor
from searcher.searcher import Searcher
import os

app = Flase(__name__)
index = os.path.join(os.path.dirname(__file__), 'index.csv')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/search', methods['POST'])
def search():
  if request.method == 'POST':
    results_arr = []
    img_url = request.form.get('img')

    try:
      d = Descriptor((8, 12, 3))

      from skimage import io
      import cv2
      query = io.imread(img_url)
      query = (query * 255).astype('uint8')
      (r, g, b) = cv2.split(query)
      query = cv2.merge([b, g, r])
      features = d.describe(query)

      searcher = Searcher(index)
      results = searcher.search(features)

      for (score, id) in results:
        results_arr.append({
          'image': str(id),
          'score': str(score)
        })

      return jsonify(results=(results_arr[::-1][:3]))

    except:
      jsonify({'sorry': 'Sorry, something went wrong! Please try again.'})

if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)