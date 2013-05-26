# -*- coding: iso-8859-15 -*-
'''
Created on 25/05/2013
@author: sergio




'''

import numpy as np
from numpy import matlib 
import copy
from copy import deepcopy

def foo():
    A = np.array([[2, -1], 
                  [1,  2], 
                  [-1, 1], 
                  [-1, 0], 
                  [0, -1]])
    M = np.array([[1,  0], 
                  [1, -1]])
    b = np.array([4, 9, 3, 0, 0])
    f = np.array([2,5])

    A2 = np.dot(A, M)
    f2 = np.dot(f,M) #- np.dot(f,[0,3])
    b2 = b - np.dot(A,[0,3])
    print 'func obj 2:'
    print f2
    print 'A2: '
    print A2
    print 'b2:'
    print b2
    
    
    M2 = np.array([[-1.0/3,  2.0/3], 
                   [0, 1]])
    
    A3 = np.dot(A2, M2)
    f3 = np.dot(f2,M2)
    b3 = b2 - np.dot(A2,[1,0])
    
    print 'func obj 3:'
    print f3
    print 'A3: '
    print A3
    print 'b3:'
    print b3

def solve():
    # Montar a Matriz de Transorma��o: 
    ''' A Matriz de Transforma��o � a Matriz Identidade de dimenss�o igual ao 
    n�mero de var�aveis, trocando-se a linha correspondente � vari�vel ativa
    pelo sim�trico dos coeficientes da restri��o ativa divididos pelo coeficiente
    da vari�vel ativa na restri��o ativa. '''
    
    # O novo sistema � formado pelas seguintes equa��es.
    
 

    


class SimplexAFS():
    INTEIRO_NULO = -99999
    INTEIRO_MAX = 9999999
    
    def __init__(self, nome_arquivo):
        tableau = np.loadtxt(nome_arquivo)
        qtd_variaveis = len(tableau[0])-1
        self.funcao_objetivo = tableau[0][:qtd_variaveis]
        self.restricoes = tableau[1:,:qtd_variaveis]
        self.valores = tableau[1:,len(tableau[0])-1]
        self.vetor = None

    def __monta_expressao(self,expr,coef,indice):
        sinal = ''
        if coef>=0: sinal = '+'
        return expr + sinal + str(coef)+'*x_'+str(indice)
    
    def imprimir_sistema(self):
    
    
    
        qtd_var = self.qtd_variaveis() 
        qtd_restr = self.qtd_restricoes()
    
        expressao = 'max '
        for i in range(qtd_var):
            expressao = self.__monta_expressao(expressao, self.funcao_objetivo[i], i)
        print 'Fun��o Objetivo:\n\t' + expressao 
        
        print 'Restri��es'
        ''' As restri��es s�o inequa��es definidas a partir da segunda linha.'''
        for i in range(qtd_restr): 
            expressao = ''
            for j in range(qtd_var):
                expressao = self.__monta_expressao(expressao, self.restricoes[i,j], j)
            expressao = expressao + ' <= ' + str(self.valores[i])
            print '\t['+str(i)+']: '+expressao 


    def adicionar_restricao(self,expressao,valor):
        self.restricoes.append(expressao)
        self.valores.append(valor)
        

    def qtd_variaveis(self):
        return len(self.funcao_objetivo)
    
    
    def __adicionar_restricoes_variaveis(self):
        '''
        Complexidade: O(V).
        '''
        # Adicionar a matriz com valor -1 para que fique -x_i <= 0.
        matriz = np.dot(matlib.identity(self.qtd_variaveis()), -1).tolist()
        for linha in matriz:
            self.adicionar_restricao(linha, 0)

    def _montar_matriz_transformacao(self):
        ''' A Matriz de Transforma��o � a Matriz Identidade de dimenss�o igual ao 
        n�mero de var�aveis, trocando-se a linha correspondente � vari�vel ativa
        pelo sim�trico dos coeficientes da restri��o ativa divididos pelo coeficiente
        da vari�vel ativa na restri��o ativa . '''
        
        i_restr_ativ = self.__indice_restr_ativa()
        i_var_ativ = self.__indice_var_ativa()
        
        matriz_T = matlib.identity(self.qtd_variaveis())
        
        coef_ativo = self.restricoes[i_restr_ativ,i_var_ativ]
        
        matriz_T[i_var_ativ] = np.dot(self.restricoes[i_restr_ativ],-1.0/coef_ativo)
        matriz_T[i_var_ativ,i_var_ativ] = -1.0/coef_ativo
       
        return matriz_T

    def __indice_var_ativa(self):
        '''
        Determina a vari�vel de maior impacto.
        @return: Posi��o, come�ando em 0, da vari�vel ativa na lista "self.funcao_objetivo".
        '''
        indice = self.INTEIRO_NULO
        maior = self.INTEIRO_NULO
        for i in range(len(self.funcao_objetivo)):
            if self.funcao_objetivo[i] > maior:
                maior = self.funcao_objetivo[i]
                indice = i
        return indice
    
    def _pode_parar(self):
        '''
        Determina se o crit�rio de parada foi atingido.
        @return: True - crit�rio atingito, False - crit�rio n�o atingido.
        '''
        
        for v in self.funcao_objetivo:
            if v > 0: 
                return False
        return True
        
    def _qtd_restricoes(self):
        return len(self.restricoes)
    
    
    def _satisfaz_restricoes(self):
        for i in range(len(self.restricoes)):
            restr = self.restricoes[i]
            valor = 0

            for x_i in restr:
                valor += x_i
            
    
    
