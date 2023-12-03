dicc_rodales = {
        'R1'   : {'b_nativo': 32, 'b_exotico': 68, 'propietario': 'NDSJKNDKAS', 'colindancias': {'N': 'R4', 'NW': 'R6', 'NE': 'R3', 'S': '', 'SE': 'R2', 'SW': ''}},
        'R2'   : {'b_nativo': 23, 'b_exotico': 77, 'propietario': 'NSDJKNDFJSA', 'colindancias': {'N': 'R3', 'NW': 'R1', 'NE': '', 'S': '', 'SE': '', 'SW': ''}},
        'R3'   : {'b_nativo': 32, 'b_exotico': 68, 'propietario': 'ADBHJKSABNJDK', 'colindancias': {'N': 'R5', 'NW': 'R4', 'NE': '', 'S': 'R2', 'SE': '', 'SW': 'R1'}},
        'R4'   : {'b_nativo': 43, 'b_exotico': 57, 'propietario': 'NDAJKASND', 'colindancias': {'N': '', 'NW': 'R7', 'NE': 'R5', 'S': 'R1', 'SE': 'R3', 'SW': 'R6'}},
        'R5'   : {'b_nativo': 43, 'b_exotico': 57, 'propietario': 'NDJKSANJDKAS', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R3', 'SE': '', 'SW': 'R4'}},
        'R6'   : {'b_nativo': 43, 'b_exotico': 57, 'propietario': 'JKDASNLKD', 'colindancias': {'N': 'R7', 'NW': '', 'NE': 'R4', 'S': '', 'SE': 'R1', 'SW': ''}},
        'R7'   : {'b_nativo': 43, 'b_exotico': 57, 'propietario': 'BNDJKSABNDJKSA', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R6', 'SE': 'R4', 'SW': ''}}
}

afectados = set()

def simular_incendio(direccion_viento: str, rodal_inicial: str):

    vuelta = 1
    direcciones_afectadas = {
        'N': ['N'],
        'NE': ['NE'],
        'SE': ['NE'],
        'S': ['S'],
        'SW': ['SW'],
        'NW': ['NW'],
        'W': ['NW', 'SW'],
        'E': ['NE', 'SE']
    }

    if rodal_inicial == '':
        return

    if rodal_inicial != '':

        afectados.add(rodal_inicial)
        for i in direcciones_afectadas[direccion_viento]:
            match vuelta:
                case 1:
                    siguiente_rodal_1 = dicc_rodales[rodal_inicial]['colindancias'][i]
                
                case 2:
                    siguiente_rodal_2 = dicc_rodales[rodal_inicial]['colindancias'][i]

            vuelta += 1

    if direccion_viento in ['E', 'W']:
        return (
            simular_incendio(direccion_viento, siguiente_rodal_1),
            simular_incendio(direccion_viento, siguiente_rodal_2)
        )
    
    else:
        return simular_incendio(direccion_viento, siguiente_rodal_1)
    

def main():

    simular_incendio('W', 'R5')
    print(afectados)

if __name__ == '__main__':
    main()