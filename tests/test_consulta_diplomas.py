from diploma_service.services import ServicoConsultaDiplomas
from diploma_service.models import (
    Diploma, 
    Diplomado
)

def test_consultar_diplomado_por_cpf():
    srv = ServicoConsultaDiplomas()

    returned = srv.consultar_diplomado("1")
    expected = Diplomado(cpf="1", nome="João da Silva", endereco="Rua das Flores, 123, Cidade A")
    
    assert returned == expected