#     def _maximizar(self, i_var_ativa):
#         '''
#         Incrementa a vari�vel ativa at� que alguma restri��o torne-se ativa.
#         @return: �ndice da restri��o ativa.
#         @param i_var_ativa:
#         '''
#         while True:
#             # Incrementa a vari�vel em quest�o.
#             #self.valores[i_var_ativa+self._qtd_restricoes()+1] += 1
#             self.restricoes[i_var_ativa+,i_var_ativa]
#             
#             i_restr_ativa = self._satisfaz_restricoes()
#              
#             if i_restr_ativa > 0:
#                 # Retorna ao valor que satisfaz as restri��es.
#                 self.valores[i_var_ativa+self._qtd_restricoes()+1] -= 1
#                 return i_restr_ativa
        
            
        
        
    
    def copiar(self):
        return copy.deepcopy(self)
    

    def __indice_restr_ativa(self):
        '''
        A restri��o ativa � a restri��o de menor valor.
        @return: �ndice da restri��o ativa na lista "self.restricoes".
        '''
#         min = self.valores.min()
#         return np.where(self.valores == min)[0][0]
        valor = self.INTEIRO_MAX
        i_min = self.INTEIRO_MAX
        for i in range(self.qtd_restricoes()):
            if self.restricoes[i,self.__indice_var_ativa()] !=0 :
                if self.valores[i] > 0:
                    if self.valores[i] < valor:
                        valor = self.valores[i]
                        i_min = i
        return i_min
    
    def qtd_restricoes(self):
        return len(self.restricoes)
    
    
    
    
    def _resolve_sitema_original(self):
        indices = np.where(self.valores==0)
        return  np.linalg.solve(self.copia.restricoes[indices],self.copia.valores[indices])
    
    
    def _imprimir_solucao(self):
        print 'SOLUCAO:'
        expressao = ''
        for i in range(self.qtd_variaveis()):
            expressao = self.__monta_expressao(expressao, self.solucao[i], i)
        print 'Fun��o Objetivo:\n\t' + expressao 
        
        valor = 0
        for i in range(len(self.copia.funcao_objetivo)):
            x = self.copia.funcao_objetivo[i]
            coef = self.solucao[i]
            valor += coef * x
        print 'Valor: ' + str(valor)
    
    
    def resolver(self):
        #self._adicionar_restricoes_variaveis()
        
        # Armazena valores originais para uso no final.
        self.copia = self.copiar()
        
        
        while not self._pode_parar():
            #self.imprimir_sistema()
            
            i_var_ativa = self.__indice_var_ativa()
            i_restr_ativa = self.__indice_restr_ativa()
            
            # Monta a matriz de transforma��o.
            matriz_T = self._montar_matriz_transformacao()
            
            # Transofrma��o dos Valores das Restri��es.
            vetor = [0 for i in range(self.qtd_variaveis())]
            vetor[i_var_ativa] = self.valores[i_restr_ativa]/self.restricoes[i_restr_ativa,i_var_ativa]
            
            
            valores_T =  self.valores - np.dot(self.restricoes, vetor)
            self.valores = valores_T[0:len(valores_T)]
            
            # Transforma��o das Restri��es.
            restricoes_T = np.dot(self.restricoes,matriz_T)
            self.restricoes = restricoes_T.getA()
                        
            # Transforma��o da Fun��o Objetivo.
            funcao_obj_T = np.dot(self.funcao_objetivo,matriz_T)
            self.funcao_objetivo = funcao_obj_T.getA()[0]
            #print self.funcao_objetivo
        
        self.imprimir_sistema() 
        
        self.solucao = self._resolve_sitema_original()
        
        self._imprimir_solucao()
        
        return self.solucao
        
            
if __name__ == '__main__':
#    foo()
#    SimplexAFS('pag_231.txt').resolver()
    SimplexAFS('pag_204.txt').resolver()
#     s.adicionar_restricao([2,-1], 4)
#     s.adicionar_restricao([1,2], 9)
#     s.adicionar_restricao([-1,1], 3)
#     t = s.copiar()
#     s.restricoes = []
#     print s.restricoes
#     print t.restricoes
    