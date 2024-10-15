from modelos.Atividade_4 import Livro

Livro_historia = Livro('Pedra mitinho', 'Machado de Assis', 2002)

def main():
    
    Livro.listar_livros()
    Livro.verificar_disponibilidade()
    

if __name__== '__main__':
    main()