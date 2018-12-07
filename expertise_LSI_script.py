#xoding: utf-8
# Consigo monstar o array de frequencias como indicado no tutorial, mas como usalo agora?
# To fazendo tudo em memoria para facilitar
# Ver como percorrer todos os arquivos java do projeto

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import  os
import tempfile
TEMP_FOLDER = tempfile.gettempdir()

# faz um array com todos os caminhos absolutos dos arquivos .java de um diretorio
def array_of_paths_of_java_files_from_directory(path):
	paths = []
	for dirpath, _, arquivos in os.walk(path):
		for arquivo in arquivos:
			if(len(arquivo.split(".")) >= 2):
				if(arquivo.split(".")[1] == "java"):
					paths.append(dirpath + "/" + arquivo)
	return paths

#MUDE AQUI O CAMINHO DO DIRETORIO
paths = array_of_paths_of_java_files_from_directory("/home/david/Área de Trabalho/homemade-dynamite")

documents = []

for path in paths:
	documents.append(open(path).read())

from gensim import corpora
from gensim import models


# pensar na possibilidade de uso de syntax... ou usar o texto somente
#import processa
#documents = [processa.process('public class Teste { public static void main(String[] args) { int a = 10; int b = 20; System.out.println(a+b);  } } '),
#             processa.process('public class Turma { public static void main(String[] args) { float c;  double d = 20.0; double d2 = 30.0; System.out.println(a+b);  } } '),
#             processa.process(open('Aluno.java').read())]



#Essa forma de limpar o texto ehd  realmente a mais adequada??             
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

#texts = [[token for token in text if frequency[token] > 1] for text in texts]

texts = [[token for token in text] for text in texts]


from pprint import pprint  # pretty-printer
#pprint(texts)


dictionary = corpora.Dictionary(texts)
#print(dictionary)

#print(dictionary.token2id)


corpus = [dictionary.doc2bow(text) for text in texts]
#for c in corpus:
    #print(c)

m = models.LsiModel(corpus, id2word=dictionary, num_topics=4)
c_lsi = m[corpus]

print("___________________________________________________________________________________________________")

for i in range(len(c_lsi)):
    print(paths[i].split("/")[-1])
    print(c_lsi[i])
    
linhas = []
import csv
with open("analysis-result.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        linhas.append(line[0:])
        
        
#OS DADOS TÃO AQUI, MAS NÃO CONSEGUI ENTENDER O CALCULO !!!!    
print("______________________________________________________________________________________________________")
print()
for i in range(len(paths)):
	file_name = paths[i].split("/")[-1]
	for linha in linhas:
		file_name_tsv = linha[1].split("/")[-1]
		if(file_name_tsv == file_name):
			print(linha[0]  + "   " + linha[1] + "   " + linha[2])
			print(c_lsi[i])
    
