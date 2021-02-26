import decimal
def main():
    while True:
        try:
            inp = float(input('please enter your number (input 0 for exit) : ')) 
            if inp == 0.0 :
                break
            elif inp < 1.0 or inp > 10.0:
                print('you have to input number between 1 and 10')
                print('please try again')
                continue
            else:
                d = decimal.Decimal(str(inp))
                if (d.as_tuple().exponent * -1) >= 11:
                    print('you have to input number with only 12 decimal places')
                    print('please try again')
                    continue
                else:
                    ans = isFloatingValue(str(inp))
                    print(ans)
        except ValueError:
            print('you put the worng format')
            print('please try again with float')

def isFloatingValue(data):
    data = data.replace('.','')
    for i in range(3):
        number = int(data[0:i+2])
        if isPrime(number): return True
    return False

def isPrime(number):
    if (number <= 1) : 
        return False
    if (number <= 3) : 
        return True
    if (number % 2 == 0 or number % 3 == 0) : 
        return False
    i = 5
    while(i * i <= number) : 
        if (number % i == 0 or number % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
        

if __name__ == "__main__":
    main()