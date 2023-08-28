import json, os
from flask import Flask, request, jsonify, send_file


app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and file.filename.endswith('.json'):
        input_data = json.load(file)

        # Process the input_data
        if isinstance(input_data, list):
            output = []
            for item in input_data:
                filename = item['Filename']
                first_frame_number = item['FirstFrameNumber']
                last_frame_number = item['LastFrameNumber']

                first_frame = filename.replace('%07d', f"{first_frame_number:07d}")
                last_frame = filename.replace('%07d', f"{last_frame_number:07d}")

                output.append({
                    "FirstFrame": first_frame,
                    "LastFrame": last_frame
                })
        elif isinstance(input_data, dict):
            output = {}
            filename = input_data['Filename']

            first_frame_number = input_data['FirstFrameNumber']
            last_frame_number = input_data['LastFrameNumber']

            first_frame = filename.replace('%07d', f"{first_frame_number:07d}")
            last_frame = filename.replace('%07d', f"{last_frame_number:07d}")

            output["FirstFrame"] = first_frame
            output["LastFrame"] = last_frame
        else:
            output = {}

        # Save output to a JSON file
        output_file_path = os.path.join("static/output.json")
        with open(output_file_path, 'w') as f:
            json.dump(output, f)

        return send_file(output_file_path, as_attachment=True, download_name='output.json', mimetype='application/json')


if __name__ == '__main__':
    app.run()
