from flask import Flask, request

app = Flask(__name__)

from flask.json import jsonify



@app.route('/api/v1/users')
def get_user_list():
    return jsonify([
      {'username' : 'zaki'},
      {'username' : 'nube'}
      ])

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    #user = UserService.create(user_data)
user = {'username' : 'zaki'}
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

