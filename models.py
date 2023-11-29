class Diplomado:

    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self._diplomas = []

    def to_json(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "endereco": self.endereco
        }
    
    def diplomas(self):
        return self._diplomas
    
    def add_diploma(self, diploma):
        if (not diploma in self.diplomas()):
            self._diplomas.append(diploma)

class Diploma:
    def __init__(self, id, curso, data_conclusao):
        self.id = id
        self.curso = curso
        self.data_conclusao = data_conclusao
        self._diplomado = None

    def to_json(self):
        return {
            "id": self.id,
            "curso": self.curso,
            "data_conclusao": self.data_conclusao,
            "diplomado": self.diplomado().to_json()
        }
    
    def diplomado(self):
        return self._diplomado
    
    def add_diplomado(self, diplomado):
        self._diplomado = diplomado
