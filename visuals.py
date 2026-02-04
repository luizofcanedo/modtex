import streamlit as st

def html_delta(valor):
    
    cor = "#09ab3b" if valor >= 0 else "#ff2b2b" # Verde ou Vermelho
    seta = "↑" if valor >= 0 else "↓"
    
    return f"""
    <span style="
        color: {cor};
        font-weight: bold;
        background-color: {cor}15; /* 15% de transparência no fundo (efeito badge) */
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.9em;
    ">
        {seta} {valor:.2f}
    </span>
    """

def links_logos(marca_alvo):
    links = {
        'Fiat': "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Fiat_logo.svg/1280px-Fiat_logo.svg.png",
        'Jeep': "https://www.nicepng.com/png/full/425-4251525_new-chrysler-logo-png-wwwimgkidcom-the-image-kid.png",
        'Peugeot': "https://upload.wikimedia.org/wikipedia/en/thumb/9/9d/Peugeot_2021_Logo.svg/1280px-Peugeot_2021_Logo.svg.png",
        'Citroen': "https://images.seeklogo.com/logo-png/18/2/citroen-2009-logo-png_seeklogo-189184.png",
        'Ram': "https://logohistory.net/wp-content/uploads/2023/01/Ram-Logo-1993.png",
    }
    return links.get(marca_alvo)

def coes_marcas(marca_alvo):
    cores = {
        'Fiat': "red",
        'Jeep': "gray",
        'Peugeot': "gray",
        'Citroen': "red",
        'Ram': "red",
    }
    return cores.get(marca_alvo)