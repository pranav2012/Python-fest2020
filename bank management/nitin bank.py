print("Welcome to Black Eagle Bank ")
restart = ['Y']
chances = 3
balance = 999.12
while chances >= 0:
    pin = int(input('Please enter the 4 digit PIN:'))
    if pin == 1234:
        while restart not in ('n','NO','no','N'):
            print('\n\nPlease press 1 for your balance.')
            print('Please enter 2 to make a withdrawal')
            print('Please enter 3 to pay in')
            print('Please enter 4 to return card')
            option = int(input('what would you like to choose ?:'))
            if option == 1:
                print('Your balance is Rs.',balance)
                if restart in ('n','NO','no','N'):
                    print('Thank You !!!')
                    break
                
            elif option == 2:
                option2 = ('y')
                withdrawal = float(input('How much would you like to withdraw? 10,20,50,100,200 for others 1: '))
                if withdrawal in [10,20,50,100,200]:
                    balance = balance - withdrawal
                    print('\n\nYou balance is now Rs.',balance)
                    restart = input('\n\nWould you like to go back?')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawal != [10,20,50,100,200]:
                    print('Invalid amount , Please re-try\n')
                    restart = 'y'
                elif withdrawal == 1:
                    withdrawal = float(input('Please enter desired amount:'))
                    
            elif option == 3:
                pay_in = float(input('How much would you like to pay in ?:'))
                balance = balance + pay_in
                print('\n\nYour balance is now Rs.',balance)
                restart = input('Would you like to go back?')
                if restart in ('n','NO','no','N'):
                    print('Thank You !!!')
                    break

            elif option == 4:
                print('Please wait while your card is returned...\n')
                print('Thank you for your interest in our Bank !!!')
                break

            else:
                print('Please enter a correct number.\n')
                restart = 'y'

    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0 :
            print('\n No more tries\n Thank You !!!')
            break
