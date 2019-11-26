import better_exceptions

from flask import request, redirect, url_for, render_template, flash, send_file
from flaskr import app, controller, config

from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_bootstrap import Bootstrap

title = "Top page"
DEFAULT_SIMILAR_TOPN = app.config["DEFAULT_SIMILAR_TOPN"]
w2v = controller.Word2Vec()

# NavBarのセットアップとFlask用Bootstrapのセットアップ
nav = Nav()
nav.init_app(app)
bootstrap = Bootstrap(app)

# 類似語検索トップページ
@app.route('/')
def similar():
	title = "類似語検索"
	top = DEFAULT_SIMILAR_TOPN
	return render_template('similar.html', alert="", word="", top=top, title=title)

# 類似語検索
@app.route('/similar/search', methods=['GET'])
def similar_search():
	title = "類似語検索"
	alert = None
	word = request.args.get('word')
	topn = int(request.args.get('top')) if request.args.get('top') else DEFAULT_SIMILAR_TOPN
	result = None

	if w2v:
		result = w2v.most_similar(word, topn)
		if result is None:
			alert = "単語 「{}」 はモデルに存在しません。".format(word)

	return render_template('similar.html', alert=alert, word=word, result=result, top=topn, title=title)
