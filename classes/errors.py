from enum import Enum
     
class ERROR(Enum):
    OK = 0
    UNAUTHORIZED = 1
    DATABASE_ERROR = 2
    BAD_REQUEST = 3
    INTERNAL_ERROR = 4
    OBJ_NOT_FOUND = 5
    UNKNOWN_DEVICE = 6
    UNABLE_CHANGE = 7
    FAIL_CHANGE = 8
    UNVALID_USER = 9
    INTEGRITY_ERROR = 10
    
class APIError:
    errors = {
        0:'Ok',
        1:'Не авторизован',
        2:'Ошибка базы данных',
        3:'Неверный запрос',
        4:'Внутренная ошибка',
        5:'Объект, указанный в запросе, не найден',
        6:'Неверный идентификатор устройства',
        7:'Невозможно изменить состояние данного устройства',
        8:'Не удалось изменить состояние устройства',
        9:'Неверное имя пользователя или пароль',
        10: 'Ошибка целостности БД',
    }

    def err(e: ERROR):
        return APIError.errors[e if type(e) == int else e.value]
    