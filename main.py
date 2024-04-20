from baillie_psw import baillie_test
from rabin_miller import isPrimeRM, mod_pow
from bitness import generate_prime
import base64


def convert_output(value, output_format):
    """Convert numeric output to various formats."""
    if output_format == "base2":
        return bin(value)[2:]  # Slice off the '0b' prefix
    elif output_format == "base10":
        return str(value)
    elif output_format == "base64":
        byte_value = value.to_bytes((value.bit_length() + 7) // 8, 'big')
        return base64.b64encode(byte_value).decode('utf-8')
    elif output_format == "byte[]":
        return list(value.to_bytes((value.bit_length() + 7) // 8, 'big'))
    else:
        return "Invalid format"


def main():
    while True:
        print("\nМеню:")
        print("1. Знайти просте число з вказаною кількістю біт.")
        print("2. Перевірити конкретне число на простоту (Baillie-PSW).")
        print("3. Перевірити конкретне число на простоту (Miller-Rabin).")
        print("4. Швидке піднесення в степінь по модулю.")
        print("5. Вихід.")

        choice = input("Введіть ваш вибір (1-5): ")
        if choice == '1':
            bits = int(input("Введіть кількість бітів для простого числа: "))
            prime_number = generate_prime(bits)
            print(f"Згенероване просте число: {prime_number}")
        elif choice == '2':
            number = int(input("Введіть число для перевірки на простоту: "))
            if baillie_test(number):
                print(f"Число {number} є простим.")
            else:
                print(f"Число {number} не є простим.")
        elif choice == '3':
            number = int(input("Введіть число для перевірки на простоту: "))
            k = int(input("Введіть кількість ітерацій тесту: "))
            if isPrimeRM(number, k):
                print(f"Число {number} є простим.")
            else:
                print(f"Число {number} не є простим.")
        elif choice == '4':
            base = int(input("Введіть основу (base): "))
            exponent = int(input("Введіть степінь (exponent): "))
            modulus = int(input("Введіть модуль (modulus): "))
            result = mod_pow(base, exponent, modulus)
            format_choice = input("Виберіть формат виводу (base2, base10, base64, byte[]): ")
            formatted_result = convert_output(result, format_choice)
            print(f"Результат {base}^{exponent} mod {modulus} = {formatted_result}")
        elif choice == '5':
            print("Завершення програми.")
            break
        else:
            print("Неправильний вибір, спробуйте знову.")


if __name__ == "__main__":
    main()