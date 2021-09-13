# import requests

# from bs4 import BeautifulSoup

# link = input()
# r = requests.get(link)
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.find('h1').text)


# import requests
#
# from bs4 import BeautifulSoup
#
# word = input()
# link = input()
# r = requests.get(link)
# soup = BeautifulSoup(r.content, 'html.parser')
# paragraphs = soup.find_all('p')
# for p in paragraphs:
#     if word in p.text:
#         print(p.text)


# import requests
#
# from bs4 import BeautifulSoup
#
# number = int(input())
# link = input()
#
# r = requests.get(link)
# soup = BeautifulSoup(r.content, 'html.parser')
# subtitles = soup.find_all('h2')
# print(subtitles[number].text)

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


def f(array, left, right, value):
    if left >= right:
        return 0
    elif left == right - 1:
        if array[left] == value:
            return 1
        else:
            return 0
    else:
        middle = (left + right) // 2
        return f(array, left, middle, value) + f(array, middle, right, value)


print(f([1, 2, 3, 3, 3], 0, 4, 3))

print(f([1, 2, 3, 4, 5], 0, 4, 5))

print(f([1, 1, 1, 2, 2], 1, 3, 1))

print(f([2, 2, 2, 2, 2], 0, 4, 2))

print(f([1, 2, 3, 5, 5], 0, 5, 5))
