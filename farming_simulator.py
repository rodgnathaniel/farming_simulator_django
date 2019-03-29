import random


class Farmer:
    def __init__(self, energy, filth, day_light, milk, milk_val, eggs, eggs_val, bacon, bacon_val, money, wallet, cow_price, cow_count, pig_price, pig_count, coop_price, coop_count):
        self.energy = energy
        self.filth = filth
        self.day_light = day_light
        self.milk = milk
        self.milk_val = milk_val
        self.eggs = eggs
        self.eggs_val = eggs_val
        self.bacon = bacon
        self.bacon_val = bacon_val
        self.money = money
        self.wallet = wallet
        self.cow_price = cow_price
        self.cow_count = cow_count
        self.pig_price = pig_price
        self.pig_count = pig_count
        self.coop_price = coop_price
        self.coop_count = coop_count

    def farm(self):
        self.day_light -= 2
        self.filth += 1
        self.energy -= 1
        if self.energy <= 0 or self.day_light <= 0:
            print('You ran out of energy and died')
            exit()
        if self.filth > 5:
            print('You got so stinky all the animals left you')
            exit()
        else:
            return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def bathe(self):
        self.day_light -= 1
        self.filth = 0
        if self.energy <= 0 or self.day_light <= 0:
            print('You ran out of energy and died')
            exit()
        else:
            return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def sleep(self):
        self.day_light = 10
        self.energy = 5
        return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def milk_cow(self):
        self.milk += self.milk_val
        return f'You have {self.milk} gallon of milk 🐄\nenergy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def farm_chicken(self):
        self.eggs += self.eggs_val
        return f'You have {self.eggs} eggs 🐔\nenergy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def make_bacon(self):
        self.bacon += self.bacon_val
        return f'You have {self.bacon} pounds of bacon 🐖\nenergy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def make_money(self):
        if self.money == 0:
            self.milk *= 3
            self.bacon *= 4
            self.money += self.milk + self.eggs + self.bacon
            self.wallet += self.money
            return f'you made {self.money} dollars'
        if self.money != 0:
            self.money = 0
            self.milk = 0
            self.bacon = 0
            self.eggs = 0
            return self.money, self.milk, self.bacon, self.eggs

    def check_wallet(self):
        return f'{self.wallet} dollars'

    def new_cow(self):
        if self.wallet < self.cow_price:
            print(f'you do not have enough money, you need ${self.cow_price}. keep on farming')
        elif self.wallet >= self.cow_price:
            self.milk_val += 5
            self.cow_count += 1
            self.wallet -= self.cow_price
            self.cow_price *= 2
            if self.cow_count == 11:
                self.wallet += 400000
                print('Congratulations you got a $400,000 bonus')
            return f' you now have {self.cow_count} cow(s)🐄, and make {self.milk_val} gallons of milk per farming. ${self.wallet} left'

    def new_pig(self):
        if self.wallet < self.pig_price:
            print(f'you do not have enough money, you need ${self.pig_price}. keep on farming')
        elif self.wallet >= self.pig_price:
            self.bacon_val += 24
            self.pig_count += 1
            self.wallet -= self.pig_price
            self.pig_price *= 2
            if self.pig_count == 11:
                self.wallet += 5000000
                print('Congratulations you got a $500,0000 bonus')
            return f' you now have {self.pig_count} pig(s)🐖, and make {self.bacon_val} pounds of bacon per farming. ${self.wallet} left'

    def upgrade_chicken_coop(self):
        if self.wallet < self.coop_price:
            print(f'you do not have enough money, you need ${self.coop_price}. keep on farming')
        elif self.wallet >= self.coop_price:
            self.eggs_val += 120
            self.coop_count += 1
            self.wallet -= self.coop_price
            self.coop_price *= 2
            if self.coop_count == 11:
                self.wallet += 1000000
                print('Congratulations you got a $1,000,000 bonus')
            return f' you now gain {self.eggs_val} eggs per farming🐔. ${self.wallet} left'

    def gamble(self, bet):
        self.wallet -= bet
        return self.wallet

    def black_jack_win(self, bet):
        self.wallet += bet
        return self.wallet


