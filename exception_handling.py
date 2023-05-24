try: #potencjalny problem z kodem
    dzielna = int(input("enter a number to divide: "))
    dzielnik = int(input("enter a number to divide by: "))
    liczba = dzielna / dzielnik
except ZeroDivisionError as e: #dzielenie przez zero
    print(e)
    print("You can't divide by 0")
except ValueError as e: #nie ten typ zmiennej
    print(e)
    print("Only numbers please")
except Exception as e: #wyjątek
    print(e)
    print("something went wrong")
else: #jeżeli nie będzie żadnego wyjątku to wykona się akcja
    print(liczba)
finally: #akcja wykonuje się zawsze na końcu
    print("this will print whenever the code is finished!")