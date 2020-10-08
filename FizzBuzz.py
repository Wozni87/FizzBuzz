while True:
    try:
        current_number = int(input('Enter a number: '))
        if current_number % 5 == 0  and current_number % 3 == 0:
            print('FizzBuzz')
        elif current_number % 5 == 0:
            print('Buzz')
        elif current_number % 3 == 0:
            print('Fizz')
        else:
            print('Other')        
    except:
        print('Please enter a number')