# CALCULADOR SIMPLES

numero1 = 0
numero2 = 0
resultado = 0
op = ''

while True:
    print('CALCULADORA SIMPLES')
    print('1 - SOMA')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')
    print('5 - SAIR')

    op = input('Escolha uma opção: ')

    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    if op == '1':
        resultado = numero1 + numero2
        print(f'Resultado: {numero1} + {numero2} = {resultado}')
    elif op == '2':
        resultado = numero1 - numero2
        print(f'Resultado: {numero1} - {numero2} = {resultado}')
    elif op == '3':
        resultado = numero1 * numero2
        print(f'Resultado: {numero1} * {numero2} = {resultado}')
    elif op == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f'Resultado: {numero1} / {numero2} = {resultado}')
        else:
            print('Erro: Divisão por zero não é permitida.')
    else:
        print('Opção inválida. Tente novamente.')

    if op == '5':
        print('Saindo da calculadora...')
        break
