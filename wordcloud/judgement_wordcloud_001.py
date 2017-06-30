import MeCab
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

pos_list = [10, 11, 31, 32, 34]
pos_list.extend(list(range(36,50)))
pos_list.extend([59, 60, 62, 67])
def create_mecab_list(text):
	mecab_list = []
	mecab = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
	mecab.parse("")
	# encoding = text.encode('utf-8')
	node = mecab.parseToNode(text)
	while node:
		if len(node.surface) > 1:
			if node.posid in pos_list:
				morpheme = node.surface
				mecab_list.append(morpheme)
		node = node.next
	return mecab_list

with open("./086064_hanrei_utf8.txt", "r") as file:
	hanrei = file.read()

# d = path.dirname(__file__)
# text = open(path.join(d, './086064_hanrei_utf8.txt')).read()

string = " ".join(create_mecab_list(hanrei))#.decode("utf-8")


fpath = "/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"
wordcloud = WordCloud(
	# background_color="white",
	max_font_size=40,
	relative_scaling=.5,
	# width=900,
	# height=500,
	font_path=fpath
	).generate(string)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
