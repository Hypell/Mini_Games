from ast import AsyncFunctionDef
import time
import random

def intro():
    print("공유지의 비극 게임에 참가한 것을 환영합니다.")
    time.sleep(1)
    print("\n이 곳에는 본인 소유의 사유지와 모두와 공유하는 공유지가 있습니다.")
    time.sleep(1)
    print("\n랜덤한 10 ~ 15번 사이의 턴 동안 가장 많은 자원을 채취하면 승리하게 됩니다.")
    time.sleep(1)
    print("\n욕심은 되돌릴 수 없는 결과를 불러올 수도 있습니다.")
    time.sleep(1)
    print("\n그러면 게임을 시작하겠습니다.")
    print('='*60)
    time.sleep(3)

def explain():
    print("\n<공유지> \n\n- 공유지는 턴마다 총 100의 자원을 갖고 있습니다.\n- 공유지는 턴의 종료 후 자원이 줄어들어도 다음 턴에 다시 100의 자원으로 회복됩니다.")
    print("- 단, 한 턴에 공유지의 자원이 0 이하가 되면, 그 턴에 공유지를 선택한 참가자들은 어떠한 자원도 채취하지 못하고, 이후에는 공유지를 선택하면 자원을 얻지 못합니다.\n- 공유지는 고갈되더라도 알려주지 않습니다.")
    print('='*60)
    input('\npress ENTER to continue: ')

    print("\n<사유지> \n\n- 사유지는 모든 게임 참가자들이 보유하고 있는 영역으로 선택하면 그 턴에 20 ~ 30의 자원을 무작위로 얻게 됩니다. \n- 사유지는 고갈되지 않습니다.")
    print('='*60)
    input('\npress ENTER to continue: ')

    print("\n<눈가림> \n\n- 게임참가자 4명 중 한 명이라도 누적 자원 채취량이 100 또는 225이 넘으면, 넘게된 그 턴과 다음 턴의 누적 자원 채취량은 알려주지 않습니다.")
    print('='*60)
    input('\npress ENTER to continue: ')


# 누적 자원 채취량 출력하기
def print_status(member):
    for k in member:
        print(f'\n{k}: 당신에게는 자원이 {member[k]}만큼 있습니다.')
        time.sleep(1)

# 선택, 자원량 제대로 입력받기
def get_number(prompt, domain):
    while True:
        try:
            select = int(input(prompt))
            if select not in domain: raise ValueError
            return select
        except ValueError:
            print("\n올바르지 않은 입력입니다.\n")
            pass

#공유지 자원 더하기
def add_share_gain(pre_gain, member, share):
    if (sum(pre_gain.values())) >= share:
        return 0

    for k in member:
        member[k] += pre_gain[k]
    return 100

#사유지 자원 더하기
def add_personal_gain(member,k):
    personal_gain = random.randint(20,30)
    member[k] += personal_gain

#공유지 사유지 선택하기
def choose(member, pre_gain, k):
    import time
    print(f'\n{k}의 차례입니다.')
    time.sleep(1)
    print("\n공유지와 사유지 중 어느 영역을 선택하시겠습니까?")

    select = get_number('공유지(0), 사유지(1): ', (0, 1))

    if select == 0:
        print("\n공유지에서 자원을 얼만큼 채취하시겠습니까?")
        share_gain = get_number('입력: ', range(100))
        pre_gain[k] = share_gain
    elif select == 1:
        add_personal_gain(member, k)
        pre_gain[k] = 0

    return pre_gain

#눈가림
def close_eyes(member, exceed):
    a, b = exceed
    if max(member.values()) > 100:
        a += 1

    if max(member.values()) > 225:
        b += 1
    
    if ((a not in (1,2)) and (b not in (1,2))):
        print_status(member)

    return (a, b)

# 한 턴 실행하기
def do_turn(turn, member, share, exceed):
    print(f'\nTURN {turn + 1}')
    time.sleep(1)
    pre_gain = {}
    for k in member:
        pre_gain = choose(member, pre_gain, k)

    share = add_share_gain(pre_gain, member, share)
    
    exceed = close_eyes(member, exceed)

    return share, exceed

#전체 실행하기
def do_game():
    member = {'A':0, 'B':0, 'C':0, 'D':0}
    turn_num = random.randint(10,15)
    share = 100
    exceed = (0, 0)

    intro()
    explain()

    for turn in range(turn_num):
        share, exceed = do_turn(turn, member, share, exceed)

    print_result(member)


# 최종 결과 출력하기
def print_result(member):
    print('='*60)
    time.sleep(1)
    print("\n모든 턴이 끝났습니다.\n")
    time.sleep(1)
    winner = 'A'
    for k in member:
        print(f'{k}: {member[k]}')
        if(member[k] >= member[winner]):
            winner = k
    time.sleep(1)
    print(f'\n최종승자는 {k}입니다.')

#게임 실행
do_game()