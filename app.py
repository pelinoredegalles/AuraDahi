import streamlit as st
from PIL import Image
import os
import json

st.set_page_config(page_title="Aura Dahi - Velas Artesanales", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        body {
            background-color: #F5F1ED;
        }
        .header {
            text-align: center;
            color: #9B8B7E;
            margin-bottom: 20px;
        }
        .product-card {
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            background-color: #F0EAE3;
            margin: 10px;
            color: #9B8B7E;
        }
        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 30px 0;
            flex-wrap: wrap;
        }
        .btn-link {
            display: inline-block;
            padding: 16px 50px;
            margin: 10px;
            background-color: #9B8B7E;
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            font-size: 18px;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            border: 2px solid #9B8B7E;
        }
        .btn-link:hover {
            background-color: #7A6E65;
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        .description {
            color: #555;
            font-size: 16px;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    try:
        logo = Image.open("logo.jpg")
        st.image(logo, use_container_width=True, width=300)
    except FileNotFoundError:
        st.markdown("<div class='header'><h1>🕯️ Aura Dahi</h1></div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='description' style='text-align: center; color: #9B8B7E;'>
            <p>✨ Velas 100% soja artesanales ✨</p>
            <p>🪔 Adornos cerámicos únicos</p>
            <p>🎉 Creaciones para eventos y días especiales</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2 style='text-align: center; color: #9B8B7E;'>Nuestras Creaciones</h2>", unsafe_allow_html=True)

with open('produits.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    productos = data['productos']

for i in range(0, len(productos), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(productos):
            producto = productos[i + j]
            with col:
                try:
                    img = Image.open(producto['imagen'])
                    st.image(img, use_container_width=True)
                    st.markdown(f"<div class='product-card'><h4>{producto['nombre']}</h4><p>{producto['descripcion']}</p></div>", unsafe_allow_html=True)
                except FileNotFoundError:
                    st.warning(f"Imagen {producto['imagen']} no encontrada")

st.markdown("---")

st.markdown("<h2 style='text-align: center; color: #9B8B7E;'>Contáctanos</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style='text-align: center;'>
            <p><strong>📍 Ubicación:</strong></p>
            <p>Fuengirola</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='text-align: center;'>
            <a href='https://www.instagram.com/auradahi/' target='_blank' class='btn-link'>📸 Instagram</a>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='text-align: center;'>
            <a href='https://wa.me/34611822813' target='_blank' class='btn-link'>💬 WhatsApp</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; margin-top: 40px; color: #999;'>
        <p><small>Consulta precios, entregas y personalizaciones por DM 📩</small></p>
    </div>
""", unsafe_allow_html=True)
