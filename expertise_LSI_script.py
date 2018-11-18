# Consigo monstar o array de frequencias como indicado no tutorial, mas como usalo agora?
# To fazendo tudo em memoria para facilitar
# Ver como percorrer todos os arquivos java do projeto

# Mudar caminho do arquivo aqui
def make_array_from_file():
	with open("./Aluno.java") as file_class:
		file_lines = file_class.readlines()
	return file_lines


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


import  os
import  tempfile
TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))


from gensim import corpora


documents = make_array_from_file() 

             
             
#Essa forma de limpar o texto é realmente a mais adequada??             
# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]

from pprint import pprint  # pretty-printer
pprint(texts)


dictionary = corpora.Dictionary(texts)
print(dictionary)

print(dictionary.token2id)


corpus = [dictionary.doc2bow(text) for text in texts]
for c in corpus:
    print(c)


