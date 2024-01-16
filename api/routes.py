from flask import request, jsonify
import api.controller
from app import app


@app.route('/add_photo', methods=['POST'])
def add_photo_route():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400

    url = data.get('url')
    if not url:
        return jsonify({"error": "Missing 'url' in JSON data"}), 400

    api.controller.add_photo(url)
    return jsonify({"message": "Photo added successfully"})

@app.route('/get_all_photos', methods=['GET'])
def get_all_photos_route():
    photos = api.controller.get_all_photos()
    photo_list = [{"id": photo.id, "url": photo.url} for photo in photos]
    return jsonify({"photos": photo_list})