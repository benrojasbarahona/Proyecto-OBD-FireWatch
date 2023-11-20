    print(f"\nResumen del rodal ingresado:\nID: {id_rodal}\nPropietario: {propietario}\n% Bosque nativo: {pb_nativo}\n% Bosque exótico: {pb_exotico}")
                try: 
                    print(f"Se encuentra al {referencia_coordenadas[info_colin]} de {rodal_colindante}\n")
                    asignar_colindancias(id_rodal, rodal_colindante, info_colin)
                except UnboundLocalError: pass

                generar_rodal(
                    id_rodal, propietario, pb_nativo, pb_exotico,
                    colin_N = colin_norte, colin_NE = colin_noreste, colin_NW = colin_noroeste,
                    colin_S = colin_sur, colin_SE = colin_sureste, colin_SW = colin_suroeste
                )

                for key,value in dicc_rodales.items():
                    print(f"{key}   :   {value}")