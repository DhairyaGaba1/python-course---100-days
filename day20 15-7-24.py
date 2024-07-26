#Code for video 86

# a = True
# print(a:=False)

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

# foods = list()
# while (food := input("What food do you like?: ")) != "quit":
#     foods.append(food)

#Code for video 87

# import shutil

# # Copying a file
# shutil.copy("src.txt", "dst.txt")

# # Copying a directory
# shutil.copytree("src_dir", "dst_dir")

# # Moving a file
# shutil.move("src.txt", "dst.txt")

# # Deleting a directory
# shutil.rmtree("dir")

#Code for video 89

# import requests 
# from bs4 import BeautifulSoup
# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
# r = requests.get(url)
# # print(r.text)


# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#   print(heading.text)
# # url = "https://jsonplaceholder.typicode.com/posts"

# # data = {
# #     "title": 'harry',
# #     "body": 'bhai',
# #     "userId": 12,
# #   }
# # headers =  {
# #     'Content-type': 'application/json; charset=UTF-8',
# #   }
# # response = requests.post(url, headers=headers, json=data)

# # print(response.text)

#Code for video 91

# def my_generator():
#     for i in range(5):
#         yield i

# gen = my_generator()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# for j in gen:
#     print(j)

#Code for video 92

# import functools
# import time

# @functools.lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n*5

# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")

# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")

