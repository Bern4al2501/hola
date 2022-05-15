informacion = {
    'id_cliente' : 1,
    'nombre': 'Juan',
    'edad' :3,
    'primer_ingreso' : False
}

def cliente (informacion:dict):
    diccionario = {}
    diccionario['Apto'] = True
    if informacion ['edad'] > 18:
        diccionario['Atraccion'] = 'Extreme'
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        diccionario['Atraccion'] = 'Carros Chocones'
    elif informacion['edad'] >= 7 and informacion['edad'] <= 15:
        diccionario['Atraccion'] = 'Sillas Voladoras'
    else :
        diccionario['Apto'] = False
        diccionario['Atraccion'] = 'N/A'
        diccionario['total_boleta'] = 'N/A'
    if informacion['primer_ingreso'] == True and diccionario['Atraccion'] == 'Extreme':
        diccionario['total_boleta'] = 20000 - 1000
    elif informacion['primer_ingreso'] == True and diccionario['Atraccion'] == 'Carros Chocones':
        diccionario['total_boleta'] = 5000 - 350
    elif informacion['primer_ingreso'] == True and diccionario['Atraccion'] == 'Sillas Voladoras':
        diccionario['total_boleta'] = 10000 - 500 
    if informacion['primer_ingreso'] == False and diccionario ['Atraccion'] == 'Extreme':
        diccionario['total_boleta'] = 20000
    elif informacion['primer_ingreso'] == False and diccionario['Atraccion'] == 'Carros Chocones':
        diccionario['total_boleta'] = 5000
    elif informacion['primer_ingreso'] == False and diccionario['Atraccion'] == 'Sillas Voladoras':
        diccionario['total_boleta'] = 10000
   

    diccionario1 = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion':diccionario['Atraccion'], 'apto': diccionario['Apto'], 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': diccionario['total_boleta']}
    return diccionario1

print(cliente(informacion))