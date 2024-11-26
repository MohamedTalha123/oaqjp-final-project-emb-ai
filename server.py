from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detection():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text_to_analyze = data["text"]
    emotions = emotion_detector(text_to_analyze)
    response = {
        "message": f"For the given sentence, the system's response is: "
                   f"anger: {emotions['anger']}, "
                   f"disgust: {emotions['disgust']}, "
                   f"fear: {emotions['fear']}, "
                   f"joy: {emotions['joy']} and "
                   f"sadness: {emotions['sadness']}. "
                   f"The dominant emotion is {emotions['dominant_emotion']}."
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)