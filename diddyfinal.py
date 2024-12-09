# Importar las librerías necesarias
import streamlit as st  # Para crear la interfaz de usuario
import pandas as pd  # Para cargar y manejar los datos
import matplotlib.pyplot as plt  # Para generar gráficas
from PIL import Image  # Para manejar y mostrar imágenes

# Cargar los datos
file_path = 'diddydatosfinal.csv'  # Ruta del archivo CSV
data = pd.read_csv(file_path, encoding='latin1')  # Cargar el CSV con la codificación adecuada

# --- INTRODUCCIÓN ---
# Mostrar una introducción extensa y detallada
st.markdown("""
# Buscador de Información
### Introducción
El caso de Sean Combs, conocido mundialmente como Puff Daddy o P. Diddy, representa una red compleja de crímenes que va más allá de su figura como ícono del entretenimiento. Este caso ha generado un interés masivo no solo por el peso mediático del propio Combs, sino por las múltiples conexiones personales, profesionales y sociales que emergen entre las personas involucradas. Desde las víctimas hasta los cómplices, cada actor desempeña un papel crucial que ayuda a construir la narrativa de los acontecimientos, h...
Nuestro enfoque no se limita a los personajes que habitualmente ocupan el centro del escenario. Reconocemos que detrás de los nombres más reconocidos existen otras figuras, menos visibles, pero igualmente importantes. Estas personas, cuyos roles suelen quedar opacados por el impacto mediático, pueden ofrecer perspectivas y detalles que son clave para entender el panorama completo. Aquí, buscamos arrojar luz sobre esas voces menos influyentes en el medio, pero no menos significativas en el desarrollo de l...
A través de cuadros comparativos, nuestra meta es estructurar y analizar las conexiones entre todos los implicados, trazando patrones y revelando relaciones tanto directas como indirectas. Estas herramientas visuales no solo permitirán identificar nexos claros, sino también explorar contextos que podrían pasar desapercibidos en una lectura superficial del caso.

En este espacio, invitamos a sumergirse en un análisis exhaustivo que prioriza tanto los detalles públicos como los menos conocidos, contribuyendo a una comprensión integral y matizada. Creemos que cada pieza, por pequeña que parezca, es esencial para construir un cuadro completo y justo de lo ocurrido. ¡Acompáñanos a descubrir las conexiones que cuentan toda la historia!
""")

# --- FILTROS INTERACTIVOS ---
# Paso 1: Seleccionar el Rol
roles = data['Rol'].dropna().unique()  # Obtener roles únicos del dataset
rol_seleccionado = st.selectbox("Selecciona un Rol:", roles)  # Menú desplegable para seleccionar un rol

# Filtrar por el Rol seleccionado
datos_filtrados = data[data['Rol'] == rol_seleccionado]  # Filtrar los datos por el rol seleccionado

# Crear una columna combinada para mostrar nombre completo
datos_filtrados['Nombre Completo'] = datos_filtrados['Nombre'] + " " + datos_filtrados['Apellidos']

# Paso 2: Seleccionar el Nombre Completo
nombre_completo_seleccionado = st.selectbox("Selecciona un Nombre:", datos_filtrados['Nombre Completo'])

# Filtrar por el Nombre Completo seleccionado
datos_seleccionados = datos_filtrados[datos_filtrados['Nombre Completo'] == nombre_completo_seleccionado]

# --- VISUALIZAR DETALLES ---
if not datos_seleccionados.empty:  # Verificar si los datos seleccionados no están vacíos
    st.markdown("### Detalles del Caso")
    for index, row in datos_seleccionados.iterrows():
        st.write(f"- **Nombre:** {row['Nombre']} {row['Apellidos']}")
        st.write(f"- **Sexo:** {row['Sexo']}")
        st.write(f"- **Edad:** {row['Edad']}")
        st.write(f"- **Año:** {row['Año']}")
        st.write(f"- **Acusación/Cargo:** {row['Acusacion/Cargo']}")
        st.write(f"- **Fuente:** [Ver Fuente]({row['Fuente']})")
        
        # Mostrar imagen si está disponible
        if pd.notna(row['Fotos']):
            foto_path = f"FOTOS/{row['Fotos']}"  # Ruta de la imagen
            try:
                imagen = Image.open(foto_path)
                st.image(imagen, caption=f"Foto de {row['Nombre Completo']}", use_column_width=True)
            except FileNotFoundError:
                st.write("Foto no disponible.")
        else:
            st.write("Foto no disponible.")
        st.write("---")

# --- GRÁFICAS COMPARATIVAS ---
st.markdown("### Gráficas Comparativas")

# Gráfico de edades por rol (por ejemplo, víctimas)
if 'Edad' in data.columns and 'Rol' in data.columns:
    fig, ax = plt.subplots()
    data[data['Rol'] == 'Victima']['Edad'].hist(ax=ax, bins=10, color='blue', alpha=0.7)
    ax.set_title('Distribución de Edades de las Víctimas')
    ax.set_xlabel('Edad')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

# Gráfico de edades por rol (por ejemplo, agresores)
if 'Edad' in data.columns and 'Rol' in data.columns:
    fig, ax = plt.subplots()
    data[data['Rol'] == 'Agresor']['Edad'].hist(ax=ax, bins=10, color='red', alpha=0.7)
    ax.set_title('Distribución de Edades de los Agresores')
    ax.set_xlabel('Edad')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

# --- PROPUESTA ADICIONAL ---
st.markdown("### Análisis Adicional: Distribución por Género y Rol")
roles_generos = data.groupby(['Rol', 'Sexo']).size().unstack(fill_value=0)  # Agrupar por rol y género
st.table(roles_generos)  # Mostrar tabla comparativa

# Gráfico de barras para la distribución de género y rol
fig, ax = plt.subplots()
roles_generos.plot(kind='bar', ax=ax, stacked=True, color=['blue', 'orange'])
ax.set_title('Distribución de Género por Rol')
ax.set_xlabel('Rol')
ax.set_ylabel('Cantidad')
st.pyplot(fig)
