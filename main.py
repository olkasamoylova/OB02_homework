class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id        # Приватный атрибут для ID
        self.__name = name              # Приватный атрибут для имени
        self.__access_level = 'user'    # Приватный атрибут для уровня доступа

    # Методы для получения данных пользователя, так как по умолчанию они приватные и напрямую извне не заберешь инфо
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level
