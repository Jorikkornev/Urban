import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def log_in(self, nickname, password):
        if nickname in self.users and self.users[nickname].password == password:
            self.current_user = self.users[nickname]
        else:
            print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users[nickname] = User(nickname, password, age)
            self.current_user = self.users[nickname]

    def log_out(self):
        self.current_user = None

    def add(self, video):
        if video.title not in self.videos:
            self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, video_title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return
        if video_title not in self.videos:
            print(f"Видео с таким названием не найдено.")
            return
        if self.videos[video_title].adult_mode and self.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу.")
            return
        print(f"Просмотр видео {video_title} начался.")
        for i in range(self.videos[video_title].duration):
            print(f"Просмотр на {i + 1} секунде.")
            time.sleep(1)
        print("Конец видео.")


class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users and self.users[nickname].password == password:
            self.current_user = self.users[nickname]
        else:
            print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users[nickname] = User(nickname, password, age)
            self.current_user = self.users[nickname]
            self.current_user.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, video):
        if video.title not in self.videos:
            self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, video_title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return
        if video_title not in self.videos:
            print(f"Видео с таким названием не найдено.")
            return
        if self.videosvideo_title.adult_mode and self.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу.")
            return
        print(f"Просмотр видео {video_title} начался.")
        for i in range(self.videosvideo_title.duration):
            print(f"Просмотр на {i + 1} секунде.")
            time.sleep(1)
        print("Конец видео.")
