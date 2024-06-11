import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
def main():
    # Chemin de l'image du logo
    logo_path = "logoRetro.png"
    
    # Convertir l'image en base64
    logo_base64 = get_image_base64(logo_path)
    
    # Ajout de CSS pour les styles et animations
    st.markdown("""
    <style>
    body {
        color: #fff;
        background-color: #000000; 
    }
    .big-font {
        font-size: 40px !important;
        font-weight: bold;
        color: #f9d342;  /* Couleur du titre en jaune */
    }
    @keyframes blinker {
        50% { opacity: 0; }
    }
    h2 {
        color: #ffffff;
    }
    .logo-container {
        position: absolute;
        top: 10px;
        right: 10px;
        width: 150px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Contenu de la page
    st.markdown('<div class="big-font">Automatisation des données GA4 de Retro Photo</div>', unsafe_allow_html=True)
    st.markdown("""
    ## Description de l'application
    Cette application permet une **analyse approfondie des données GA4** pour Retro Photo, une entreprise spécialisée dans la vente de cartes postales d'anciennes photos. En exploitant les données de leur site web, cette application aide à visualiser et analyser le comportement des utilisateurs, l'engagement sur le site, et les performances des différentes pages.
    """, unsafe_allow_html=True)
    
    # Affichage du logo en haut à droite
    st.markdown(f'<div class="logo-container"><img src="data:image/png;base64,{logo_base64}" alt="Logo"></div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
