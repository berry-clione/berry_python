# -*- coding: utf-8 -*-
import better_exceptions
import colored_traceback.always

from flaskr import app
from flaskr import config

import gensim
from os import path
from os import listdir
from os.path import isfile, join

class Word2Vec:

	def __init__(self):
		self.model_file = app.config["MODEL_PATH"]

		if self.model_file is None:
			raise Exception(file_list)

		# モデルをgensimを用いてロードする
		print("Now loading w2v model file... (((((((((((っ･ω･)っ ﾌﾞｰﾝ")
		self.w2v = gensim.models.Word2Vec.load(
			self.model_file
		)
		# self.w2v = gensim.models.KeyedVectors.load_word2vec_format(
		# 	self.model_file, 
		# 	binary=True
		# 	# unicode_errors="ignore"
		# )
		print("Finished loading! (๑´ڡ`๑)")

	def most_similar(self, word, topn):
		"""
		入力された単語の類似語をtopn件取得
		:param word: 入力単語
		:param topn: 取得上位件数
		:return: 類似語一覧
		"""
		try:
			# 類似語取得
			result = self.w2v.most_similar(word, topn=topn)
			result = [(w, s) for w, s in result]
			# result = [(w, (s + 1.0) / 2.0) for w, s in result]
			return result
		except:
			return None

	# TODO 現在使われていない
	def cosine_similarity(self, word1, word2):
		"""
		単語と単語のCosine Similarityを取得
		:param word1: 単語１
		:param word2: 単語２
		:return: Cosine Similarity
		"""
		return self.w2v.similarity(word1, word2)

class FileUtil:
	def read_file(file_path):
		with open(file_path, "r", encoding="utf-8") as f:
			return f.read() # fulltext

if __name__ == '__main__':
	# 検証用
	wc = Word2Vec()

	print(wc.most_similar("犬", 5))
	# print(wc.cosine_similarity("猫", "犬"))
