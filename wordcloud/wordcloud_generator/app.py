import better_exceptions
import colored_traceback.always

from flaskr import app
# print(app.config)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)