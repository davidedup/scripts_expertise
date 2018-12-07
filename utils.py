#coding: utf-8
import os

def array_of_paths_of_java_files_from_directory(path):
	paths = []
	for dirpath, _, arquivos in os.walk(path):
		for arquivo in arquivos:
			if(arquivo.split(".")[1] == "java"):
				paths.append(dirpath + "/" + arquivo)
	
