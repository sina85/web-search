import urllib.request
from bs4 import BeautifulSoup
import re
import os

function_list = ['ZipArchive::addPattern', 'mb_check_encoding', 'mb_convert_encoding', 'mb_convert_variables', 'mb_parse_str']
def find_func(base):
    a = ['']
    f = urllib.request.urlopen(base)
    soup = BeautifulSoup(f.read(), 'html.parser')
    for i in function_list:
    	s = i + '\([^\)]*\)'
    	a.append(re.findall(s, soup.prettify()))
    return a
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


with open('location', 'r') as f:
    for line in f:
        RecurseLinks(line.strip())
  
# call the initial root web folder
#Manual Example
#RecurseLinks('https://plugins.svn.wordpress.org/newsletter/trunk/')
#RecurseLinks('https://plugins.svn.wordpress.org/wordfence/trunk/')
#RecurseLinks('https://plugins.svn.wordpress.org/powerpress/trunk/')
#RecurseLinks('https://plugins.svn.wordpress.org/embedpress/trunk/')
#RecurseLinks('https://plugins.svn.wordpress.org/elementor/trunk/')
#RecurseLinks('https://plugins.svn.wordpress.org/podcast-subscribe-buttons/trunk/')
