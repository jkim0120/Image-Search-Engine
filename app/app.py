from flask import Flask, render_template, request, jsonify
from descriptor.descriptor import Descriptor
from searcher.searcher import Searcher
import os

app = Flask(__name__)

@app.route('/')
def index():
  blah = '103100'
  return render_template('index.html')

@app.route('/search', methods = ['POST'])
def search():
  if request.method == 'POST':
    results_arr = []
    img_path = request.form.get('img')

    try:
      import cv2

      d = Descriptor((8, 12, 3))
      query = cv2.imread('static/images/' + img_path)
      features = d.describe(query)
      searcher = Searcher('index.csv')
      results = searcher.search(features)

      for (score, id) in results:
        results_arr.append({'image': str(id), 'score': str(score)})

      return jsonify(results = (results_arr[::-1][:5]))

    except:
      return jsonify({'sorry': 'Sorry, something went wrong! Please try again.'})

if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)