class Blackjack:

    def __init__(self, card):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.suits = ['♤', '♧', '♡', '♢']
        self.deck = []
        self.score = []
        self.card = card

    def build_deck(self):
        for i in self.suits:
            for j in self.values:
                self.deck.append((i, j))
        return self.deck

    def find_score(self):
        self.score = [sum(self.score)]
        print(self.score)
        if self.score > [21]:
            return f' Bust!, Your score is at {self.score}'
        else:
            return f'Your score is at {self.score}'

    def draw_card(self):
        self.card = random.choice(self.deck)
        for i in range(len(self.deck)):
            if i == self.card:
                self.deck.pop(self.card)
        if self.card[1] == 1 and self.score < [11]:
            self.score.append(11)
        elif self.card[1] == 'J':
            self.score.append(10)
        elif self.card[1] == 'Q':
            self.score.append(10)
        elif self.card[1] == 'K':
            self.score.append(10)
        else:
            self.score.append(self.card[1])
        return f'{self.card}'

    def win_or_loose(self):
        if self.score == [21]:
            return 'x5'
        if self.score <= [21] and self.score >= [19]:
            return 'x2'
        if self.score < [19]:
            return 'lose'
        if self.score > [21]:
            return 'bust'

    def reset_score(self):
        self.score = []
        return self.score


farmer = Farmer(5, 0, 10, 0, 5, 0, 12, 0, 24, 0, 0, 500, 1, 750, 1, 1000, 1)
black_jack = Blackjack(0)
print('you are just a simple farmer and you heart is on the farm')
print('you can take a farmer from the farm but you can never take a farm from the farmer\n...')

while True:
    task = input('\nHowdy, what would you like to do?\n(farm)\n(bathe)\n(sleep)\n(sell)\n(store)\n(check wallet)\n(blackjack)\n**type \'city boy\' to leave the farm**\n>')
    if task == 'farm':
        print(farmer.farm())
        animal = input('which animal are you looking to farm?\n(cow)\n(chicken)\n(pig)\n>')
        if animal == 'cow':
            print(farmer.milk_cow())
        elif animal == 'chicken':
            print(farmer.farm_chicken())
        elif animal == 'pig':
            print(farmer.make_bacon())
    elif task == 'bathe':
        print(farmer.bathe())
    elif task == 'sleep':
        print(farmer.sleep())
    elif task == 'sell':
        print(farmer.make_money())
        farmer.make_money()
    elif task == 'store':
        purchases = input(f'You have ${farmer.wallet}\nWhat would you like to buy:\n${farmer.cow_price}(new cow)\n${farmer.pig_price}(new pig)\n${farmer.coop_price}(chicken coop upgrade)\n>')
        if purchases == 'new cow':
            print(farmer.new_cow())
        elif purchases == 'new pig':
            print(farmer.new_pig())
        elif purchases == 'chicken coop upgrade':
            print(farmer.upgrade_chicken_coop())
    elif task == 'check wallet':
        print(farmer.check_wallet())

    elif task == 'blackjack':
        print('welcome to black jack\n♤ 🂱 🂲 🂳 🂴 🂵 🂶 🂷 🂸 🂹 🂺 🂻 🂼 🂽 🂾\n♧ 🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮\n♡ 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃌 🃍 🃎\n♢ 🃑 🃒 🃓 🃔 🃕 🃖 🃗 🃘 🃙 🃚 🃛 🃜 🃝 🃞')
        while True:
            try:
                bet = int(input('how much are you betting?\n>'))
                break
            except ValueError:
                print('Value must be integer.')
                continue
        farmer.gamble(bet)
        black_jack.build_deck()
        while True:
            start = input('would you like a hit?(type yes)\ntype \'stay\' if done\n>')
            if start == 'yes':
                print(black_jack.draw_card())
                print(black_jack.find_score())
            if black_jack.win_or_loose() == 'x5':
                bet *= 5
                print(f'TwEnTy OnE!\nCheers!\nyou won ${bet}')
                black_jack.reset_score()
                farmer.black_jack_win(bet)
                break
            if black_jack.win_or_loose() == 'bust':
                print('better luck next time')
                black_jack.reset_score()
                break
            elif start == 'stay' and black_jack.win_or_loose() == 'lose':
                print('better luck next time')
                black_jack.reset_score()
                break
            elif start == 'stay' and black_jack.win_or_loose() == 'x2':
                bet *= 2
                print(f'you won double: ${bet}')
                black_jack.reset_score()
                farmer.black_jack_win(bet)
                break
    elif task == 'city boy':
        print('Thank you, come back soon')
        break
