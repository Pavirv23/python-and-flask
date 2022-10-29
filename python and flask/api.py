# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
api = Flask(__name__)

@api.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})
@api.route('/home/<int:num>', methods = ['GET'])
def disp(num):

	return jsonify({'data': num**2})
# driver function
if __name__ == '__main__':

	api.run(debug = True)

