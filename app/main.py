from flask import Flask, request, render_template
from utils.preprocess import preprocess_image
import cv2
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['document']
        path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(path)

        processed = preprocess_image(path)
        result_path = path.replace(".jpg", "_processed.jpg")
        cv2.imwrite(result_path, processed)

        return render_template('index.html', original=path, processed=result_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
