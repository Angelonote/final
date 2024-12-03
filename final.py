import streamlit as st
import pandas as pd

# Cargar los datos
file_path = 'Sean_P_diddy_Combs_final.csv'  
data = pd.read_csv(file_path, encoding='latin1')

# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Buscador de Información</h1>", unsafe_allow_html=True)

# Paso 1: Seleccionar el Rol
roles = data['Rol'].dropna().unique()  # Obtener roles únicos
rol_seleccionado = st.selectbox("Selecciona un Rol:", roles)

# Filtrar por el Rol seleccionado
datos_filtrados = data[data['Rol'] == rol_seleccionado]
# Creamos una nueva columna combinada para mostrar nombre y apellido juntos
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
        st.write(f"- **Acusación/Cargo:** {row['Acusacion/Cargo']}")
        st.write(f"- **Fuente:** [Ver Fuente]({row['Fuente']})")
        st.write("---")
else:
    st.write("No se encontró información para esta selección.")
