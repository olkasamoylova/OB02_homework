class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id        # Приватный атрибут для ID
        self.__name = name              # Приватный атрибут для имени
        self.__access_level = 'user'    # Приватный атрибут для уровня доступа, в основном классе задает обычный уровень доступа (как всем)

    # Методы для получения данных пользователя, так как по умолчанию они приватные и напрямую извне не заберешь инфо
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__admin_access_level = 'admin'  # Приватный атрибут для особого уровня доступа администратора

    # Метод для добавления пользователя
    def add_user(self, user_list, user):
        if self.get_access_level() == 'admin':
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему.")
        else:
            print("У вас, коллега, недостаточно прав для добавления пользователя.")

    # Метод для удаления пользователя
    def remove_user(self, user_list, user):
        if self.get_access_level() == 'admin':
            if user in user_list:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален из системы.")
            else:
                print("Пользователь не найден в системе.")
        else:
            print("У вас, коллега, недостаточно прав для добавления пользователя.")


