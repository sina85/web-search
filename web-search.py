import urllib.request
from bs4 import BeautifulSoup
import re

def find_func(base):
    #ZipArchive::addPattern()
    #scandir
    f = urllib.request.urlopen(base)
    soup = BeautifulSoup(f.read(), 'html.parser')
    a = re.findall('ZipArchive::addPattern\([^\)]*\)', soup.prettify());
    b = re.findall("mb_check_encoding\([^\)]*\)", soup.prettify());
    c = re.findall("mb_convert_encoding\([^\)]*\)", soup.prettify());
    d = re.findall("mb_convert_variables\([^\)]*\)", soup.prettify());
    e = re.findall("mb_parse_str\([^\)]*\)", soup.prettify());
    l = a + b + c + d + e
    return l
def RecurseLinks(base):
    f = urllib.request.urlopen(base)
    soup = BeautifulSoup(f.read(), 'html.parser')
    for anchor in soup.find_all('a'):
        href = anchor.get('href')
        if (href.startswith('/') or href.endswith('../') or href.startswith('http')):
            continue
            #print ('skip, most likely the parent folder -> ' + href)
        elif (href.endswith('/')):
            #print ('crawl -> [' + base + href + ']')
            RecurseLinks(base + href) # make recursive call w/ the new base folder
        elif (href.endswith('.php')):
            l = find_func(base + href)
            print ('[-] ' + base + href)
            if (l):
                print ('[+] ' + base + href)
                print ('--->')
                print (*l, sep =' ,') # save it to a list or return 
                print ('----')

# call the initial root web folder
RecurseLinks('https://plugins.svn.wordpress.org/newsletter/trunk/')
RecurseLinks('https://plugins.svn.wordpress.org/wordfence/trunk/')
RecurseLinks('https://plugins.svn.wordpress.org/powerpress/trunk/')
RecurseLinks('https://plugins.svn.wordpress.org/embedpress/trunk/')
RecurseLinks('https://plugins.svn.wordpress.org/elementor/trunk/')
RecurseLinks('https://plugins.svn.wordpress.org/podcast-subscribe-buttons/trunk/')
