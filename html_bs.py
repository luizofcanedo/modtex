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