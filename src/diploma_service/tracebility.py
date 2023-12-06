class Trace:
    """
    Esta classe é usada para rastrear a relação entre métodos de código e requisitos específicos.
    Ela permite criar uma matriz de rastreabilidade que liga os métodos aos códigos de requisitos.
    """

    # Dicionário para armazenar a relação entre métodos e códigos de requisitos.
    requirements_dict = {}

    # Dicionário para armazenar a relação entre testes e códigos de requisitos.
    test_requirements_dict = {}

    @staticmethod
    def REQ(req_code):
        """
        Método decorador para anotar métodos com um código de requisito específico.
        :param req_code: O código do requisito a ser associado ao método.
        :return: Um decorador que anota o método com o código de requisito.
        """
        def decorator(func):
            # Armazena o nome do método e o código do requisito associado no dicionário.
            Trace.requirements_dict[func.__name__] = req_code
            return func
        return decorator

    @staticmethod
    def TestFor(req_code):
        """
        Método decorador para anotar testes com um código de requisito específico.
        :param req_code: O código do requisito associado ao teste.
        :return: Um decorador que anota o teste com o código de requisito.
        """
        def decorator(func):
            if req_code in Trace.test_requirements_dict:
                Trace.test_requirements_dict[req_code].append(func.__name__)
            else:
                Trace.test_requirements_dict[req_code] = [func.__name__]
            return func
        return decorator

    @staticmethod
    def get_req_code(func):
        """
        Retorna o código do requisito associado a um método.
        :param func: A função cujo código de requisito é desejado.
        :return: O código do requisito se existir, ou "None" se não for encontrado.
        """
        return Trace.requirements_dict.get(func.__name__, "None")

    @staticmethod
    def matrix():
        """
        Gera uma matriz de rastreabilidade mapeando métodos aos códigos de requisitos.
        :return: Um dicionário representando a matriz de rastreabilidade.
        """
        matrix = {}
        # Itera sobre os itens do dicionário para construir a matriz de rastreabilidade.
        for method, req_code in Trace.requirements_dict.items():
            matrix[method] = req_code
        return matrix

    @staticmethod
    def test_coverage_report():
        """
        Gera um relatório de cobertura de testes para requisitos.
        :return: Uma representação string do relatório.
        """
        report = ""
        for req, tests in Trace.test_requirements_dict.items():
            report += f"Requisito {req} é coberto pelos testes: {', '.join(tests)}\n"
        return report