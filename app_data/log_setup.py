import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from app_data.definitions import logging_level, logfile_location, logfile_name
from os import sep, path, mkdir

if logfile_location.endswith(sep):
    logfile_location = logfile_location[0:-1]
if not path.exists(logfile_location):
    logfile = logfile_name
else:
    logfile = logfile_location + sep + logfile_name
    
file_handler = RotatingFileHandler(logfile)
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s pid: %(process)d: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
logging.basicConfig(level=logging_level)
file_handler.setLevel(logging_level)

'''
Дадим краткие характеристики уровней логирования:
    Debug (10): самый низкий уровень логирования, предназначенный для отладочных сообщений, для вывода диагностической информации о приложении.
    Info (20): этот уровень предназначен для вывода данных о фрагментах кода, работающих так, как ожидается.
    Warning (30): этот уровень логирования предусматривает вывод предупреждений, он применяется для записи сведений о событиях, на которые программист обычно обращает внимание. Такие события вполне могут привести к проблемам при работе приложения. Если явно не задать уровень логирования — по умолчанию используется именно warning.
    Error (40): этот уровень логирования предусматривает вывод сведений об ошибках — о том, что часть приложения работает не так как ожидается, о том, что программа не смогла правильно выполниться.
    Critical (50): этот уровень используется для вывода сведений об очень серьёзных ошибках, наличие которых угрожает нормальному функционированию всего приложения. Если не исправить такую ошибку — это может привести к тому, что приложение прекратит работу.
'''