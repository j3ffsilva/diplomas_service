from services import ServicoConsultaDiplomas
from models import (
    Diploma, 
    Diplomado
)
from tracebility import Trace

@Trace.TestFor("RF-124")
def test_consultar_diplomas_por_cpf():
    srv = ServicoConsultaDiplomas()

    returned = srv.consultar_diplomas("1")

    expected_diplomado = Diplomado(
        cpf="1",
        endereco="Rua das Flores, 123, Cidade A",
        nome="João da Silva"
    )
    
    expected_diploma_1 = Diploma(
        id="1",
        curso="Engenharia da Computação",
        data_conclusao="2020-06-15"
    )
    expected_diploma_1.add_diplomado(expected_diplomado)
    
    expected_diploma_4 = Diploma(
        id="4",
        curso="Medicina",
        data_conclusao="2022-05-30"
    )
    expected_diploma_4.add_diplomado(expected_diplomado)

    expected = [expected_diploma_1, expected_diploma_4]

    assert returned == expected
