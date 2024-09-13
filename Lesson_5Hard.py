import time

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        if any((user.nickname == login and user.password == hash(password)) for user in self.users):
            self.current_user = login
            print('Пользователь', {login}, 'вошел в систему.')
        else:
            print('Пользователь не найден или неверный пароль.')

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print('Пользователь', {nickname}, 'уже существует.')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print('Пользователь', {nickname}, 'зарегистрировался и вошел в систему.')

    def log_out(self):
        self.current_user = None
        print('Пользователь вышел из системы.')

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, video_title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((video for video in self.videos if video.title.lower() == video_title.lower()), None)
        if video:
            print('Воспроизведение видео:', {video.title})

            if video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                return

            for i in range(video.duration):
                print(i + 1, end = ' ', flush=True)
                time.sleep(1)

            print("Конец видео")
            self.current_user.time_now = 0
        else:
            print("Видео не найдено.")


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname

    def contains(self, item):
        return item in self.nickname

class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title

    def contains(self, search_word):
        return search_word in self.title.lower()


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')