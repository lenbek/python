import random

class LotoGame:
    def __init__(self):
        self.card_line_num = 3
        self.card_col_num = 9
        self.card_uncov_cell_line = 5
        self.numbers = 90
        self.players = []

    def step_generator(self):
        lst = list(range(1, self.numbers + 1))
        random.shuffle(lst)
        for i in lst:
            yield i

    def check_winner(self):
        if len(self.players) == 1:
            self.players[0].status = 1
            return True
        for p in self.players:
            if p.status == 1:
                return True
        return False

    def start(self):
        if len(self.players) < 2:
            print('Недостаточно игроков')
            return
        steps = self.step_generator()
        for step_nr, step_num in enumerate(steps):
            if self.check_winner():
                print('Игра окончена. Победители: ', ', '.join(p.name for p in self.players if p.status == 1))
                break
            print('=' * 50)
            print(f'Ход: {step_nr+1}. Новый бочонок: {step_num}(осталось {self.numbers-step_nr-1})')
            print('=' * 50)

            for p in self.players:
                print(p)

            for p in self.players:
                ind = p.check_num(step_num)
                if p.is_comp and ind >= 0:
                    p.del_num(ind)
                elif not p.is_comp:
                    slv = input(f'{p.name}, зачеркнуть цифру? (y/n) ').lower()
                    if slv == 'y' and ind >= 0:
                        p.del_num(ind)
                    elif slv == 'n' and ind < 0:
                        continue
                    else:
                        print('Ответ неверный! Вы проиграли.')
                        self.players.remove(p)
        else:
            print('Игра окончена. Победители: ', ', '.join(p.name for p in self.players))


    def add_player(self, name, is_comp):
        self.players.append(LotoCard(name, is_comp))

class LotoCard(LotoGame):
    def __init__(self, name, is_comp):
        super().__init__()
        self.name = name
        self.is_comp = is_comp
        self.gen_card()
        self.status = 0

    def gen_card(self):
        self.uncov_cell = self.card_uncov_cell_line * self.card_line_num
        self.card = [''] * self.card_col_num * self.card_line_num

        lst_nn = list(random.sample(range(1, self.numbers + 1), self.uncov_cell))
        lst_nn.sort()
        for i in range(0, self.card_line_num):
            lst_pos = random.sample(range(0, self.card_col_num), self.card_uncov_cell_line)
            lst_pos.sort()
            for j, p in enumerate(lst_pos):
                self.card[i * self.card_col_num + p] = lst_nn[i + self.card_line_num * j]

    def __str__(self):
        txt = f'--- Карточка: {self.name} ----------' + '\n'
        txt += '\n'.join(' '.join((map('{:>2}'.format,
                                       self.card[self.card_col_num*i:self.card_col_num*(i+1)])))
                             for i in range(0, self.card_line_num))
        txt += ('\n' + '---' * 10)
        return txt

    def check_num(self, num):
        try:
            return self.card.index(num)
        except ValueError:
            return -1

    def del_num(self, ind):
        self.card[ind] = '-'
        self.uncov_cell -= 1
        if self.uncov_cell == 0:
            self.status = 1


game = LotoGame()
game.add_player('Игрок', False)
game.add_player('Компьютер', True)
# game.add_player('Компьютер2', True)

game.start()

