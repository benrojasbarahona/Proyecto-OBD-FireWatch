""" 
    mi idea a partir del archivo 'rodales.csv' extraer la información de dos maneras, una para cada
    diccionario, uno que tenga un diccionario en la cual sus llaves sean los propietarios, y en sus argumentos
    para cada respectivo propietario, agregar el rodal el cual es dueño, sus porcentajes de exotico y nativo.
    
    luego en la otra manera de guardar la información, quiero hacer otro diccionario, el cual tenga como claves
    los rodales, y en sus argumentos, sus porcentajes de nativo, exotico y propietario de ser necesario.
    
    estas dos formas de almacenar la información a partir de un solo archivo me va a permitir trabajar mucho mas
    libremente con los datos y poder extraer informacion mas rapidamente de manera mas fluida, para que de esta
    manera, poder mostrar la informacion en menos lineas y menos analizis de datos.

"""#    @shyupss_    #

def main():

    def promedio(arreglo_de_numeros: list) -> float: #funcion de promedio
        return (round((sum(arreglo_de_numeros))/len(arreglo_de_numeros), 2))
    
    #lectura del archivo csv...
    with open('rodales.csv', 'r') as info:
        lineas_rodales_info = info.readlines()

    propietario_key = {}; rodal_key = {} # <--- "data_pack"
    
    #filtro las lineas y las almaceno para ambos tipos de "data_pack"
    for linea in lineas_rodales_info:
        rodal, propieario, nativo, exotico = linea.strip('\n').split(', ')
        #  guardo los datos en los distintos "data_pack"
        #  <--------------------------------------------------------------------------------------->
        if propieario not in propietario_key:
            propietario_key[propieario] = {'rodales': rodal, 'nativo': float(nativo), 'exotico': float(exotico),
                                           'array_nativo': [float(nativo)], 'array_exotico': [float(exotico)]}
        else:
            propietario_key[propieario]['array_nativo'].append(float(nativo))
            propietario_key[propieario]['array_exotico'].append(float(exotico))
            propietario_key[propieario]['rodales'] += f', {rodal}'
            propietario_key[propieario]['nativo'] = promedio(propietario_key[propieario]['array_nativo'])
            propietario_key[propieario]['exotico'] = promedio(propietario_key[propieario]['array_exotico'])
        # <--------------------------------------------------------------------------------------->
        if rodal not in rodal_key:
            rodal_key[rodal] = {'propietario': propieario, 'nativo': float(nativo), 'exotico': float(exotico)}
        else:
            ... #el pepe
        # <--------------------------------------------------------------------------------------->
    print("propietarios lista:\n", propietario_key),
    print('<----------------------------------->')
    print("propietarios lista:\n", rodal_key)

main()