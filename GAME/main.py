import random 

options = ('piedra', 'papel', 'tijera')

rounds = 1
computer_wins = 0 
user_wins = 0

print("""
    [ 🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
                >>> Ingresa una opción <<<
    """.encode('utf-8'))

while True:
    print('***' * 10)
    print('Round ', rounds)
    print('***' * 10)
    
    print(f'''
🤖 Computer wins: {computer_wins}
🙋 User wins: {user_wins}
        '''.encode('utf-8'))
    
    user_option = input('>>> Piedra, papel o tijera => ').lower()
    rounds += 1
    
    if not user_option in options:
        print('Esa opción no es valida')
        
    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)

    if user_option == computer_option:
        print('Empate!\n')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('🪨 Piedra gana a tijera ✂️'.encode('utf-8'))
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('📄 Papel gana a piedra 🪨')
            print('¡Computer gana!\n'.encode('utf-8'))
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('📄 Papel gana a piedra 🪨'.encode('utf-8'))
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('✂️ Tijera gana a papel 📄'.encode('utf-8'))
            print('¡Computer gana!\n')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('✂️ Tijera gana a papel 📄'.encode('utf-8'))
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('🪨 Piedra gana a tijera ✂️'.encode('utf-8'))
            print('¡Computer gana!\n')
            computer_wins += 1
    
    if computer_wins == 3:
        print('🎖️ El ganador es Computer 🎖️'.encode('utf-8'))
        break
    
    if user_wins == 3:
        print('🎖️ El ganador es User 🎖️'.encode('utf-8'))
        break