#Melhorar o tratamento das palavras, muitas não não consideras devido a outros caracteres

def read_file():
    with open('./Aluno.java', 'r') as lyrics_file:
        file_lines = lyrics_file.readlines()
    return file_lines


def is_key_word(word):
    #mudar isso por um array
    if(word == "implements" or word == "extends" or word == "@Test" or word == "extends Exception" or word ==  
       "extends RuntimeException" or word == "Exception" or word == "Exception" or word == "RuntimeException" 
       or word == "throws" or word ==  "try" or word == "catch" or word == "IOException" or word == "File"
       or word == "abstract"):
        return True
    return False
    
lines = read_file()

frequency = {}


for line in lines:
    words = line.split(" ");
    for word in words:
        word = word.strip()
        if is_key_word(word):
            if (frequency.get(word) == None):
                frequency[word] = 1
            else:
                frequency[word] = frequency[word] + 1
print(frequency)
