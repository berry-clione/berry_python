import re

RE_ALPHABET = re.compile("^[0-9 .,*]+$") # alphabet, number, space, comma or dot
MAX_CONTENT_LENGTH = 100 * 1024 * 1024 * 1024

DEFAULT_SIMILAR_TOPN = 10
MODEL_PATH = "flaskr/model/enwiki2vec_400d.model"
