#! usr/bin/python3

# codewars.com/kata/55c45be3b2079eccff00010f/
def order(sentence):
    if sentence == "":
        return ""
    else:
        return " ".join(sorted([word for word in sentence.split(" ")], key=lambda x: [char for char in x if char.isdigit()]))
