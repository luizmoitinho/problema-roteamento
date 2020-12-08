# Problema Roteamento

Projeto produzido utilizando Python para resolver o problema do roteamento, presente nas redes de computadores. Tem como objetivo, 
dentre os host presentes na aplicação, buscar a melhor rota a ser traçada com base no seu custo (busca de custo uniforme).

--

## Intalação de bibliotecas:
1. Tkinter
>  pip install tk-tools

2. SimpleGUI
>  pip install PySimpleGUI
--
## Executando a aplicação
1. Baixe o projeto do github (.zip ou clone)
2. Acesse a pasta raiz do projeto
3. Execute o arquivo Main.py pelo terminal:
  > python(3) May.py
  > O número 3 refere-se a versão do python, pode variar a depender como se encontra o python em sua máquina.
3.1 Execute o terminal via VsCode:
  > Abra o projeto no VsCode e pressione o icone de start, presente no canto superior direito do editor.
 
## Aplicação
1. Após feito os passos anterirores, deverá ser exibido em tela as inteface gráfica da aplicação.
2. Informe o nome contindo dentro um host (imagem do PC) no campo de origem
3. Informe o nome contindo dentro um host (imagem do PC) no campo de destino
4. Pressione em enviar.
5. A melhor rota deverá ser traçada em verde e o custo total será exibido no canto inferior direito da aplicação.
6. Repita o passo 1, para mais testes.

## Validação
1. Para validar se a rota traçada é a melhor, basta somar os números presente nas semi-retas que podem ser traçadas saindo da origem e chegando no destino

## Algoritmo
1. O caminho é traçado utilizando a busca de custo uniforme, que possui como g(x) os custos presentes nas semi-retas, importantes para traçar a solução ótima, neste caso.
2. Para conseguir o caminho percorrido para chegar ao destino, cada nó que é expandido possui uma lista que contém todos os nós que foram visitados para que pudesse chegar até ali.
Ou seja, cada um possui uma lista propria do caminho percorrido até o momento da expansão daquele nó.
