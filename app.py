#---Flask Hello World---#

#import the Flask class from the flask package
from flask import Flask

#create the application object
app = Flask(__name__)

#error handling
app.config["DEBUG"] = True

#use the decorator patter to link the view function to a url
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
	return "Hello, WorldDFGDFH"

#define a view that returns search query as a string
@app.route("/test/<search_query>")
def search(search_query):
	return search_query
#define a view that takes an integer input only
@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "Correct"
#define a view that takes a float value only
@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "Correct"

#define a view that shows you (response, status, headers)
@app.route("/name/<name>")
def index(name):
	if name.lower() == "karan":
		return "Hello, {}!".format(name), 200
	else:
		return "Not Found", 404


#start the development server using the run() method

if __name__ == "__main__":
	app.run()

