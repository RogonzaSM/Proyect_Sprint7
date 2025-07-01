import streamlit as st
import pandas as pd
import plotly.express as px

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis interactivo de anuncios de venta de coches en EE.UU.')

# Botón para histograma
if st.button('Mostrar histograma de odómetro'):
    st.write('Creando histograma de kilometraje (odómetro)...')
    fig = px.histogram(car_data, x='odometer', title='Distribución del odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión precio vs. kilometraje'):
    st.write('Creando gráfico de dispersión...')
    fig2 = px.scatter(car_data, x='odometer', y='price', color='type', 
                      title='Precio vs. Kilometraje por tipo de coche')
    st.plotly_chart(fig2, use_container_width=True)

#Version con checkboxes
if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Mostrando histograma...')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar gráfico de dispersión precio vs. kilometraje'):
    st.write('Mostrando gráfico de dispersión...')
    fig2 = px.scatter(car_data, x='odometer', y='price', color='type')
    st.plotly_chart(fig2, use_container_width=True)
