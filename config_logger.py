# Импортируем библиотеку логирования
import logging
from config import LOGGER_API_PATH, LOGGER_FORMAT


# Функция, которая настраивает логгер "api_logger"
def create_logger(app):
    """
    Эта функция создаст и настроит логгер api_logger
    Функцию нужно импортировать и запустить как можно ближе к началу программы
    Получить этот логгер можно будет в любом файле приложения
    с помощью logger = logging.getLogger("api_logger")
    """

    # Создаем логгер
    api_logger = logging.getLogger("api_logger")
    # Настраиваем его на максимальную чувствительность
    api_logger.setLevel(logging.DEBUG)

    # Добавляем обработчик – ошибки будут падать в файл
    api_logger_handler = logging.FileHandler(filename=app.config["LOGGER_API_PATH"])
    api_logger_handler.setLevel(logging.DEBUG)
    api_logger.addHandler(api_logger_handler)

    # Создаем форматер и настраиваем вывод для обработчиков
    api_logger_format = logging.Formatter(app.config['LOGGER_FORMAT'])
    api_logger_handler.setFormatter(api_logger_format)