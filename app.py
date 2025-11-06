import streamlit as st

st.set_page_config(page_title="SQL Regex Builder", page_icon="🔍", layout="centered")

st.title("🔍 Generador de consulta SQL con REGEXP")

# Inicializar variables de sesión
for key in ["column", "ds", "regex", "output"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# Función para limpiar los campos
def clear_fields():
    st.session_state.column = ""
    st.session_state.ds = ""
    st.session_state.regex = ""
    st.session_state.output = ""

# Entradas de usuario (vinculadas al estado de sesión)
st.session_state.column = st.text_input("COLUMN", value=st.session_state.column, placeholder="Ejemplo: COLUMNA")
st.session_state.ds = st.text_input("DS (Data Source)", value=st.session_state.ds, placeholder="Ejemplo: datasource.img.abc")
st.session_state.regex = st.text_area("REGEX", value=st.session_state.regex, placeholder=r"Ejemplo: (?i)\b(\sagua)\b")

# Botones
col1, col2 = st.columns(2)
with col1:
    generate = st.button("Generar SQL")
with col2:
    clear = st.button("Limpiar campos", on_click=clear_fields)

# Lógica de generación
if generate:
    if st.session_state.column and st.session_state.ds and st.session_state.regex:
        escaped_regex = st.session_state.regex.replace("\\", "\\\\")
        st.session_state.output = (
            f"SELECT {st.session_state.column}\n"
            f"FROM {st.session_state.ds}\n"
            f"WHERE {st.session_state.column} REGEXP \n"
            f"'{escaped_regex}'"
        )
    else:
        st.warning("Completa todos los campos antes de generar la consulta.")

# Mostrar resultado
if st.session_state.output:
    st.subheader("Resultado:")
    st.code(st.session_state.output, language="sql")
