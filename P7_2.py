import pandas as pd
import plotly.express as px
import streamlit as st

#titulo
st.header("VISUALIZACIÓN INFORMACIÓN SOBRE COCHES EN VENTA")

st.divider()

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.markdown("Análisis de información: *seleccione la variable de su interés*")

#seleccionador de variables
opciones=list(car_data.columns)[0:12]

v = st.multiselect(
    label = "Seleccione máximo 2 variables:",
    options = opciones,
    max_selections = 2)

# Boton de ejecutar
informacion = st.button(
    label = "Crear gráfico"
)

st.divider()
if informacion:
    try:
     hist_plot01 = px.histogram(car_data, x = v[0], title = f"Distribución {v[0]}", color = "type")
     st.plotly_chart(hist_plot01, use_container_width=True)
       
     hist_plot02 = px.scatter(car_data, x = v[1], title = f"Distribución {v[1]}", color = "type")
     st.plotly_chart(hist_plot02, use_container_width=True)
    except:
       st.write("Faltan variables por seleccionar")

st.divider()

st.header("Coches eléctricos")
# Boton de ejecutar
electricos = st.button(
    label = "Mostrar información coches eléctricos")

filtro=car_data["fuel"]=="electric"

if electricos:
    st.write("Información de coches eléctricos:")
    st.dataframe(car_data[filtro])

df_electricos = car_data[filtro]

# Boton mostrar gráfico
electricos2 = st.button(
    label = "Mostrar gráfico de coches eléctricos")

if electricos2: 
     fig = px.histogram(df_electricos, x="model_year", color="model", title="Distribución de coches eléctricos por año")
     st.plotly_chart(fig, use_container_width=True)
     st.write(f" Total de coches eléctricos: {len(df_electricos)}")

st.divider()

st.header("Visualizacion información por tipo de coche")
#seleccionador de variables
opciones = car_data["type"].unique().tolist()

seleccion = st.multiselect(
    label = "Seleccione tipo de coche:",
    options = opciones,
    max_selections = 1)

# Boton de ejecutar
info = st.button(
    label = "listado"
)

st.divider()

if info:
    if len(seleccion) == 0:
        st.warning("Selecciona al menos un tipo de coche.")
    else:
        df_info = car_data[car_data["type"].isin(seleccion)]
        st.write(" Listado de coches según el tipo seleccionado:")
        st.dataframe(df_info)
      

       