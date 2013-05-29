SIMPLEX
Esta implementa��o foi desenvolvida por Anna Carolina, Fernando Menucci e S�rgio Rodrigues, como trabalho da disciplina Estrutura de Dados e Algoritmos, do curso de Mestrado em Modelagem Matem�tica da Informa��o da Funda��o Get�lio Vargas, Rio de Janeiro, 2013.

A implementa��o do algoritmo de Simplex baseia-se na t�cnica de programa��o linear apresentada no livro Algorithms, de Christos Papadimitriou et all.

O algoritmo est� preparado para maximizia��o, portanto para us�-lo em minimiza��o � necess�rio converter a fun��o objetivo pelo sim�trico.

ARQUIVOS:
 - SimplexAFS.py: Classe SimplexAFS que resolver o sistema descrito um arquivo texto.
 - simplex.py: M�dulo para execu��o em linha de comando.
 
 COMO USAR:
 Para executar o Simplex utilize o seguinte comando:
 python simplex.py <nome_do_arquivo>
 
 Caso o nome do arquivo contenha espa�os, coloc�-lo entre aspas.
 Caso o arquivo n�o exista ou seja mal formatadao, um erro ser� emitido.
 
 O arquivo � do tipo texto e deve conter a seguinte estrutura de exemplo:
 
 1.a linha: Coeficientes da fun��o objetivo, seguido pelo valor 0.
 2.a linha em diante: Coeficientes das restri��es, seguido pelo valor  das restri��es.
 
 Coment�rios no arquivo s�o aceitos desde que iniciados com o caracter "#".
 
 Veja um exemplo abaixo:
2 5	0 #Funcao objetivo. Determina as variaveis. Completar 0.
2 -1 4	#1.a inequacao
1 2 9	#2.a inequacao
-1 1 3 	#3.a inequacao

Fim do exemplo. 