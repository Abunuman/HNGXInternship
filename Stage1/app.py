from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')


    # Get current day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # Get current UTC time
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Validate UTC time within +/- 2 hours
    current_utc_time = datetime.datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%SZ')
    valid_time_range = datetime.timedelta(hours=2)
    utc_time_now = datetime.datetime.utcnow()

    if abs(current_utc_time - utc_time_now) > valid_time_range:
        return jsonify({"status": "Error", "message": "UTC time validation failed"}), 400

    # GitHub URL of the file being run
    github_file_url = 'https://github.com/Abunuman/HNGXInternship/blob/main/Stage1/app.py'  # Replace with your GitHub URL

    # GitHub URL of the full source code
    github_source_url = 'https://github.com/Abunuman/HNGXInternship'  # Replace with your GitHub URL

    # Response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "current_utc_time": current_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_source_url": github_source_url,
        "status_code": "200"
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
