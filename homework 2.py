from collections import Counter

def find_and_return_odd_repeating_number(input_list):
    counts = Counter(input_list)
    odd_repeating_numbers = [number for number, count in counts.items() if count % 2 != 0]
    return odd_repeating_numbers[0] if odd_repeating_numbers else None

# Misol ro'yxati
my_list = [1, 2, 3, 4, 5, 3, 2, 7, 8, 9, 10, 1]

# Ro'yxat ichidagi qaytalanib kelayotgan toq sonni topish
result = find_and_return_odd_repeating_number(my_list)
print("Qaytalanib kelayotgan toq son:", result)