import hashlib


class User:
    def __init__(self, name, password, age):
        """Класс пользователя
        Атрибуты: name - str, password - str, age - int
        Методы: hash_password - принимает password, возвращает его hash значение
        """
        self.name = name
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __repr__(self):
        return f'self.name = {self.name}, self.password = {self.password}, self.age = {self.age}'


    def hash_password(self):
        if self.password: # Проверка на сложный пароль?
            self.password = hash(self.password)
        return self.password


class Video:
    def __init__(self, title, duration, time_now, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    """Класс UrTube
    Атрибуты: users - список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    Методы: log_in: принимает username, password, ищет username в users, сравнивает hash пароля из users с password,
    если все значения совпадают - current_user = user
    register - принимает три аргумента: username, password, age, если username есть в users, выводит сообщение
    "Пользователь {nickname} уже существует". После успешной регистрации вызывается log_in
    log_out - current_user = None

    """
    def __init__(self, users, videos, current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, username, password):
        pass

    def register(self,nickname, password, age):
        pass

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self, *args):
        for arg in args:
            if isinstance(arg, Video):
                self.videos.append(arg)
        return self.videos

    def get_videos(self, find_key):
        pass

    def watch_video(self, find_key):
        pass

if __name__ == '__main__':
    u1 = User('Vasia', '1243Ydff', 23)
    u2 = User('Nastia', 'sj6rdge', 16)
    print(u1)
    print(u2)
