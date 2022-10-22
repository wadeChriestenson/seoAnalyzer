import requests
from bs4 import BeautifulSoup

print('SEO Scan')
user_choice = input('Enter name of website to scan \n')
# URL = "https://w3schools.com/"
URL = 'https://' + user_choice
page = requests.get(URL)
# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")


def meta_tag(web_site):
    site_name = web_site.find('meta', property='og:site_name')
    metaTag = web_site.find("meta", property='og:description')
    print('Results from SEO analyzer scan: \n ***', site_name['content'], '***')
    print(metaTag["content"] if metaTag else "No meta title given")
    print('Meta tag character count:', len(metaTag['content']))


def h_tags(web_site):
    h1 = web_site.find_all("h1")
    h2 = web_site.find_all("h2")
    h3 = web_site.find_all("h3")
    h4 = web_site.find_all("h4")
    h5 = web_site.find_all("h5")
    h6 = web_site.find_all("h6")
    print('and has the following amount tags.')
    print(' H1 -', len(h1), '\n',
          'H2 -', len(h2), '\n',
          'H3 -', len(h3), '\n',
          'H4 -', len(h4), '\n',
          'H5 -', len(h5), '\n',
          'H6 -', len(h6), '\n')
    return


def word_count(web_site):
    capital = web_site.text.capitalize()
    words = capital.split()
    print('and has', len(words), 'total words.')
    word_freq = set(words)
    print('Keywords on page:')
    for key_words in word_freq:
        if key_words.isalpha() and words.count(key_words) > 5 and len(key_words) > 5:
            print(key_words.capitalize(), '-', words.count(key_words))
    return


meta_tag(soup)
h_tags(soup)
word_count(soup)
