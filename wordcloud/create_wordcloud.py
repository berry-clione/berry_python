# -*- coding: utf-8 -*-
import colored_traceback.always
import better_exceptions

import MeCab
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import re

### MeCab
pos_list = [10, 11, 31, 32, 34]
pos_list.extend(list(range(36,50)))
pos_list.extend([59, 60, 62, 67])
stop_words = ["する", "ない", "なる", "もう", "しよ", "でき", "なっ", "くっ", "やっ", "ある", "しれ", "思う", "今日", "それ", "これ", "あれ", "どれ", "どの", "NULL", "れる", "なり", "あっ"]
re_alphabet = re.compile("^[a-zA-Z0-9 .,*]+$") # alphabet, number, space, comma or dot
text_file = "./sample_input.txt"
output_png = "./wordcloud.png"

class nlp:
	def omit_signal(text):
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
				if re_alphabet.match(morpheme):
					node = node.next
					continue
				if morpheme in stop_words:
					node = node.next
					continue
				if len(morpheme) > 0: # > 1:
					if len(morpheme) == 1:
						morpheme += "_"
					if node.posid in pos_list:
						mecab_list.append(morpheme)
						# print(morpheme, end=", ")
				node = node.next
		return mecab_list

	def create_wordcloud(morphemes):
		# fpath = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf" # Ubuntu
		fpath = "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc" # Mac OS X Mojave
		wordcloud = WordCloud(
			background_color="whitesmoke",
			collocations=False,
			stopwords=set(stop_words),
			# max_font_size=60,
			max_font_size=80,
			relative_scaling=.5,
			width=500,
			height=250,
			# height=500,
			font_path=fpath
			).generate(morphemes)
		plt.figure()
		plt.imshow(wordcloud)
		plt.axis("off")
		wordcloud.to_file(output_png)
		plt.show()

class file_util:
	def read_file(file_path):
		with open(file_path, "r", encoding="utf-8") as f:
			return f.read() # fulltext

############

corpus = file_util.read_file(text_file)
normalized_corpus = nlp.omit_signal(corpus)
morphemes_list = nlp.create_mecab_list([normalized_corpus])
nlp.create_wordcloud(" ".join(morphemes_list))
