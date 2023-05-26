from flask import Flask, request
# import openai


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/process-audio', methods=['POST'])
def process_audio():
    audio_uri = request.form.get('audio_uri')
    if audio_uri:
        # Extract the filename from the URI
        filename = os.path.basename(audio_uri)

        # Perform audio processing logic here
        # Example: Print the filename
        print(f"Processing audio file: {filename}")

        return f"Processing audio file: {filename}"
    else:
        return "Invalid request: audio_uri not provided", 400


if __name__ == '__main__':
    app.run()
