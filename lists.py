mylist = ['ботинки','куртка','джинсы','футболка','свитер']

print('На ноги я одеваю {0}, а под {1} на мне {2}'.format(mylist[2], \
                                                          mylist[1], mylist[3]))

print('Всего вещей на мне одето:', len(mylist))

new_list = [1 , 2, mylist]
print(new_list)

def shoping():
    flag = True
    while flag:
        vote = input('Если хотите добавить какую-то вещь в свой инвентарь напишите д, удалить - у')
        if vote == 'д':
            voteD = input('Что хотите добавить?')
            mylist.append(voteD)
            print('Теперь у вас {0} вещей: {1}.'.format(len(mylist), mylist))
            break
        elif vote == 'у':
            voteD = input('Что хотите удалить?')
            for item in mylist:
                if item == voteD:
                    del mylist[mylist.index(voteD,)]
                    print('Теперь у вас {0} вещей: {1}.'.format(len(mylist), \
                                                                mylist))
                    break
        else:
            print('Не понятно, попробуйте еще раз.')

shoping()
