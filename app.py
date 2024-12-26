from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name': 'English'}, {'name': 'Python'}, {'name': 'Java'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'it works'})

@app.route('/lang', methods=['GET'])
def get_languages():
    return jsonify(languages)

@app.route('/lang', methods=['POST'])
def add_one():
    # Check if the request contains JSON data
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    # Extract the name from the JSON data
    name = request.json.get('name')
    
    # Validate the input
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    
    # Create a new language entry
    language = {'name': name}
    
    # Add to the languages list
    languages.append(language)
    
    # Return the created language with a 201 status code
    return jsonify({'language': language}), 201

@app.route('/lang/<string:name>', methods=['GET'])
def get_language_by_name(name):
    # Using a loop for clarity
    for language in languages:
        if language['name'].lower() == name.lower():  # Case-insensitive comparison
            return jsonify({'language': language})
    
    return jsonify({'error': 'Language not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)
