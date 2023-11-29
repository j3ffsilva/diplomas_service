from daos import DiplomaDAO, DiplomadoDAO

class ServicoConsultaDiplomas:

    def consultar_diplomas(self, cpf):
        diploma_dao = DiplomaDAO()
        return diploma_dao.find_diplomas_by_cpf(cpf)