import os
import yaml
from bs4 import BeautifulSoup

working_directory = "resources/Text/"

files = os.listdir(working_directory)

# data = ""
#
# for item in files:
#     with open(f"{working_directory}{item}") as fp:
#         soup = BeautifulSoup(fp, 'html.parser')
#         data +=soup.text
#
# with open("data.yaml", "w") as f:
#     yaml.dump(data, f, encoding="utf-8", allow_unicode=True)

with open("data.yaml", "r") as f:
    data = yaml.safe_load(f)

data = data.lower()

data = [item.strip(' ,.!?:;"()0123456789-/\\«»') for item in data.split()]
data = [item.strip(' «»,.!?:;"()0123456789-/\\') for item in data]

gen = filter(lambda x: len(x) > 2, data)
data = list(gen)

with open("data_words.yaml", "w") as f:
     yaml.dump(data, f, encoding="utf-8", allow_unicode=True)


with open("data_words.yaml", "r") as f:
     data = yaml.safe_load(f)
uniques = set(data)
calculated = dict()
maximum = 1
for word in uniques:
    calculated[word] = data.count(word)
    if calculated[word] > maximum:
        maximum = calculated[word]

# data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}

with open("result_words.yaml", "w") as f:
     yaml.safe_dump(calculated, f, encoding="utf-8", allow_unicode=True, sort_keys =False)