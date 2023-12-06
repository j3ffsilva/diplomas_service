from diploma_service.tracebility import Trace

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    Hook para ser chamado após a conclusão de todos os testes.
    """
    # Chama a função para gerar o relatório de cobertura de testes
    report = Trace.test_coverage_report()
    terminalreporter.write('\n\nRelatório de Cobertura de Teste por Requisito:\n')
    terminalreporter.write(report)