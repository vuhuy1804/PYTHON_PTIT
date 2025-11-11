
def count_digit_up_to(digit, n):
    total = 0

    for pos in range(10):  
        place_value = 10 ** pos  
        if place_value > n:
            break

        left_part = n // place_value     # phần bên trái (bao gồm chữ số hiện tại)
        right_part = n % place_value     # phần bên phải (các chữ số nhỏ hơn vị trí này)
        current_digit = left_part % 10   # chữ số tại vị trí đang xét

        
        if current_digit > digit:
            total += (left_part // 10 + 1) * place_value
        elif current_digit == digit:
            total += (left_part // 10) * place_value + (right_part + 1)
        else: 
            total += (left_part // 10) * place_value

        # Trường hợp đặc biệt cho chữ số 0 (không được tính ở đầu số)
        if digit == 0:
            total -= place_value

    return total


def count_digit_in_range(digit, low, high):
    return count_digit_up_to(digit, high) - count_digit_up_to(digit, low - 1)


t = int(input().strip())
for _ in range(t):
    low, high = map(int, input().split())
    for d in range(10):
        print(count_digit_in_range(d, low, high), end=' ')
    print()
