import streamlit as st

st.set_page_config(page_title="SQL Regex Builder", page_icon="🔍", layout="centered")

st.title("🔍 Generador de consulta SQL con REGEXP")

# Campos de entrada
column = st.text_input("COLUMN", placeholder="Ejemplo: COLUMNA")
ds = st.text_input("DS (Data Source)", placeholder="Ejemplo: datasource.img.abc")
regex = st.text_area("REGEX", placeholder=r"Ejemplo: (?i)\b(\sagua)\b")

# Inicialización de variables de estado
if "output" not in st.session_state:
    st.session_state.output = ""

# Botones
col1, col2 = st.columns(2)
with col1:
    generate = st.button("Generar SQL")
with col2:
    clear = st.button("Limpiar campos")

# Lógica
if generate:
    if column and ds and regex:
        escaped_regex = regex.replace("\\", "\\\\")
        query = f"SELECT {column}\nFROM {ds}\nWHERE {column} REGEXP \n'{escaped_regex}'"
        st.session_state.output = query
    else:
        st.warning("Completa todos los campos antes de generar la consulta.")

if clear:
    column = ""
    ds = ""
    regex = ""
    st.session_state.output = ""
    st.experimental_rerun()

# Mostrar resultado
if st.session_state.output:
    st.subheader("Resultado:")
    st.code(st.session_state.output, language="sql")
