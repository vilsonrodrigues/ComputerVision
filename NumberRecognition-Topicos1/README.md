# Reconhecendo números em imagens

Utilizando uma data base com 1170 exemplos de números escritos a mão. Foi utilizado o OpenCV para extração desses caracteres 
os transformando em vetores de características. Em seguida, foi utilizada a Multi Layer Perceptron (MLP) da biblioteca Keras para 
treinamento. E com um modelo de 50-100-10 neurônios, eu consegui atingir 91% de acurácia. Que, dado os poucos exemplos, e alguns 
caracteres realmente ruins de identificar, acabou sendo um resultado muito satisfatório.
