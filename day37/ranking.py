k= [100, 55, 65, 85, 90, 91, 85, 70, 60, 95]
# 방법 1
k_idx = 0

print("<우리 학급의 등급 결과입니다.>")
for i in k:
    k_idx += 1
    if i >= 70:
        result = "1급"
    elif i >=60:
        result = "2급"
    else:
        result = "불합격"

    print(str(k_idx) + "번 학생은" + result + "입니다.")

print('*'*30)
# 방법 2 for in range()
n = len(k)
for i in range(0, n):
    if k[i] >= 70:
        result = "1급"
    elif k[i] >= 60:
        result = "2급"
    else:
        result = "불합격"
    print("{}번 학생은 {}입니다.".format(i+1, result))
