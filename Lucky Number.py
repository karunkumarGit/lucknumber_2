number = int(input())

is_multiple_of_9 = ((number % 9) == 0)

number_str = str(number)
first_digit = int(number_str[0])
second_digit = int(number_str[1])
is_first_digit = first_digit == 9
is_second_digit = second_digit == 9

is_any_digit_9 = is_first_digit or is_second_digit

condition = is_multiple_of_9 or is_any_digit_9

if condition:
    print("lucky number")
else:
    print("not")