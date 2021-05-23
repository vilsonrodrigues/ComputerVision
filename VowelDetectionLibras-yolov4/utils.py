import glob, os

#Exibe o diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

#Cria os arquivos .txt para armazenar a lista de imagens de treino e dev
file_train = open('train.txt', 'w')
file_dev = open('dev.txt', 'w')
#Insere no txt
#O código foi construído para png, caso for aproveitar e seja outro formato, basta alterar
for path in ['dev','train']:
	for pathAndFilename in glob.iglob(os.path.join(current_dir+'/'+path, "*.png")):
	    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
	    if path == 'dev':
	        file_dev.write("data-detection/" + "/" + path +'/' + title + '.png' + "\n")
	    elif path == 'train':
	        file_train.write("data-detection" + "/" + path +'/' + title + '.png' + "\n")	      