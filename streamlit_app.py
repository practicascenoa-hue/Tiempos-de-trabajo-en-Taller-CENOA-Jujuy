import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Taller CENOA - Seguimiento", layout="wide")

st.title("🚗 Seguimiento de Reparaciones - Taller CENOA Jujuy")

# Crear la conexión
conn = st.connection("gsheets", type=GSheetsConnection)

# Leer los datos
# Nota: "ttl=600" actualiza los datos cada 10 minutos
df = conn.read(ttl=600)

# Mostrar los datos en una tabla linda
st.write("Estado actual de los vehículos en taller:")
st.dataframe(df, use_container_width=True)

# Buscador opcional por Patente o Cliente
busqueda = st.text_input("Buscar por Patente o Cliente")
if busqueda:
    df_filtrado = df[df.astype(str).apply(lambda x: busqueda.lower() in x.str.lower().values, axis=1)]
    st.write("Resultados encontrados:")
    st.table(df_filtrado)
