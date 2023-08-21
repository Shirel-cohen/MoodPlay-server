from flask import Flask, request, jsonify
from deepface import DeepFace

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def analyze_mood():
#     face_analysis = DeepFace.analyze(img_path="sad.jpg")
#     return face_analysis
#
#
# app.run(host = '0.0.0.0')

@app.route('/', methods=['POST'])
def analyze_mood():
    if 'image' not in request.files:
        return "No image provided", 400

    image_file = request.files['image']

    if image_file.filename == '':
        return "No selected image", 400

    image_path = "temp_image.jpg"  # Temporary image path
    image_file.save(image_path)

    face_analysis = DeepFace.analyze(img_path=image_path)

    # You might want to format the response as needed
    # For example: return jsonify({"mood": face_analysis["dominant_emotion"]})
    return jsonify(face_analysis)

app.run(host='0.0.0.0')