import logging


def log_info_triangle(text: str):
    """
    Метод логирования с заданными параметрами для записи информации
    """
    FORMAT: str = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
                  'в строке {lineno:03d} функция "{funcName}()" ' \
                  'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(filename='project.log', filemode='w', format=FORMAT, style='{',
                        level=logging.INFO, encoding='utf-8')
    logger = logging.getLogger('Основной файл')
    logger.info(text)


def log_warning_triangle(text: str):
    """
    Метод логирования с заданными параметрами для записи предупреждения
    """
    FORMAT: str = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
                  'в строке {lineno:03d} функция "{funcName}()" ' \
                  'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(filename='project.log', filemode='w', format=FORMAT, style='{',
                        level=logging.WARNING, encoding='utf-8')
    logger = logging.getLogger('Основной файл')
    logger.warning(text)