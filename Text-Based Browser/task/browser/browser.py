import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def take_args():
    args = sys.argv
    return args[1]


def create_dir(name_dir):
    try:
        os.mkdir(name_dir)
    except FileExistsError:
        pass


def check_url_exist(url):
    return "." in url


def make_correct_url(some_url):
    if some_url.startswith("https://"):
        return some_url
    return "https://" + some_url


def make_file_name(some_name):
    if some_name.startswith("https://"):
        return some_name[8:].replace(".", "_")
    return some_name.replace(".", "_")


def print_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    texts = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
    all_text = ''
    for text in texts:
        if text.name == 'a':
            all_text += Fore.BLUE + text.text
        else:
            all_text += text.text + '/n'
    return all_text


def print_in_file(name_dir, url):

    path = name_dir + "/" + make_file_name(url)

    with open(path, "w") as some_file:
        some_file.write(print_page(url))


def main_f():
    dir_for_pages = take_args()
    create_dir(dir_for_pages)
    stack_of_pages = []

    while True:
        something = input()
        if something == "exit":
            break
        elif something == "back":
            if len(stack_of_pages) > 1:
                print(print_page(stack_of_pages[-2]))
            else:
                pass
        else:
            try:

                path = dir_for_pages + "/" + something
                with open(path, "r") as may_be_file:
                    print(may_be_file.read())
            except FileNotFoundError:
                if check_url_exist(something):
                    correct_url = make_correct_url(something)
                    print(print_page(correct_url))
                    print_in_file(dir_for_pages, correct_url)
                    stack_of_pages.append(make_file_name(correct_url))
                else:
                    print("Error: Incorrect URL")


main_f()
