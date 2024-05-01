from baillie_psw import baillie_test
from rabin_miller import isPrimeRM, mod_pow
from bitness import generate_prime
import base64


# Передбачити можливість виводу результатів у base2, base10, base64, byte[]
def convert_output(value, output_format):
    if output_format == "base2":
        return bin(value)[2:]  # Повертає двійкове представлення числа без префікса '0b'
    elif output_format == "base10":
        return str(value)  # Повертає десяткове представлення числа у форматі рядка
    elif output_format == "base64":
        # Конвертує число у послідовність байтів та кодує у формат base64
        byte_value = value.to_bytes((value.bit_length() + 7) // 8, 'big')
        return base64.b64encode(byte_value).decode('utf-8')
    elif output_format == "byte[]":
        # Повертає список байтів, що представляють число
        return list(value.to_bytes((value.bit_length() + 7) // 8, 'big'))
    else:
        return "Invalid format"  # Невалідний формат вводу


def main():
    while True:
        print("\nМеню:")
        print("1. Знайти просте число з вказаною кількістю біт.")
        print("2. Перевірити конкретне число на простоту (Baillie-PSW).")
        print("3. Перевірити конкретне число на простоту (Miller-Rabin).")
        print("4. Швидке піднесення в степінь по модулю.")
        print("5. Вихід.")

        try:
            choice = int(input("Введіть ваш вибір (1-5): "))
        except ValueError:
            print("Будь ласка, введіть коректне числове значення.")
            continue

        if choice == 1:
            try:
                bits = int(input("Введіть кількість бітів для простого числа: "))
                if bits < 2:
                    print("Кількість бітів має бути більшою за 1.")
                    continue
                prime_number = generate_prime(bits)
                print(f"Згенероване просте число: {prime_number}")
            except ValueError:
                print("Будь ласка, введіть ціле число.")
        elif choice == 2 or choice == 3:
            try:
                number = int(input("Введіть число для перевірки на простоту: "))
                if number < 2:
                    print("Число має бути більше 1.")
                    continue
                if choice == 2:
                    if baillie_test(number):
                        print(f"Число {number} є простим.")
                    else:
                        print(f"Число {number} не є простим.")
                else:
                    k = int(input("Введіть кількість ітерацій тесту: "))
                    if k < 1:
                        print("Кількість ітерацій має бути більшою за 0.")
                        continue
                    if isPrimeRM(number, k):
                        print(f"Число {number} є простим.")
                    else:
                        print(f"Число {number} не є простим.")
            except ValueError:
                print("Будь ласка, введіть коректне ціле число.")
        elif choice == 4:
            try:
                base = int(input("Введіть основу (base): "))
                exponent = int(input("Введіть степінь (exponent): "))
                modulus = int(input("Введіть модуль (modulus): "))
                if modulus <= 0:
                    print("Модуль має бути більше за 0.")
                    continue
                result = mod_pow(base, exponent, modulus)
                format_choice = input("Виберіть формат виводу (base2, base10, base64, byte[]): ")
                formatted_result = convert_output(result, format_choice)
                print(f"Результат {base}^{exponent} mod {modulus} = {formatted_result}")
            except ValueError:
                print("Будь ласка, введіть коректні числові значення.")
        elif choice == 5:
            print("Завершення програми.")
            break
        else:
            print("Неправильний вибір, спробуйте знову.")

if __name__ == "__main__":
    main()
