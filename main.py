from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

user_service = UserService(FileDbService)


@app.route('/api/v1/users')
def get_user_list():
    return jsonify(user_service.get_list())

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    user = UserService.create(user_data)
    return jsonify(user)

@app.route('/api/v1/users', methods=['PUT'])
def update_user():
    #user = UserService.update(user_data)
user = {'username' : 'zaki'}
return jsonify(user)

@app.route('/api/v1/users', methods=['DELETE'])
def create_user():
    #user = UserService.delete(user_data)
    return None, 204

@app.route('/api/v1/users/<user_id>')
def get_user(user_id):
    return jsonify(
      {'username' : 'zaki'}
      )

@app.route('/api/v1/posts')
def get_posts_list():
    return jsonify([
        {'title' : 'mi titulo 1'},
        {'title' : 'im titulo 2'}
    ])

