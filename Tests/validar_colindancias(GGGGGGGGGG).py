

def retorna_lista_rodales(direccion: str) -> list:
    """Retorna una lista con las IDS de los rodales ya ingresados"""
    global dicc_rodales
    rodales = list(dicc_rodales.keys()) # Toma todos los rodales del registro y los añade a una lista
    rodales.append("")

    for rodal in rodales:
        if dicc_rodales[rodal]['colindancias'][direccion] == rodal:
            rodales.pop(rodal)

    return rodales.sort()


def main():
    ...


if __name__ == '__main__':
    main()


referencia_validacion = {'N':{'NE': 'SE',
                     'NW': 'SW',
                      'S':'S',
                     'SE': 'S',
                     'SW': 'S'},
                     
               'NE':{'SE': 'S',
                      'N': 'NW',
                     'NW': 'SW',
                     'SW': 'SW',
                      'S':'SW'},

               'NW':{'N': 'NE',
                     'SW': 'S',
                      'S': 'SE',
                     'SE': 'SE',
                     'NE': 'SE'},

                'S':{'SE': 'NE',
                     'SW': 'NW',
                      'N': 'N',
                     'NE': 'N',
                     'NW': 'N'},

                'SE':{'S': 'SW',
                     'NE':'SE',
                     'NW': 'NW',
                     'SW': 'NW',
                      'N': 'NW'},

                'SW':{'S': 'SE',
                     'NW': 'N',
                      'N': 'NE',
                     'SE': 'NE',
                     'NE': 'NE'}
}

for direct, colin in colindancias.items():
    if not colindancia_valida(colin, direct):
        colindante_valido = [colin, direct]

for direct, colin in colindancias.items():
    if colindante_valido[0] != colin:
        valido = colindancias_validas(colindante_valido[0], colin, colindante_valido[1], direct)
        if not valido:
            raise 'blablebli'

def colindancias_validas (rodal_valido: str, rodal_a_validar: str, direccion_valido: str, direccion_a_validar: str):
    if dicc_rodales[rodal_valido]['colindancias'][referencia_validacion[direccion_valido][direccion_a_validar]] != rodal_a_validar:
        # La colindancia es invalida
        return False
    # La colindancia es valida
    return True