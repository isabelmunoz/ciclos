

estimulo = input('¿El usuario responde a estímulos?')

if estimulo == 'si':
    print('Valorar la necesidad de llevarlo al hospital mas cercano')
elif estimulo == 'no':
    print('Abrir la vía aérea')
    respira = input('¿Respira?')
    if respira == 'si':
        print('Permitirle posición de suficiente ventilación')
    elif respira == 'no':
        print('Administrar 5 ventilaciones y llamar a  ambulancia')
        signos_de_vida = input('¿Signos de vida?')
        if signos_de_vida == 'si':
            print('Reevaluar a la espera de la ambulancia')
        elif signos_de_vida == 'no':
            print('Administrar compresiones torácicas hasta que llegue ambulancia')
        ambulancia = input('¿Llegó la ambulancia?')
        while ambulancia == 'no':
            signos_de_vida = input('¿Signos de vida?')
            if signos_de_vida == 'si':
                print('Reevaluar a la espera de la ambulancia')
                ambulancia = input('¿Llegó la ambulancia?')
                if ambulancia =='si':
                    print('fin')
            else:
                print('Administrar compresiones torácicas hasta que llegue ambulancia')
        print('fin')
