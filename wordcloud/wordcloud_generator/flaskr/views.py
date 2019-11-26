import better_exceptions

from flask import request, redirect, url_for, render_template, flash, send_file
from flaskr import app, controller

title = "Top page"

# Top page ... initially execute index()
@app.route('/')
def index():
	return render_template("index.html", title=title)

# If a user post text in '/post' with POST method, execute get_text()
@app.route('/post', methods=['POST'])
def get_text():
	# corpus = request.args.get('inputtext')
	corpus = request.form['inputtext']
	if corpus:
		controller.wordcloud_generator(corpus)
		output_path = app.config["OUTPUT_PNG_FILE"]
		return send_file(output_path, as_attachment=True)
	else:
		print("Text not found.")

