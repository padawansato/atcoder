n = input()
lst = [map(int,input().split())]



def check_even(lst):
    """
引数　リスト
返り値　リストがすべて偶数ならbool　trueを返す
    """
    i = 0
    while lst[i] % 2 == 0:
        i += 1

        if i == len(lst):
            return True
        else:
            return False


def make_even(lst):
    """
引数　リスト
返り値　２で割られた数になったリスト
    """
    while i % 2 == 0:
        lst[i] = lst[i] // 2
    
    return lst


cnt = 0
while True:
    if check_even(lst) is True:
        lst = make_even(lst)
        cnt += 1
    else:
        break

print(cnt)
