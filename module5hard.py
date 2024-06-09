import time
# '-------------------------------------------------------------------------------'
class User:
    def __init__(self, name, password, age):
        self.name = name
        self.password = hash(password)
        self.age = age
#        print(self.name, ';', self.password, ';', self.age)

    def curr_user(self):
        member = [self.name, self.password, self.age]
#        print(member)
        return member

# '-------------------------------------------------------------------------------'
class Video:
    def __init__(self,title,duration,adult_mode):
        self.title = title
        self.diration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
#        print(self.title,';', self.diration,';', self.adult_mode)
    def curr_video(self):
        film = [self.title, self.diration, self.adult_mode]
#        print(film)
        return film

# '-------------------------------------------------------------------------------'
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add_video(self, *args):
        self.videos = []
#        print(self.videos)
        for i in args:
#            print(i)
            if i in self.videos:
                print('Такое видео уже есть в списке')
            else:
                self.videos.append(i)
#        print(self.videos)
        return self.videos

    def add_user(self,*args):
        self.users = []
        for i in args:
            if i in self.users:
                print('ТакоЙ пользователь уже есть в списке')
            else:
                self.users.append(i)
#                print(self.users)
#        print(self.users)
        return self.users

    def log_in(self,users):
        self.users = users
        input_login = input('Введите Логин: ')
        input_password = input('Введите пароль: ')
        self.login = input_login
        self.password = hash(input_password)
        print('self.login =',self.login, 'self.password =',self.password)
        for i in self.users:
            if self.login == i[0] and self.password == i[1]:
#                print('i[0]=',i[0], '  i[1]=',i[1])
                print('user Verified')
                current_user = i
#                print('current_user =',current_user)
            else:
                print('login Failed')
        return current_user

    def register(self,users):
        self.users = users
        print(' ====  New use found !  Register, please !  ===')
        input_nickname = input('Введите Логин: ')
        input_password = input('Введите пароль: ')
        input_age = input('Введите Ваш вoзраст:')
        self.nickname = input_nickname
        self.password = hash(input_password)
        self.age = int(input_age)
        new_user = [self.nickname, self.password, self.age]
#        print(new_user)
#        print('self.nickname =',self.nickname, 'self.password =',self.password,'self.age = ',self.age)
        if new_user not in self.users:
            self.users.append(new_user)
        print('   ===  Your data added to user list Successful !!!   ===')
#        print(self.users)
        return (self.users)

    def log_out(self,current_user):
        self.current_user = current_user
#        print(self.current_user)
        return self.current_user

    def get_videos(self, videos):
        self.videos = videos
        found_videos = []
        print(self.videos)
        key_word = input('Введите ключевое слово поиска: ')
        print(key_word)
        for i in self.videos:
            if key_word.lower() in (i[0]).lower():
                found_videos.append(i)
#                found_videos = i
                print('ключевое слово найдено в:', i[0])
        return found_videos

    def watch_video(self,found_videos,current_user):
        self.found_videos = found_videos
        self.current_user = current_user
        print(self.found_videos)
        print(self.current_user)
        print('Если в списке "found_videos" более одного видео - берем первое из списка')
        time_ = self.found_videos[0][1]
        if (self.found_videos[0][2] == True or self.found_videos[0][2] == None) and self.current_user[2] >= 18:
            print('Play time:  ')
            for i in range(1,time_+1):
                time.sleep(1)
                print(i,' ',end='')
        else:
            print("Your age dosn't allow to wach this video !")

# '-------------------------------------------------------------------------------'
# '-------------------------------------------------------------------------------'
#' =========================  СПИСОК  ВИДЕО  ========================='
print()
V1 = Video('Лучший язык программирования 2024 года.',15,adult_mode = None)
v1 = V1.curr_video()
V2 = Video('Для чего девушкам парень-программист?', 18, adult_mode = True)
v2 = V2.curr_video()
V3 = Video('Программисты в Простоквашино.', 25, adult_mode = True)
v3 = V3.curr_video()
#' =========================  СПИСОК  ПОЛЬЗОВАТЕЛЕЙ  ========================='
print()
U1 = User('Vasya Pupkin','Passw1',25)
u1 = U1.curr_user()
U2 = User('Petya Vaskin','Passw2', 13)
u2 = U2.curr_user()
U3 = User('Masha Penkina','Passw3',20)
u3 = U3.curr_user()


#' =========================  ВЫПОЛНЕНИЕ  ========================='
ur = UrTube()
print()
#' =========================  СОЗДАНИЕ СПИСКОВ videos & users  ========================='
print('  ======  add_video')
videos = ur.add_video(v1,v2,v1,v3,v2)
print(videos)
print('---------------------------------')
print('  ======  get_videos')
found_videos = ur.get_videos(videos)
print(found_videos)

print('---------------------------------')
print('  ====== add_user')
users = ur.add_user(u1,u2,u1,u3,u2)
print(users)
print()
print('===============================================')
#' =========================  РЕГИСТРАЦИЯ и ПРОВЕРКА НОВОГО  ПОЛЬЗОВАТЕЛЯ  ========================='
print('   ==== ur.register')
ur.register(users)
print((users))
print('---------------------------------')
print('   ==== ur.log_in')
current_user = ur.log_in(users)
print()
print('current_user =',current_user)

print('===============================================')
print('   =====  ur.watch_video')
ur.watch_video(found_videos,current_user)

print('===============================================')
print('   ====== log_out')
current_user = ur.log_out(current_user)
print()
print('current_user =',current_user, 'logged out - Free,  Good By')