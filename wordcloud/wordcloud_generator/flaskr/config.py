import re
import os

### MeCab
POS_LIST = [10, 11, 31, 32, 34]
POS_LIST.extend(list(range(36,50)))
POS_LIST.extend([59, 60, 62, 67])
STOP_WORDS = ["する", "ない", "なる", "もう", "しよ", "でき", "なっ", "くっ", "やっ", "ある", "しれ", "思う", "今日", "それ", "これ", "あれ", "どれ", "どの", "NULL", "れる", "なり", "あっ", "できる", "私"]
RE_ALPHABET = re.compile("^[0-9 .,*]+$") # alphabet, number, space, comma or dot
INPUT_TEXT_FILE = "./sample_input.txt"
# OUTPUT_PNG_FILE = "flaskr/static/img/wordcloud.png"
current_dir = os.getcwd()
# OUTPUT_PNG_FILE = "static/img/wordcloud.png"
OUTPUT_PNG_FILE = os.path.join(current_dir, "flaskr/static/img/wordcloud.png")
MAX_CONTENT_LENGTH = 100 * 1024 * 1024 * 1024
