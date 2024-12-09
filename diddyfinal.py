import streamlit as st
import pandas as pd
from PIL import Image

# Cargar los datos
file_path = 'diddydatosfinal.csv'  # Archivo de datos
data = pd.read_csv(file_path, encoding='latin1')

# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Buscador de Información</h1>", unsafe_allow_html=True)

# Paso 1: Seleccionar el Rol
roles = data['Rol'].dropna().unique()  # Obtener roles únicos
rol_seleccionado = st.selectbox("Selecciona un Rol:", roles)

# Filtrar por el Rol seleccionado
datos_filtrados = data[data['Rol'] == rol_seleccionado]

# Crear una nueva columna combinada para mostrar nombre y apellido juntos
datos_filtrados['Nombre Completo'] = datos_filtrados['Nombre'] + " " + datos_filtrados['Apellidos']

# Paso 2: Seleccionar el Nombre Completo
nombre_completo_seleccionado = st.selectbox("Selecciona un Nombre:", datos_filtrados['Nombre Completo'])

# Filtrar por el Nombre Completo seleccionado
datos_seleccionados = datos_filtrados[datos_filtrados['Nombre Completo'] == nombre_completo_seleccionado]

# Paso 3: Mostrar Información
if not datos_seleccionados.empty:
    st.markdown("### Detalles del Caso")
    for index, row in datos_seleccionados.iterrows():
        st.write(f"- **Nombre:** {row['Nombre']} {row['Apellidos']}")
        st.write(f"- **Sexo:** {row['Sexo']}")
        st.write(f"- **Edad:** {row['Edad']}")
        st.write(f"- **Año:** {row['Año']}")
        st.write(f"- **Acusación/Cargo:** {row['Acusacion/Cargo']}")
        st.write(f"- **Fuente:** [Ver Fuente]({row['Fuente']})")
        
        # Mostrar la foto si existe
        if pd.notna(row['Fotos']):
            foto_path = f"FOTOS/{row['Fotos']}"
            try:
                imagen = Image.open(foto_path)
                st.image(imagen, caption=f"Foto de {row['Nombre Completo']}", use_column_width=True)
            except FileNotFoundError:
                st.write("Foto no disponible.")
        else:
            st.write("Foto no disponible.")
        st.write("---")
else:
    st.write("No se encontró información para esta selección.")