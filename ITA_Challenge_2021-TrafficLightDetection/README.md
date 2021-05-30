## Trabalho que faturou o primeiro lugar no ITA Challenge 2021

### Detecta em tempo real com a YOLOv4 os 4 estados dos semáforos: green, yellow, red e off.

Vídeos gerados com a rede

[Detecção em São Paulo - Parte 1](https://www.youtube.com/watch?v=i2XTW9elPns)

[Detecção em São Paulo - Parte 2](https://youtu.be/8WeWgPLnqoc)


### Métricas

Essas são as métricas do classificador na etapa de validação

class_id = 0, name = green, ap = 84.55%   	 (TP = 55, FP = 14) 

class_id = 1, name = yellow, ap = 0.00%   	 (TP = 0, FP = 2) 

class_id = 2, name = red, ap = 72.27%   	 (TP = 47, FP = 7) 

class_id = 3, name = off, ap = 73.50%   	 (TP = 9, FP = 4) 

A baixa quantidade de amostras yellow acabou prejudicando o desempenho do modelo nessa classe
