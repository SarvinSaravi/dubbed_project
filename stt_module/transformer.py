from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re

tokenizer = AutoTokenizer.from_pretrained("persiannlp/mt5-small-parsinlu-translation_en_fa")

model = AutoModelForSeq2SeqLM.from_pretrained("persiannlp/mt5-large-parsinlu-translation_en_fa")


def run_model(input_string, **generator_args):
    input_ids = tokenizer.encode(input_string, return_tensors="pt")
    res = model.generate(input_ids, **generator_args)
    output = tokenizer.batch_decode(res, skip_special_tokens=True)
    print(output)
    return output


def transform():
    path = '/recognized.txt'
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    text = ''
    for line in lines:
        run_model(line)
        text += ' ' + line
    print(text)
