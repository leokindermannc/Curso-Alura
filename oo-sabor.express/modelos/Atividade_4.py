class Livro:
    livros = []
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._ativo = False
        Livro.livros.append(self)

    def __str__(self):
        return f'{self.titulo}, {self.autor}, {self.outra_informacao}'
    
    

    
    @classmethod
    def listar_livros(cls):
        print(f'{'Nome do Titulo'.ljust(25)} | {'Nome do Autor'.ljust(25)} | {'ano'.ljust(25)} | {'Status'}')
        for Livro in cls.livros:
            print(f'{Livro.titulo.ljust(25)} | {Livro.autor.ljust(25)} | {str(Livro.ano).ljust(25)} | {Livro.ativo}')

    @classmethod
    def verificar_disponibilidade(cls):
        ano=input('DIgite o ano que voce quer procurar')
        lista_encontrados = []
        for livro in cls.livros:
            if str(livro.ano)==ano:
                lista_encontrados.append(livro)
        if lista_encontrados:
            for livro in lista_encontrados:
                print(f'titulo:{livro.titulo}, autor{livro.autor}, ano{livro.ano}')
        else:
                print('livro nao encontrado')


    @property
    def ativo(self):
        return 'Disponivel' if self._ativo else False
    
    def alternar_estado(self):
        self._ativo = not self._ativo

        
  
Livro_historia = Livro('Pedra mitinho', 'Machado de Assis', 2002)
Livro.listar_livros()
Livro.verificar_disponibilidade()      