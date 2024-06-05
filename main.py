from src.tracebility import Trace
from src.services import *

def main():
    
    srv = ServicoConsultaDiplomas()

    # Simula uma chamada para registrar os requisitos
    srv.consultar_diplomas("1")

    # Gerar e imprimir a matriz de rastreabilidade
    print("Matriz de Rastreabilidade:")
    print(Trace.matrix())

if __name__ == "__main__":
    main()