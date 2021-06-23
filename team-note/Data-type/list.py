# 리스트의 인덱싱과 슬라이싱

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 여덟 번째 원소만 출력
print(a[7])  # 8

# 뒤에서 첫 번째 원소 출력
print(a[-1])  # 9

# 뒤에서 세 번째 원소 출려
print(a[-3])  # 7

# 네 번째 원소 값 변경
a[3] = 7
print(a)  # [1, 2, 3, 7, 5, 6, 7, 8, 9]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])  # [2, 3, 7]
