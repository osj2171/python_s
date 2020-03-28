# 컴퓨터가 생각하는 수를 맞추기
# 기회는 6번
# 6번 이후에는 정답을 출력한다.

import random as r

q_num = r.randint(1,20)
print("---숫자 맞추기---")

for num in range(1,20):
    ans = int(input("%d번째 예상숫자:"% num))
    if ans == q_num:
        print("정답")
        break
    if ans > q_num:
        print("아래")
    else:
        print("위")

if num == 19:
    print("답은 %d"% q_num)




