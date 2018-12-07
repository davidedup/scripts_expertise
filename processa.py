import itertools
import os
import pprint
import re
import sys
import zipfile

import chardet

import javalang


def error(msg):
    sys.stderr.write("error" + msg + "\n")

def use_path(path):
    return 'P' * len(path)

def no_path(path):
    return ''


CONFIG = { 'path': no_path }


# https://stackoverflow.com/questions/2319019/using-regex-to-remove-comments-from-source-files
def remove_comments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile('".*?"',re.DOTALL ) ,"" ,string) # remove all occurance strings from string
    string = re.sub(re.compile('\s',re.DOTALL ) ,"" ,string) # spaces
    string = re.sub(re.compile('\d',re.DOTALL ) ,"" ,string) # digits
    return string


def process(raw):
    content = []
    #code = raw.decode(encoding).encode('ascii', 'ignore')
    code = raw
    try:
        tree = javalang.parse.parse(code)
        for path, node in tree:
            content.append(CONFIG['path'](path) + node.__class__.__name__)
    except Exception:
        code = raw.decode(encoding)
        content.extend(remove_comments(code).split())
    return ' '.join(content)
