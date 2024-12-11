from flask import Flask, request, jsonify
import tempfile
import os
from werkzeug.utils import secure_filename
from recognizeOffender import recognize_from_image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = 'searchPerson'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Save the uploaded image
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Run recognition
    try:
        result = recognize_from_image(file_path)
        if result:
            return jsonify({
                'status': 'success',
                'message': 'Known offender recognized',
                'offender_details': result
            })
        else:
            return jsonify({'status': 'success', 'message': 'No offender recognized'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(file_path)  

if __name__ == '__main__':
    app.run(debug=True)