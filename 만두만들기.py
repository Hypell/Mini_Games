import time

def intro():
    print("만두 가게를 운영하는 당신.")
    time.sleep(1)
    print("\n방금 손님이 가게에 들어와 만두를 주문했습니다.")
    time.sleep(1)
    print("\n이제부터 맛있는 만두를 만들어 주세요!")


def successlist(success):
    success.append('success')
    return success


def mandusok(success):
    mandusok = set()
    time.sleep(1)
    print('\n만두 속을 만들기 위한 재료 5가지를 선택하십시오.')
    time.sleep(1)
    print('\n돼지고기(0), 닭고기(1), 김치(2), 물(3), 우유(4), 달걀 노른자(5), 대파(6), 양파(7), 부추(8), 두부(9), 당면(10)')
    for i in range(1,6):
        mandusok_ing_i = int(input(f'선택{i}: '))
        mandusok.add(mandusok_ing_i)
    if mandusok == {0, 3, 5, 8, 10}:
        successlist(success)
    elif mandusok == {1, 4, 5, 7, 9}:
        successlist(success)
    elif mandusok == {2, 5, 6, 9, 10}:
        successlist(success)


def mandupi(success):
    mandupi = set()
    time.sleep(1)
    print('\n만두 피 반죽을 만들기 위한 재료 3가지를 선택하십시오.')
    time.sleep(1)
    print('\n중력분(0), 박력분(1), 물(2), 달걀 흰자(3), 소금(4), 설탕(5)')
    for i in range(1,4):
        mandupi_ing_i = int(input(f'선택{i}: '))
        mandupi.add(mandupi_ing_i)
    if mandupi == {0, 2, 3}:
        successlist(success)
    elif mandupi == {0, 2, 4}:
        successlist(success)
    elif mandupi == {0, 3, 4}:
        successlist(success)


def mandushape_boil(success):
    mandushape_boil = {}
    time.sleep(1)
    print('\n만들고 싶은 만두 모양을 한 가지 선택하십시오.')
    time.sleep(1)
    print('\n둥근 모양(0), 반달 모양(1), 호빵 모양(2)')
    mandushape = int(input(f'선택: '))
    print('\n만두를 익힐 방법을 한 가지 선택하십시오.')
    time.sleep(1)
    print('\n찌기(0), 기름에 굽기(1), 삶기(2)')
    manduboil = int(input(f'선택: '))
    mandushape_boil[mandushape] = manduboil
    if mandushape_boil == {0:2}:
        successlist(success)
    if mandushape_boil == {1:1}:
        successlist(success)
    if mandushape_boil == {2:0}:
        successlist(success)

while True:
    success = []
    intro()
    mandusok(success)
    mandupi(success)
    mandushape_boil(success)

    if success == ['success', 'success', 'success']:
        print('\n손님: 정말 맛있네요! 다음에 또 오겠습니다.')
        break
    else:
        print('\n손님: ……웩 최악이네요. 안녕히계세요.\n')
        time.sleep(1)
        continue