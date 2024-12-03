import streamlit as st
import pandas as pd

# Cargar los datos
file_path = 'Sean_P_diddy_Combs_final.csv'  
data = pd.read_csv(file_path, encoding='latin1')
# En esta sección estamos cargando el archivo CSV que contiene la información de los casos.
# Especificamos la codificación 'latin1' para evitar problemas con caracteres especiales.

# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Buscador de Información</h1>", unsafe_allow_html=True)
# Aquí agregamos un título centrado utilizando Markdown y HTML. 
# El argumento `unsafe_allow_html=True` nos permite personalizar el texto con HTML.

# Paso 1: Seleccionar el Rol
roles = data['Rol'].dropna().unique()  # Obtener roles únicos
rol_seleccionado = st.selectbox("Selecciona un Rol:", roles)
# Creamos un cuadro desplegable (`selectbox`) para que el usuario seleccione un rol. 
# Los roles únicos se extraen directamente de los datos.

# Filtrar por el Rol seleccionado
nombres_filtrados = data[data['Rol'] == rol_seleccionado]['Nombre']
# Filtramos los nombres basándonos en el rol seleccionado por el usuario.
# Esto nos permite mostrar solo los nombres relacionados con ese rol.

# Paso 2: Seleccionar el Nombre
nombre_seleccionado = st.selectbox("Selecciona un Nombre:", nombres_filtrados)
# Creamos otro cuadro desplegable para que el usuario seleccione un nombre.
# Esta lista depende del rol que haya elegido previamente.

# Filtrar por el Nombre seleccionado
datos_seleccionados = data[(data['Rol'] == rol_seleccionado) & (data['Nombre'] == nombre_seleccionado)]
# Filtramos los datos para obtener la información específica de la persona seleccionada,
# combinando el rol y el nombre como criterios.

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
# Si encontramos información sobre la persona seleccionada, la mostramos en formato de lista.
# Incluimos detalles como nombre, sexo, edad, cargo o acusación, y un enlace a la fuente.

else:
    st.write("No se encontró información para esta selección.")
# Si no se encuentran datos, mostramos un mensaje para indicarlo.
