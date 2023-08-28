# Flask JSON Processor

This Flask application serves an endpoint that accepts a JSON file, processes it, and saves the output as another JSON file.

## Requirements
- Python 3.11
- Flask

## Installation
- Clone this repository
- Build the Docker image: `docker build -t flask-app .`

## Running the App
- Run the Docker container: `docker run -p 5000:5000 flask-app`
- The app will be accessible at `http://localhost:5000/`
- 
## How to Run the App
1. Clone this repository to your local machine.
2. Navigate to the repository folder in the terminal.
3. Install the required packages using `pip install -r requirements.txt`.
4. Run the app using `python app.py`.

## Endpoint
- POST `/process`: Accepts a multipart/form-data POST request with a JSON file under the key 'file'. It processes the JSON content and saves the output as a JSON file.

## Testing
To run the unit tests, use `python -m unittest discover -s tests -p '*_test.py'`.

## Output
The processed data will be saved as a JSON file in the `/static` directory. The API will return a downloadable json named output.json
