# -*- coding: utf-8 -*-
import better_exceptions
import colored_traceback.always

import logging
from gensim.models import word2vec

# input_file = 'data/word2vec/enwiki_normalized_all.txt'
input_file = 'data/word2vec/dumps_enwiki/normalized/enwiki_normalized_1000000.txt'
output_model = 'flaskr/model/enwiki2vec_400d.model'

# 学習
def train(input_path, output_path, 
		size=400, min_count=5, window=10, skipgram=0, 
		sample=1e-4, hs=0, negative=5, iter=15):
	# 進捗表示用
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	# 一行ごとに学習するために、コーパスをLineSentenceに格納する
	sentences = word2vec.LineSentence(input_path)
	# 学習
	model = word2vec.Word2Vec(sentences, 
		sg=skipgram, size=size, min_count=min_count, window=window, 
		sample=sample, hs=hs, negative=negative, iter=iter)
	# 学習結果を出力する
	model.save(output_path)

# 追加学習（単語の数も更新される）
def retrain(input_path, output_path, output_full_path, model_path):
	# 進捗表示用
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	# 事前学習したモデルを読み込む
	model = word2vec.Word2Vec.load(model_path)
	# 一行ごとに学習するために、コーパスをLineSentenceに格納する
	sentences = word2vec.LineSentence(input_path)
	# 単語の追加
	model.build_vocab(sentences, update=True)
	# 学習
	model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)
	# 学習結果を出力する
	model.save(output_full_path)
	# model.wv.save_word2vec_format(output_path)

class Word2VecUtil:
	"""Word2Vecの主な機能を集めたクラス"""

	def __init__(self, model_path):
		self.model = word2vec.Word2Vec.load(model_path)

	def most_similar(self, word, topn=5):
		return self.model.most_similar(word, topn=topn)

	def get_vector(self, word):
		return self.model[word]

	def cosine_similarity_matrix(self, x_words, y_words):
		result = {}

		vocab = self.model.wv.vocab

		for x in x_words:
			if x in vocab:
				r = {}
				for y in y_words:
					if y in vocab:
						r[y] = self.model.wv.similarity(x, y)
				result[x] = r

		return result

##################
# class Word2VecTrain:
# 	def __init__(self):
# 		# wiki2vec作成用
# 		self.wiki_model = config.get_property('word2vec', 'Wiki2VecModel')
# 		# 任意のコーパスでword2vec作成用
# 		self.word2vec_model = config.get_property('word2vec', 'Word2VecModel')
# 		self.word2vec_full_model = config.get_property('word2vec', 'Word2VecFullModel')

# 	def train(self, input_path, size=400, min_count=5, window=10, skipgram=1, sample=1e-4, hs=0, negative=5, iter=15):
# 		word2vec.train(input_path=input_path, output_path=self.wiki_model, size=size,
# 					min_count=min_count, window=window,
# 					skipgram=skipgram, sample=sample, hs=hs, negative=negative, iter=iter)

# 	def retrain(self, input_path):
# 		word2vec.retrain(input_path=input_path, output_path=self.word2vec_model,
# 						output_full_path=self.word2vec_full_model, model_path=self.wiki_model)

# if __name__ == '__main__':
# 	w2v = Word2VecTrain()
# 	w2v.train()
# 	w2v.retrain()
#####################

train(input_file, output_model, 
	size=400, 
	min_count=5, 
	window=10, 
	skipgram=0, 
	sample=1e-4, 
	hs=0, 
	negative=5, 
	iter=1
	)




