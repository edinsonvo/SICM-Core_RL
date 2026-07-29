import streamlit as st

from sicm_core import __version__

st.set_page_config(
    page_title="SICM Research Lab",
    layout="wide",
)

st.title("SICM Research Lab")

st.success(f"SICM Core {__version__} cargado correctamente.")

st.markdown(
    """
    ## Bienvenido

    Esta es la plataforma de investigación macroeconómica
    desarrollada sobre SICM Core.
    """
)

st.divider()

st.caption(
    "© Patrocinio Valencia • edvalenciao@unal.edu.co"
)
