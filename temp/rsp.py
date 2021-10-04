from random import randint

status = ['가위', '바위', '보', '가위']

print('[ Start game to Rock-paper-scissors game ]')

while True:
    personSco = 0
    computerSco = 0
    i = 1
    while True:
        print(f'>>>{i}회<<<')

        person = int(input('( 1.가위 2.바위 3.보 ): ')) - 1
        computer = randint(0, 2)

        if status[person + 1] == status[computer]:
            computerSco += 1
        elif person == computer:
            pass
        else:
            personSco += 1

        print(' 나:', status[person])
        print(' 컴퓨터:', status[computer])
        print(f' 현재 스코어 : {personSco} : {computerSco}')

        if personSco == 2 or computerSco == 2:
            if personSco > computerSco:
                print("Congratulations! You won")
            else:
                print("You lost, next chance...")
            break

        i += 1

    YN = input("Shall we continue ?: ")
    if YN == 'N':
        break
