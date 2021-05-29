import glob, os

#Deve ser executado dentro da pasta

#Exibe o diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

#Vai armazenar o nome da imagem e a predição
results = open('results.txt', 'w')
#Insere no txt

for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.txt")):
	    title, ext = os.path.splitext(os.path.basename(pathAndFilename))	   
	    data = open(pathAndFilename, "r")	  
	    while(True):
	    	line = data.readline()
	    	if not line:
	    		break
	    	if line:	    		    		
	    		results.write(title + '.png' + ' ' + line.strip() + "\n")	    
