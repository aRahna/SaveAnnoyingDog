import random
def play_game():
    with open('слова.txt', 'r', encoding='UTF-8') as f:
        words_list = f.read().split('\n')
        random_num = random.randint(0, (len(words_list) - 1))
    current_word = list(words_list[random_num].upper())
    print('У тебя есть 10 жизней! \nБукв в слове:', str(len(current_word)))
    picked_letters = []
    correct_ones = []
    for i in range(len(current_word)):
        correct_ones.append('_ ')
    lifes = 10
    while lifes != 0:
        if current_word == correct_ones:
            print('\nТы победил!')
            x = input('Еще одну игру? (напиши да/нет): ')
            if x.lower() == 'нет':
                print('Игра закончена!')
            else:
                play_game()
            break
        current_letter = input('Введи букву: ').upper()
        if current_letter in picked_letters:
            print('Эта буква уже была!')
            continue
        if current_letter in current_word:
            index_list = []
            for i in range(len(current_word)):
                if current_word[i] == current_letter:
                    index_list.append(i)
            picked_letters.append(current_letter)
            for i in index_list:
                correct_ones[i] = current_letter.upper()  
            print('Правильно!')
            r = "слово: " + "".join(correct_ones)
            print(r)
        else:
            picked_letters.append(current_letter)
            lifes -= 1
            print('Неправильно :с')
            print('Осталось жизней: ', str(lifes))
            continue
    x1 = input('Еще одну игру? (напиши да/нет): ')
    if x1.lower() == 'нет':
        print('Игра закончена!')
    else:
        play_game()

play_game()


