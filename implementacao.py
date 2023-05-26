class AbstractExpression():
    # Todas as expressões Terminal e Non-Terminal vão implementar um método "interpret"
    @staticmethod
    def interpret():
        """
        O método "interpret" é chamado recursivamente para cada AbstractExpression(Expressão Abstrata)
        """

class Nmr(AbstractExpression):
    # Expressão Terminal

    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)

class Adicionar(AbstractExpression):
    # Expressão Non-Terminal

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} Adicionar {self.right})"

class Subtrair(AbstractExpression):
    # Expressão Non-Terminal

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Subtract {self.right})"

# O Cliente
if __name__ == "__main__":
    
    # A sentença compila com uma gramática simples de Número -> Operador -> Número -> etc.
    SENTENCE = "5 + 4 - 3 + 7 - 2"
    print(SENTENCE)

    # Partiremos a sentença em expressões individuais que irão ser adicionadas a 
    # árvore de sintaxe abstrata(AST) como expressão terminal e não terminal
    TOKENS = SENTENCE.split(" ")
    print(TOKENS)

    # Criando manualmente uma sintaxe de árvore abstrata apartir dos tokens
    AST: list[AbstractExpression] = []  
    AST.append(Adicionar(Nmr(TOKENS[0]), Nmr(TOKENS[2])))  # 5 + 4
    AST.append(Subtrair(AST[0], Nmr(TOKENS[4])))        # ^ - 3
    AST.append(Adicionar(AST[1], Nmr(TOKENS[6])))             # ^ + 7
    AST.append(Subtrair(AST[2], Nmr(TOKENS[8])))        # ^ - 2

    # utiliza a a coluna final do ast como raiz do nó 
    AST_ROOT = AST.pop()

    # Interpreta recursivamente através de toda AST apartir da raiz
    print(AST_ROOT.interpret())

    # Printa a representação da raiz
    print(AST_ROOT)