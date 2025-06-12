import logging


def log1():
    i = 0
    while i < 10:
        logging.warning(i)
        i += 1


def log2():
    logging.debug("Отладка")
    logging.info("Информационный")
    logging.warning("Внимание!")
    logging.error("Ошибка")
    logging.critical("Критическая или фатальная ошибка")


if __name__ == '__main__':
    logging.basicConfig(
        filename="ex2.log",
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        level=logging.CRITICAL
    )
    log2()