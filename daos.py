from models import *

class BancoDeDados:

    def __init__(self):

        self.diplomados = {
            "1": {
                "cpf": "1",
                "nome": "João da Silva",
                "endereco": "Rua das Flores, 123, Cidade A"
            },
            "2": {
                "cpf": "2",
                "nome": "Maria Oliveira",
                "endereco": "Avenida Central, 456, Cidade B"
            },
            "3": {
                "cpf": "3",
                "nome": "Carlos Pereira",
                "endereco": "Praça Principal, 789, Cidade C"
            }
        }
        
        self.diplomas = {
            "1": {
                "id": "1",
                "curso": "Engenharia da Computação",
                "data_conclusao": "2020-06-15",
                "diplomado": "1"
            },
            "2": {
                "id": "2",
                "curso": "Administração",
                "data_conclusao": "2021-12-20",
                "diplomado": "2"
            },
            "3": {
                "id": "3",
                "curso": "Direito",
                "data_conclusao": "2019-11-10",
                "diplomado": "3"
            },
            "4": {
                "id": "4",
                "curso": "Medicina",
                "data_conclusao": "2022-05-30",
                "diplomado": "1"
            },
            "5": {
                "id": "5",
                "curso": "Arquitetura",
                "data_conclusao": "2018-08-25",
                "diplomado": "2"
            }
        }

class DiplomaDAO:

    def find_by_id(self, id):
        """
        Faz uma busca no Banco e retorna uma model
        """
        # Uma entidade é um registro bruto no banco de dados
        # Exemplo de entidade: {'id': '1', 'curso': 'Engenharia da Computação', 'data_conclusao': '2020-06-15', 'diplomado': '1'}
        entidade = BancoDeDados().diplomas[id]

        id = entidade["id"]
        curso = entidade["curso"]
        data_conclusao = entidade["data_conclusao"]
        diplomado_id = entidade["diplomado"]

        diploma_model = Diploma(id, curso, data_conclusao)

        diplomado_model = DiplomadoDAO().find_by_cpf(diplomado_id)

        diploma_model.add_diplomado(diplomado_model)

        return diploma_model

    def find_diplomas_by_cpf(self, cpf_diplomado):
        bd = BancoDeDados()
        lst_diplomas = [
            self.find_by_id(diploma_info["id"])
                for diploma_info in bd.diplomas.values()
                    if diploma_info["diplomado"] == cpf_diplomado
        ]
        return lst_diplomas

class DiplomadoDAO:

    def find_by_cpf(self, cpf):
        """
        Faz uma busca no Banco e retorna uma model
        """
        # Uma entidade é um registro bruto no banco de dados
        # Exemplo de entidade:
        entidade = BancoDeDados().diplomados[cpf]

        cpf = entidade["cpf"]
        nome = entidade["nome"]
        endereco = entidade["endereco"]

        diplomado_model = Diplomado(cpf, nome, endereco)

        return diplomado_model