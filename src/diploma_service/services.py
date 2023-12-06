from diploma_service.daos import DiplomaDAO, DiplomadoDAO
from diploma_service.tracebility import Trace

class ServicoConsultaDiplomas:

    def consultar_diplomas(self, cpf):
        diploma_dao = DiplomaDAO()
        return diploma_dao.find_diplomas_by_cpf(cpf)
    
    @Trace.TestFor("RF-123")
    def consultar_diplomado(self, cpf):
        diplomado_dao = DiplomadoDAO()
        return diplomado_dao.find_by_cpf(cpf)
    
class ReqTracer:

    @staticmethod
    def matrix():
        return Trace.matrix()