# -*- coding: utf-8 -*-
import better_exceptions
import colored_traceback.always

from flaskr import app
from flaskr import config

import MeCab
from os import path
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re

class nlp:
	def omit_signal(text):
		# print(text)
		omitted_signal = text\
			.replace("　", " ")\
			.replace("\u3000", " ")\
			.replace("\"", " ")\
			.replace("\n", " ")\
			.replace("\t", " ")\
			.replace("  ", " ")
		return omitted_signal

	def create_mecab_list(text_list):
		mecab_list = []
		mecab = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
		mecab.parse("")
		# encoding = text.encode('utf-8')
		for text in text_list:
			node = mecab.parseToNode(text)
			while node:
				# [品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音]
				# 忙しく  形容詞,自立,*,*,形容詞・イ段,連用テ接続,忙しい,イソガシク,イソガシク
				# morpheme = node.surface
				morpheme = node.feature.split(",")[6]
				if app.config["RE_ALPHABET"].match(morpheme):
					node = node.next
					continue
				if morpheme in app.config["STOP_WORDS"]:
					node = node.next
					continue
				if len(morpheme) > 0: # > 1:
					if len(morpheme) == 1:
						morpheme += "_"
					if node.posid in app.config["POS_LIST"]:
						mecab_list.append(morpheme)
						# print(morpheme, end=", ")
				node = node.next
		return mecab_list

	def create_wordcloud(morphemes):
		# fpath = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf" # Ubuntu
		fpath = "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc" # Mac OS X Mojave
		wordcloud = WordCloud(
			background_color="whitesmoke",
			# background_color="black",
			collocations=False,
			stopwords=set(app.config["STOP_WORDS"]),
			# max_font_size=60,
			max_font_size=80,
			relative_scaling=.5,
			# width=500,
			width=800,
			# height=250,
			height=500,
			font_path=fpath
			).generate(morphemes)
		plt.figure()
		plt.imshow(wordcloud)
		plt.axis("off")
		wordcloud.to_file(app.config["OUTPUT_PNG_FILE"])
		# plt.show()

class file_util:
	def read_file(file_path):
		with open(file_path, "r", encoding="utf-8") as f:
			return f.read() # fulltext

############

def wordcloud_generator(corpus):
	# corpus = file_util.read_file(INPUT_TEXT_FILE)
	normalized_corpus = nlp.omit_signal(corpus)
	morphemes_list = nlp.create_mecab_list([normalized_corpus])
	nlp.create_wordcloud(" ".join(morphemes_list))
