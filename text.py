while True:
    '''Отрисовка карточек и отображение кликов'''
    if wait == 0:
        wait = 20  # столько тиков надпись будет на одном месте
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1
    '''Обработка кликов по карточкам'''
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            x, y = event.pos
            for i in range(num_cards):
                # ищем, в какую карту попал клик
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:  # если на карте есть надпись перекрашиваем в зелёный, плюс очко
                        cards[i].color(GREEN)
                        points += 1
                    else:  # иначе перекрашиваем в красный, минус очко
                        cards[i].color(RED)
                        points -= 1
                    cards[i].fill()
                    score.set_text(str(points), 40, DARK_BLUE)
                    score.draw(0, 0)
    '''Выигрыш и проигрыш'''
    new_time = time.time()

    if new_time - start_time >= 11:
        win = Label(0, 0, 500, 500, LIGHT_RED)
        win.set_text("Время вышло!!!", 60, DARK_BLUE)
        win.draw(110, 180)
        break

    if int(new_time) - int(cur_time) == 1:  # проверяем, есть ли разница в 1 секунду между старым и новым временем
        timer.set_text(str(int(new_time - start_time)), 40, DARK_BLUE)
        timer.draw(0, 0)
        cur_time = new_time

    if points >= 5:
        win = Label(0, 0, 500, 500, LIGHT_GREEN)
        win.set_text("Ты победил!!!", 60, DARK_BLUE)
        win.draw(140, 180)
        resul_time = Label(90, 230, 250, 250, LIGHT_GREEN)
        resul_time.set_text("Время прохождения: " + str(int(new_time - start_time)) + " сек", 40, DARK_BLUE)

        resul_time.draw(0, 0)

        break

    pygame.display.update()
    clock.tick(40)

pygame.display.update()
