from scamp import *
from data import *
from functions import *

scale = get_scale()
question = gen_question(scale, 3)

while True:
    n = input()
    if n == "0":
        break
    if n == "2":
        print(question["names"])
    else:
        play_question(question)