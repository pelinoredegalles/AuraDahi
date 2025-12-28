import streamlit as st
from PIL import Image
import json


def resize_image_fit(image_path, size=300):
    img = Image.open(image_path)
    img.thumbnail((size, size), Image.Resampling.LANCZOS)
    
    background = Image.new('RGB', (size, size), color=(245, 241, 237))
    offset = ((size - img.width) // 2, (size - img.height) // 2)
    background.paste(img, offset)
    
    return background

st.set_page_config(page_title="Aura Dahi - Creaciones Artesanales", layout="wide", initial_sidebar_state="collapsed")

with st.sidebar:
    st.markdown("<h2 style='color: #9B8B7E; text-align: center;'>🕯️ Aura Dahi</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    page = st.radio(
        "Menú",
        ["🏠 Inicio", "🪔 Cómo Hacemos"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #9B8B7E;'>
            <p><strong>📍 Fuengirola</strong></p>
            <p><small>🕯️ Velas 100% soja artesanales</small></p>
            <p><small>🪔 Adornos cerámicos únicos</small></p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; font-size: 12px; color: #9B8B7E;'>
            <p style='margin: 5px 0;'><a href='https://www.instagram.com/auradahi/' target='_blank' style='color: #9B8B7E; text-decoration: none;'>📸 Instagram</a></p>
            <p style='margin: 5px 0;'><a href='https://wa.me/34611822813' target='_blank' style='color: #9B8B7E; text-decoration: none;'>💬 WhatsApp</a></p>
        </div>
    """, unsafe_allow_html=True)

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
        .section-card {
            padding: 30px;
            border-radius: 10px;
            background-color: #F0EAE3;
            margin: 20px 0;
            border-left: 5px solid #9B8B7E;
            color: #555;
        }
        .section-title {
            font-size: 24px;
            font-weight: bold;
            color: #9B8B7E;
            margin-bottom: 15px;
        }
        .process-step {
            display: flex;
            align-items: center;
            margin: 20px 0;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            border: 1px solid #E8DDD5;
        }
        .step-number {
            font-size: 32px;
            font-weight: bold;
            color: #9B8B7E;
            width: 60px;
            text-align: center;
        }
        .step-content {
            margin-left: 20px;
            flex-grow: 1;
        }
        .step-title {
            font-size: 18px;
            font-weight: bold;
            color: #9B8B7E;
            margin-bottom: 8px;
        }
        .step-description {
            color: #555;
            line-height: 1.6;
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

if page == "🏠 Inicio":
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        try:
            logo = Image.open("data/logo.jpg")
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

    st.markdown("""
        <div class='description' style='text-align: center; color: #9B8B7E; margin: 40px 0;'>
            <h2>Bienvenido a Aura Dahi</h2>
            <p style='font-size: 18px;'>Descubre nuestras creaciones artesanales hechas con pasión y los mejores materiales.</p>
            <p>Cada vela es única, creada especialmente para ti y tus seres queridos.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("<h2 style='text-align: center; color: #9B8B7E;'>🕯️ Nuestras Creaciones</h2>", unsafe_allow_html=True)

    if "filtro_categoria" not in st.session_state:
        st.session_state.filtro_categoria = "todos"

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Todos", use_container_width=True, key="btn_todos"):
            st.session_state.filtro_categoria = "todos"
    with col2:
        if st.button("🕯️ Velas", use_container_width=True, key="btn_velas_inicio"):
            st.session_state.filtro_categoria = "velas"
    with col3:
        if st.button("🪔 Cerámicas", use_container_width=True, key="btn_ceramicas_inicio"):
            st.session_state.filtro_categoria = "ceramicas"
    with col4:
        st.empty()

    st.markdown("---")

    with open('data/produits.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        productos = data['productos']

    if st.session_state.filtro_categoria == "todos":
        productos_filtrados = productos
    else:
        productos_filtrados = [p for p in productos if p.get('categoria') == st.session_state.filtro_categoria]

    if len(productos_filtrados) == 0:
        st.markdown("<p style='text-align: center; color: #9B8B7E;'>No hay creaciones en esta categoría</p>", unsafe_allow_html=True)
    else:
        for i in range(0, len(productos_filtrados), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(productos_filtrados):
                    producto = productos_filtrados[i + j]
                    with col:
                        try:
                            img = resize_image_fit(f"data/{producto['imagen']}", size=300)
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

else:
    st.markdown("<h1 style='text-align: center; color: #9B8B7E;'>✨ Como Hacemos Nuestras Creaciones</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: center; color: #9B8B7E; margin: 30px 0;'>
            <p style='font-size: 18px;'>Cada creacion Aura Dahi es realizada con dedicacion, pasion y los mejores materiales.</p>
            <p>Aqui te mostramos nuestro proceso artesanal paso a paso.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tipo_col1, tipo_col2 = st.columns(2)
        with tipo_col1:
            if st.button("🕯️ Velas", use_container_width=True, key="btn_velas"):
                st.session_state.tipo_creacion = "velas"
        with tipo_col2:
            if st.button("🪔 Cerámicas", use_container_width=True, key="btn_ceramicas"):
                st.session_state.tipo_creacion = "ceramicas"
    
    if "tipo_creacion" not in st.session_state:
        st.session_state.tipo_creacion = "velas"

    st.markdown("---")

    if st.session_state.tipo_creacion == "velas":
        st.markdown("""
            <div class='section-card'>
                <div class='section-title'>📋 Proceso de Creacion de Velas</div>
                <p>Nuestras velas 100% soja son creadas mediante un proceso artesanal cuidadoso que garantiza la maxima calidad y durabilidad.</p>
            </div>
        """, unsafe_allow_html=True)

        steps = [
            ("Seleccion de Cera", "Comenzamos con cera de soja 100% pura, una fuente renovable y sostenible que ofrece el mejor rendimiento."),
            ("Preparacion de la Cera", "La cera se funde suavemente a la temperatura exacta para mantener todas sus propiedades naturales y conseguir una textura perfecta."),
            ("Mezcla de Fragancias", "Las fragancias de alta calidad se mezclan cuidadosamente con la cera para garantizar una distribucion uniforme del aroma en toda la vela."),
            ("Seleccion del Adorno", "Elegimos adornos ceramicos artesanales unicos que complementen perfectamente cada vela."),
            ("Vertido en Moldes", "Vertemos la cera con el adorno ceramico en moldes especiales. Cada vela se crea manualmente con amor y atencion."),
            ("Enfriamiento y Curado", "Las velas se dejan enfriar lentamente durante 24-48 horas en condiciones controladas para que fraguen correctamente y adquieran su dureza ideal."),
            ("Control de Calidad", "Cada vela pasa por un riguroso control de calidad para verificar su fragancia, color, dureza y presentacion."),
            ("Empaque Cuidadoso", "Las velas se empacan cuidadosamente con proteccion especial para garantizar que lleguen en perfecto estado a tu hogar.")
        ]

        for idx, (title, desc) in enumerate(steps, 1):
            st.markdown(f"""
                <div class='process-step'>
                    <div class='step-number'>{idx}</div>
                    <div class='step-content'>
                        <div class='step-title'>{title}</div>
                        <div class='step-description'>{desc}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.markdown("""
            <div class='section-card'>
                <div class='section-title'>🎨 Proceso de Creacion de Ceramicas</div>
                <p>Cada adorno ceramico es una pieza unica creada con tecnicas artesanales tradicionales y dedicacion especial.</p>
            </div>
        """, unsafe_allow_html=True)

        ceramic_steps = [
            ("Diseno y Conceptualizacion", "Comenzamos con la idea de crear adornos unicos. Diseñamos cada pieza considerando armonia, belleza y su compatibilidad con nuestras velas."),
            ("Preparacion de la Arcilla", "Seleccionamos arcilla de alta calidad y la preparamos cuidadosamente, asegurandonos de que este libre de impurezas y lista para moldear."),
            ("Moldeo Manual", "Cada adorno es moldeado completamente a mano. Utilizamos tecnicas tradicionales de alfareria para crear formas hermosas y funcionales."),
            ("Texturizado y Detalles", "Añadimos texturas y detalles especiales a cada pieza, creando patrones unicos que hacen que cada adorno sea irrepetible y especial."),
            ("Secado Cuidadoso", "Las piezas se dejan secar lentamente en condiciones controladas durante varios dias para evitar fracturas y grietas."),
            ("Acabado y Pulido", "Pulimos cuidadosamente cada superficie para conseguir el acabado perfecto, eliminar asperezas y realzar la belleza natural de la arcilla."),
            ("Horneado a Alta Temperatura", "Las ceramicas se cocinan en horno a temperatura controlada, lo que les proporciona dureza y permite soportar el paso del tiempo."),
            ("Pintado y Esmalte Final", "Aplicamos pintura y esmalte artesanal a cada adorno, utilizando colores que crean armonia con nuestras velas y crean una estetica unica.")
        ]

        for idx, (title, desc) in enumerate(ceramic_steps, 1):
            st.markdown(f"""
                <div class='process-step'>
                    <div class='step-number'>{idx}</div>
                    <div class='step-content'>
                        <div class='step-title'>{title}</div>
                        <div class='step-description'>{desc}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class='section-card'>
                <div class='section-title'>🎨 Diseño Personalizado</div>
                <p>¿Tienes una idea especial? Podemos crear velas 100% personalizadas:</p>
                <ul style='margin-left: 20px; color: #555;'>
                    <li>Fragancias a tu gusto</li>
                    <li>Colores especificos</li>
                    <li>Diseños ceramicos unicos</li>
                    <li>Tamaños personalizados</li>
                    <li>Para eventos especiales</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class='section-card'>
                <div class='section-title'>♻️ Compromiso Sostenible</div>
                <p>Nos comprometemos con el medio ambiente:</p>
                <ul style='margin-left: 20px; color: #555;'>
                    <li>100% cera de soja renovable</li>
                    <li>Adornos reutilizables</li>
                    <li>Empaque ecologico</li>
                    <li>Sin quimicos toxicos</li>
                    <li>Produccion responsable</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
        <div style='text-align: center; color: #9B8B7E; margin: 40px 0;'>
            <h2>🌟 ¿Por que somos diferentes?</h2>
            <p>Porque no solo vendemos velas, vendemos emociones y momentos especiales.</p>
            <p>Cada creacion lleva el corazon y la dedicacion de quien la hace.</p>
        </div>
    """, unsafe_allow_html=True)

    values = [
        ("❤️ Pasion", "Hacemos cada vela con amor y dedicacion"),
        ("🎯 Calidad", "Solo usamos los mejores materiales"),
        ("🎨 Creatividad", "Cada diseño es unico y especial"),
        ("♻️ Sostenibilidad", "Cuidamos el planeta con nuestros productos"),
        ("👥 Comunidad", "Somos un emprendimiento familiar"),
        ("✨ Autenticidad", "Lo que ves es lo que obtienes, sin trucos")
    ]

    cols = st.columns(3)
    for idx, (title, desc) in enumerate(values):
        with cols[idx % 3]:
            st.markdown(f"""
                <div style='padding: 20px; background-color: #F0EAE3; border-radius: 10px; text-align: center; margin: 10px 0; border: 1px solid #E8DDD5;'>
                    <strong style='color: #9B8B7E; font-size: 18px;'>{title}</strong>
                    <p style='color: #555; margin-top: 10px; font-size: 14px;'>{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
        <div style='text-align: center; color: #9B8B7E; margin: 40px 0;'>
            <h3>¿Quieres tu vela personalizada?</h3>
            <p>Contacta con nosotros para crear algo especial juntos.</p>
            <p style='font-size: 14px; margin-top: 20px;'><strong>Pedidos por DM • Consulta precios y entregas</strong></p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

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
