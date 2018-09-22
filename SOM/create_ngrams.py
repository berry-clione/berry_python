# coding: utf-8
import better_exceptions

import os
import pandas
import nltk
import csv

# img_paths.append(os.path.abspath(os.path.join(root_dir, cl_name, img_name)))

current_working_dir = os.getcwd()
training_data_dir = "training_data"

training_data_file_list = os.listdir(
	os.path.join(current_working_dir, training_data_dir)
	)
print("training_data_file_list : ", len(training_data_file_list))

training_data_name_list = [e.split(".")[0] for e in training_data_file_list]
pandas.DataFrame(training_data_name_list).to_csv(
	"output_data/training_data_name_list.csv", index=None, header=None
	)

##############
### Read file.
def read_text(training_data):
	print(training_data)
	with open("/".join([training_data_dir , training_data]), "r") as f:
		text = f.read()
	return text

training_data_text_list = [read_text(s) for s in training_data_file_list]
print("training_data_text_list : ", len(training_data_text_list))
# print(training_data_text_list[2])

##############

def create_ngrams(text):
	ngrams = nltk.ngrams(list(text), 1)
	# ngrams = nltk.ngrams(list(text), 2)
	fd = nltk.FreqDist(ngrams)
	fd_list = [[k,v] for k, v in fd.items()]
	return fd_list

ngrams_list = [create_ngrams(sn_text) for sn_text in training_data_text_list]
print(ngrams_list[4])
print("ngrams_list : ", len(ngrams_list))
print("ngrams_list[0] : ", len(ngrams_list[0]))
print("ngrams_list[1] : ", len(ngrams_list[1]))

# print(ngrams_list[0])
print("====== created ngrams =======")

##############

def create_ngrams_basic_vector(ngrams_list):
	pre_ngrams_basic_vector = [sn_ngram for ngrams_sn_list in ngrams_list for [sn_ngram, c] in ngrams_sn_list]
	ngrams_basic_vector = list(set(pre_ngrams_basic_vector))
	return ngrams_basic_vector

ngrams_basic_vector = create_ngrams_basic_vector(ngrams_list)
print("ngrams_basic_vector : ", len(ngrams_basic_vector))

##############

def create_ngrams_matrix(ngrams_basic_vector, ngrams_list):
	matrix = [[0 for i in range(len(ngrams_basic_vector))] for j in range(len(ngrams_list))]
	# print(len(matrix))
	for i, ngrams_sn_list in enumerate(ngrams_list):
		for [sn_ngram, c] in ngrams_sn_list:
			matrix[i][ngrams_basic_vector.index(sn_ngram)] = c
	return matrix

ngrams_matrix = create_ngrams_matrix(ngrams_basic_vector, ngrams_list)
print("ngrams_matrix : ", len(ngrams_matrix))
print("ngrams_matrix[0] : ", len(ngrams_matrix[0]))
print("ngrams_matrix[1] : ", len(ngrams_matrix[1]))
print("=== created ngrams matrix ===")

with open("output_data/ngrams_matrix.csv", "w") as f:
	writer = csv.writer(f, lineterminator="\n")
	writer.writerows(ngrams_matrix)

















