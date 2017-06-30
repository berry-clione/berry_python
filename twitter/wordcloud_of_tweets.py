import MeCab
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

stop_words = ["する", "ない", "なる", "もう", "しよ", "でき", "なっ", "くっ", "やっ", "ある", "しれ", "思う", "今日"]
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
		# for sw in stop_words:
		# 	if node.surface == sw:
		# 		node = node.next
		if len(node.surface) > 1:
			if node.posid in pos_list:
				morpheme = node.surface
				mecab_list.append(morpheme)
		node = node.next
	return mecab_list

text_tweet = []
with open("./tweets.csv", "r") as file:
	reader = csv.reader(file)
	for tweets_text in reader:
		tweets_list = csv.reader(tweets_text)
		for ele in tweets_list:
			if "228" in ele[0]:
				break
			if "@" in ele[3]:
				continue
			if "RT" in ele[3]:
				continue
			text_tweet.append(ele[3])
		# text_tweet = [ele[3] for ele in tweets_list]
text = "".join(text_tweet)
print(text)

string = " ".join(create_mecab_list(text))#.decode("utf-8")

fpath = "/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"
wordcloud = WordCloud(
	background_color="black",
	stopwords=set(stop_words),
	max_font_size=56,
	relative_scaling=.4,
	width=500,
	height=300,
	font_path=fpath
	).generate(string)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("./wordcloud.png")