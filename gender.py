import pandas as pd
import gender_guesser.detector as gender

# Crear detector de género
d = gender.Detector()

# Leer el archivo Excel (ajusta la ruta según sea necesario)
df = pd.read_excel('archivo.xlsx')

# Función para identificar género
def identificar_genero(nombre):
    primer_nombre = nombre.split()[0]  # Solo analizamos el primer nombre
    genero = d.get_gender(primer_nombre)
    
    if genero in ['male', 'mostly_male']:
        return 'Masculino'
    elif genero in ['female', 'mostly_female']:
        return 'Femenino'
    else:
        return 'Desconocido'

# Aplicar la función a la columna de nombres
df['Género'] = df['NOMBRE'].apply(identificar_genero)

# Guardar los resultados en un nuevo archivo
df.to_excel('archivo_con_genero.xlsx', index=False)

print("Archivo generado correctamente.")
