import pygame as pg
import sys


pg.init()  # Инициализация

pg.display.set_caption('Ping_pong')  # создание названия приложения в шапке
img = pg.image.load('andr.png')  # получение изображения и присваивания его переменной
pg.display.set_icon(img)  # отрисовка иконки приложения


fps = 120  # fps кадры в секунду
window_width = 600  # ширина экрана
window_height = 400  # высота экрана

width_rect_1 = 10  # ширина платформы 1
height_rect_1 = 100  # высота платформы 1

width_rect_2 = 10  # ширина платформы 2
height_rect_2 = 100  # высота платформы 2

blue = (12, 56, 84)  # Создаем RGB цвет
white = (255, 255, 255)
black = (0, 0, 0)

r = 15  # радиус шарика
x, y = 100, 300  # положение шарика
direct_x, direct_y = 1, 1  # перемещение шарика по осям

x_rect_1 = (window_width - width_rect_1)  # положение платформы 1 (Ox)
y_rect_1 = window_height // 2 - height_rect_1 // 2  # положение платформы 1 (Oy)
direct_y_rect_1 = 3  # перемещение платформы по OY

x_rect_2 = 0  # положение платформы 2 (Ox)
y_rect_2 = window_height // 2 - height_rect_1 // 2  # положение платформы 2 (Oy)
direct_y_rect_2 = 3  # перемещение платформы по OY

screen = pg.display.set_mode((window_width, window_height))  # создание переменной отрисовки экрана
clock = pg.time.Clock()  # создаем переменной времени
bg = pg.image.load('bg.png').convert()  # добавление картинки для фона

count_user_1 = 0
count_user_2 = 0  # счет игроков

while True:  # цикл событий
    for event in pg.event.get():  # цикл отслеживающий события
        if event.type == pg.QUIT:  # отслеживание закрытия окна приложения
            sys.exit()  # прерывание выполнения скрипта

    clock.tick(fps)  # инициализация частоты кадров в секунду
    pg.event.pump()  # функция реагирующая на зажатие клавиш
    screen.blit(bg, (0, 0))  # добавление картинки на фон
    # screen.fill(blue)  # фон

    pg.draw.line(screen, white, (window_width // 2, 0), (window_width // 2, window_height), 8)  # отрисовка лонии сетки
    pg.draw.line(screen, white, (0, window_height // 2), (window_width, window_height // 2), 4)  # отрисовка лонии

    font_ = pg.font.SysFont('tahoma', 32)  # создание шрифра
    text = font_.render(f'{count_user_2} : {count_user_1}', True, (255, 0, 0))  # создание текста счета
    screen.blit(text, (window_width // 2 - 32, 0))  # отрисовка счета

    ball_1 = pg.draw.circle(screen, white, (x, y), r)  # отрисовка шарика

    pg.draw.rect(screen, black,  # отрисовка платформы 1
                 (x_rect_1, y_rect_1, width_rect_1, height_rect_1)
                 )

    pg.draw.rect(screen, black,  # отрисовка платформы 2
                 (x_rect_2, y_rect_2, width_rect_2, height_rect_2)
                 )

    if pg.key.get_pressed()[pg.K_DOWN]:  # обработка перемещения платформы 1 вниз
        if y_rect_1 + height_rect_1 >= window_height:  # проверка выхода за пределы экрана
            y_rect_1 = window_height - height_rect_1
        y_rect_1 += direct_y_rect_1

    if pg.key.get_pressed()[pg.K_UP]:  # обработка перемещения платформы 1 вверх
        if y_rect_1 <= 0:  # проверка выхода за пределы экрана
            y_rect_1 = 0
        y_rect_1 -= direct_y_rect_1

    if pg.key.get_pressed()[pg.K_s]:  # обработка перемещения платформы 2 вниз
        if y_rect_2 + height_rect_2 >= window_height:  # проверка выхода за пределы экрана
            y_rect_2 = window_height - height_rect_2
        y_rect_2 += direct_y_rect_2

    if pg.key.get_pressed()[pg.K_w]:  # обработка перемещения платформы 2 ввкрх
        if y_rect_2 <= 0:  # проверка выхода за пределы экрана
            y_rect_2 = 0
        y_rect_2 -= direct_y_rect_2

    x += direct_x  # пeремешение шарика
    y += direct_y

    if y < 0 + r or y + r >= window_height:  # отталкивание шарика от потолка и пола
        direct_y = - direct_y

    if x - r >= window_width:  # проверка вылета шарика за пределы половины 1 игрока
        count_user_2 += 1  # изменение счета второго игрока
        x, y = window_height // 2, window_width // 2  # новое мечто появления
        fps = 120  # возврат фпс в исходное состояние

    if x <= 0:  # проверка вылета шарика за пределы половины 2 игрока
        count_user_1 += 1
        x, y = window_height // 2, window_width // 2  # новое мечто появления
        fps = 120  # возврат фпс в исходное состояние

    if x - r in range(x_rect_2, x_rect_2 + width_rect_2) and y - r in range(y_rect_2, y_rect_2 + height_rect_2):  # отталкивание от 2 платформы
        direct_x = - direct_x  # изменение направления шарика
        fps += 10
    if x + r in range(x_rect_1, x_rect_1 + width_rect_1) and y + r in range(y_rect_1, y_rect_1 + height_rect_1):  # отталкивание от 1 платформы
        direct_x = - direct_x  # изменение направления шарика
        fps += 10


    pg.display.update()  # обновление экрана
