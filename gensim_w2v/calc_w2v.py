import better_exceptions
from gensim.models import word2vec
# import sys
import cython

file_name = "./model.txt"
# model = word2vec.Word2Vec.load(file_name) ### _pickle.UnpicklingError: could not find MARK
model = word2vec.KeyedVectors.load_word2vec_format(file_name)

# def wordAddition(pos1, pos2):
#     result = model.most_similar(positive = [pos1,pos2], topn = 1)
#     print pos1 , '+' , pos2 , '='
#     for r in result:

def word_subtraction(pos, neg):
	pos_list = [pos]
	neg_list = [neg]
	result = model.most_similar(positive=pos_list, negative=neg_list, topn = 50)
	# for i, r in enumerate(result):
	# 	print(i+1, r[0])
	return [r[0] for r in result]

# pos = sys.argv[1]
# neg = sys.argv[2]
pos_neg_list = [
	["hoge", "fuga"]
]

for pos_neg in pos_neg_list:
	print("".join([pos_neg[0], " - ", pos_neg[1], "|"]))
	print(":-|")
	for i, r in enumerate(word_subtraction(pos_neg[0], pos_neg[1])):
		print("".join([str(i+1), ". ", r, "|"]))
	print()
