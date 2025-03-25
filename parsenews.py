import json
from rich import print_json

# names = ["aimable", "James", "mari"]
# number = len(names)
# print(number)


with open('news.json', "r") as file:
    content = json.load(file)
    number = len(content['articles'])
    print(f"articles_retrieved: {number}")
    # i = 0
    # for item in content['articles']:
    #     print(item['content'])
    print(content['articles'][10]['content'])
    print(content['articles'][10]['url'])


    