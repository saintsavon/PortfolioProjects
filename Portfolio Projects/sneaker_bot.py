import requests
import bs4
import random
import webbrowser
import csv
import threading
import RandomHeaders  # File for generating different headers to use on proxies

# INSTRUCTIONS:
# Use this link for getting a sneaker-site specific proxy: https://stormproxies.com/sneaker_proxies.html
# Make sure you have RandomHeaders.csv in your directory


proxies = {
    'http': "",
    'https': "",
}

model_number = 'BB9043'
size_list = [9, 13, 4, 10]
thread_count = 10


# Base URL =  http://www.adidas.com/us/BB9043.html?forceSelSize=BB9043_600
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def do_something():
    print('I just did something')


def url_gen(model, size):
    base_size = 580  # Plus 10 for every half size ex: 7 = 590
    # Base Size is for Shoe Size 6.5
    shoe_size = size - 6.5
    shoe_size = shoe_size * 20
    raw_size = shoe_size + base_size
    shoe_size_code = int(raw_size)
    url = 'http://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(shoe_size_code)
    return url


def check_stock(url):
    raw_html = requests.get(url, headers=RandomHeaders.LoadHeader(), proxies=proxies)
    page = bs4.BeautifulSoup(raw_html.text, "lxml")
    list_of_raw_sizes = page.select('.size-dropdown-block')
    sizes = str(list_of_raw_sizes[0].getText()).replace('\t', '')
    sizes = sizes.replace('\n\n', ' ')
    sizes = sizes.split()
    sizes.remove('Select')
    sizes.remove('size')
    return sizes


def main(model, size):
    url = url_gen(model, size)
    check_stock(url, model)


def sneaker_bot(model, size=None):
    while True:
        try:
            url = 'http://www.adidas.com/us/{}.html?'.format(model)
            sizes = check_stock(url)
            if size is not None:
                # If size is not entered by user
                if str(size) in sizes:
                    do_something()
            else:
                for a in sizes:
                    do_something()
        except:
            pass


threads = [threading.Thread(name='ThreadNumber{}'.format(n), target=sneaker_bot, args=(model_number, size,)) for size in
           size_list for n in range(thread_count)]
for t in threads: t.start()
