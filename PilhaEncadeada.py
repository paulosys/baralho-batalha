class PilhaException(Exception):
    def __init__(self,mensagem,metodo=''):
        super().__init__(mensagem)
        self.metodo = metodo

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def insereProximo(self, dado):
        if (self.prox == None):
            self.prox = Node(dado)

    def getProximo(self):
        return self.prox

    def __str__(self):
        return str(self.data)

    def temProximo(self):
        return self.prox != None

class Pilha:
    def __init__(self):
        self.__head = None
        self.__tamanho = 0
        self.__base = None
        
    def estaVazia(self) -> bool:
        return self.__head == None

    def tamanho(self) -> int:
        return self.__tamanho

    def elemento(self, posicao) -> Node:
        try:
            assert posicao > 0 and posicao <= self.__tamanho
 
            cursor = self.__head
            contador = 1
            while(cursor != None and contador < posicao ):
                contador += 1
                cursor = cursor.prox

            return cursor.dado
                
        except TypeError:
            raise PilhaException('Digite um número inteiro referente ao elemento desejado')
        except AssertionError:
            raise PilhaException(f'O elemento {posicao} NAO existe na pilha de tamanho {self.__tamanho}')
        except:
            raise

    def busca(self, valor):
        cursor = self.__head
        contador = 1

        while( cursor != None):
            if cursor.dado == valor:
                return contador           
            cursor = cursor.prox
            contador += 1

        raise PilhaException(f'Valor {valor} nao esta na pilha','busca()')
        
    def empilhar(self, valor):
        novoNode = Node(valor)
        novoNode.prox = self.__head
        if self.__base == None:
            self.__base = novoNode
        self.__head = novoNode
        self.__tamanho += 1
        
    def desempilhar(self) -> Node:
        if not self.estaVazia():
            dado = self.__head.dado
            self.__head = self.__head.prox
            self.__tamanho -= 1
            return dado
        raise PilhaException('A pilha está vazia')
        
    def enfileirar_embaixo(self, valor):
        '''
        Método utilizado para enfileirar abaixo da base da pilha
        os jogadores guardarem as cartas ganhas durante o jogo;
        
        Basicamente, o método enfileira o valor na base da pilha
        criando uma nova base, e a base antiga aponta para a nova base.
        '''
        novoNode = Node(valor)
        
        if self.__base == None:
            self.__base = novoNode
            
        self.__base.prox = novoNode 
        self.__base = novoNode

    def imprimir(self):
        print(self.__str__())    
        
    def limpar_pilha(self):
        self.__head = None
        self.__base = None
        self.__tamanho = 0
        
    def __str__(self):
        print()
        no = self.__head
        while no:
            print(f'{no.dado}')
            no = no.prox
        print()
        return ''