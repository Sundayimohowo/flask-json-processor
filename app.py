import json, os
from flask import Flask, request, jsonify, send_file


app = Flask(__name__)

def parse_fields(filename, item):
    first_frame_number = int(item['FirstFrameNumber']) if isinstance(item['FirstFrameNumber'], str) else item[
        'FirstFrameNumber']
    last_frame_number = int(item['LastFrameNumber']) if isinstance(item['LastFrameNumber'], str) else item[
        'LastFrameNumber']

    first_frame = filename.replace('%07d', f"{first_frame_number:07d}")
    last_frame = filename.replace('%07d', f"{last_frame_number:07d}")
    return {
        "FirstFrame": first_frame,
        "LastFrame": last_frame
    }


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
                output.append(parse_fields(filename, item))
        elif isinstance(input_data, dict):
            filename = input_data['Filename']
            output = parse_fields(filename, input_data)
        else:
            output = {}

        # Save output to a JSON file
        output_file_path = os.path.join("static/output.json")
        with open(output_file_path, 'w') as f:
            json.dump(output, f)

        return send_file(output_file_path, as_attachment=True, download_name='output.json', mimetype='application/json')


if __name__ == '__main__':
    app.run()
