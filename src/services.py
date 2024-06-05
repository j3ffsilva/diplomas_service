from daos import DiplomaDAO, DiplomadoDAO
from tracebility import Trace

class ServicoConsultaDiplomas:

    @Trace.REQ("RF-123")
    def consultar_diplomas(self, cpf):
        diploma_dao = DiplomaDAO()
        return diploma_dao.find_diplomas_by_cpf(cpf)
    
    @Trace.REQ("RF-124")
    def consultar_diplomado(self, cpf):
        diplomado_dao = DiplomadoDAO()
        return diplomado_dao.find_by_cpf(cpf)