n = int(input())


# 各桁の和を求める
def sum_all_digits(n):
    sum_digits = 0
    # 文字列型に変換して先頭から要素を取得
    for digit in str(n):
        sum_digits += int(digit)
    return sum_digits


print("Yes" if n % sum_all_digits(n) == 0 else "No")
