offices = [
    "1) Kazakstan", "2) Paris", "3) Uar", "4) Kyrgyzstan", "5) San_Francisco", 
    "6) Germany", "7) Moscow", "8) Sweden"
    ]
G = input("Hello user! Input 'Hello' to continue:\n ").lower()
b = "hello"
while G != b:
    print("Введите Hello: ")
    G = input()


if G == 'hello':
    # print(a)
    for i in offices:
        print(i)
    choice = int(input("Which office: "))
    text = input("Этот текст будет на вашем файле: ")
    # print('Wellcome!')
    if choice == 1:
        with open("Google_Kazakstan.txt", 'w') as filename:
            filename.write(text)
        print("Ваше сообшение получено")
    
    elif choice == 2:
        with open("Google_Paris.txt", 'w') as filename:
            filename.write(text)
        print("Ваше сообшение получено")
        
    elif choice == 3:
        with open("Google_ Uar.txt", 'w') as filename:
            filename.write(text)
        print("Ваше сообшение получено")

    elif choice == 4:
        with open("Google_ Kyrgyzstan.txt", 'w') as filename:
            filename.write(text)
        print("Ваше сообшение получено")
    
    elif choice == 5:
        with open("Google_ San_Francisco.txt", 'w') as filename:
            filename.write(text)
        print("Ваше сообшение получено")
    
    elif choice == 6:
        with open("Google_ Germany.txt", 'w') as filename:
            filename.write(text)
        print("Ваше сообшение получено")
    
    elif choice == 7:
        with open("Google_ Moscow.txt", 'w') as filename:
            filename.write(text)
        print("Ваше сообшение получено")
    
    elif choice == 8:
        with open("Google_ Sweden.txt", 'w') as filename:
            filename.write(text)
        print("Ваше сообшение получено")
else:
    print("Ошибка")
    