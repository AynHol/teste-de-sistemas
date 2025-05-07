from nota import Nota

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.avaliacao = []
    
    def novaNota(self, nota):
        self.avaliacao.append(Nota(nota))
    
    def modificarNota(self, index, nova_nota):
        if 0 <= index < len(self.avaliacao):
            self.avaliacao[index].nota = nova_nota
    
    def mediaEnd(self):
        if not self.avaliacao:
            return 0.0
        return sum(nota.nota for nota in self.avaliacao) / len(self.avaliacao)