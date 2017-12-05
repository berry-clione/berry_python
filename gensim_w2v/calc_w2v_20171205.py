import better_exceptions
from gensim.models import word2vec
import sys
import cython

file_name = "./wiki_neologd_w2v_20171204_02.txt"
model = word2vec.Word2Vec.load(file_name) 

# def wordAddition(pos1, pos2): 
#     result = model.most_similar(positive = [pos1,pos2], topn = 1) 
#     print pos1 , '+' , pos2 , '=' 
#     for r in result: 

def word_subtraction(pos, neg): 
	result = model.most_similar(positive=pos, negative=neg, topn = 10)
	for r in result: 
		print(r)

pos = sys.argv[1]
neg = sys.argv[2]

word_subtraction(pos, neg)
