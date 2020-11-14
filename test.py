import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 12239, "name": "Fish fishes from the fish pond", "views": 10939439},
#         {"likes": 39993, "name": "Create APIs with Flask", "views": 11339},
#         {"likes": 1, "name": "Luuk coding", "views": 154554534}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()
# response = requests.get(BASE + "video/6")
# print(response.json())

response = requests.patch(BASE + "video/2", {"views": 19293393939, "likes": 2})
print(response.json())

