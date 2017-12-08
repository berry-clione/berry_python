import better_exceptions
from gensim.models import word2vec
import sys
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
	result = model.most_similar(positive=pos_list, negative=neg_list, topn = 10)
	for r in result:
		print(r)

pos = sys.argv[1]
neg = sys.argv[2]
# pos = ["アメリカ"]
# neg = ["日本"]
print(model[pos])
print(model[neg])

print(pos, " - ", neg, " = ")
word_subtraction(pos, neg)
