import streamlit as st
from google import genai

st.set_page_config(
    page_title="Asistente Académico con LLM",
    page_icon="🤖",
    layout="wide"
)

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def consultar_llm(prompt):
    respuesta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return respuesta.text

def resumir_texto(texto):
    prompt = f"""
Eres un asistente académico universitario.
Resume el siguiente texto en lenguaje claro, breve y ordenado.

Texto:
{texto}
"""
    return consultar_llm(prompt)

def explicar_concepto(concepto):
    prompt = f"""
Eres un docente universitario de Ciencia de Datos.
Explica el siguiente concepto de forma clara y sencilla.

Concepto:
{concepto}

Responde con:
1. Definición breve
2. Explicación simple
3. Ejemplo aplicado
4. Importancia en Ciencia de Datos
"""
    return consultar_llm(prompt)

def generar_preguntas(texto):
    prompt = f"""
Eres un docente universitario.
Genera 5 preguntas de evaluación sobre el siguiente contenido.

Contenido:
{texto}

Incluye:
- 2 preguntas teóricas
- 2 preguntas aplicadas
- 1 pregunta de análisis
"""
    return consultar_llm(prompt)

def corregir_respuesta(pregunta, respuesta_estudiante):
    prompt = f"""
Eres un evaluador académico universitario.

Pregunta:
{pregunta}

Respuesta del estudiante:
{respuesta_estudiante}

Devuelve:
1. Comentario general
2. Aspectos correctos
3. Aspectos por mejorar
4. Nota sugerida de 0 a 20
"""
    return consultar_llm(prompt)

def retroalimentar_texto(texto):
    prompt = f"""
Eres un asesor académico.
Brinda retroalimentación constructiva sobre el siguiente texto.

Texto:
{texto}

Devuelve:
1. Fortalezas
2. Debilidades
3. Recomendaciones de mejora
"""
    return consultar_llm(prompt)

def clasificar_texto(texto):
    prompt = f"""
Eres un analista de texto académico.
Clasifica el siguiente texto según su propósito principal.

Texto:
{texto}

Categorías:
- Explicativo
- Argumentativo
- Descriptivo
- Crítico
- Técnico

Justifica brevemente.
"""
    return consultar_llm(prompt)

st.title("🤖 Asistente Académico con LLM")
st.write("Aplicación educativa desarrollada con Python, Streamlit y Gemini.")

opcion = st.sidebar.selectbox(
    "Selecciona una tarea:",
    [
        "Resumir texto",
        "Explicar concepto",
        "Generar preguntas",
        "Corregir respuesta",
        "Retroalimentar texto",
        "Clasificar texto"
    ]
)

st.sidebar.info("Proyecto: LLM Foundations + Prompt Engineering")

if opcion == "Resumir texto":
    st.header("📄 Resumir texto")
    texto = st.text_area("Pega el texto:", height=250)

    if st.button("Generar resumen"):
        if texto.strip():
            with st.spinner("Generando resumen..."):
                st.write(resumir_texto(texto))
        else:
            st.warning("Ingresa un texto primero.")

elif opcion == "Explicar concepto":
    st.header("📘 Explicar concepto")
    concepto = st.text_input("Escribe el concepto:")

    if st.button("Explicar"):
        if concepto.strip():
            with st.spinner("Generando explicación..."):
                st.write(explicar_concepto(concepto))
        else:
            st.warning("Ingresa un concepto primero.")

elif opcion == "Generar preguntas":
    st.header("📝 Generar preguntas")
    texto = st.text_area("Pega el contenido de clase:", height=250)

    if st.button("Generar preguntas"):
        if texto.strip():
            with st.spinner("Generando preguntas..."):
                st.write(generar_preguntas(texto))
        else:
            st.warning("Ingresa un contenido primero.")

elif opcion == "Corregir respuesta":
    st.header("✅ Corregir respuesta")
    pregunta = st.text_area("Pregunta:", height=120)
    respuesta_estudiante = st.text_area("Respuesta del estudiante:", height=180)

    if st.button("Corregir"):
        if pregunta.strip() and respuesta_estudiante.strip():
            with st.spinner("Corrigiendo..."):
                st.write(corregir_respuesta(pregunta, respuesta_estudiante))
        else:
            st.warning("Completa la pregunta y la respuesta.")

elif opcion == "Retroalimentar texto":
    st.header("💬 Retroalimentar texto")
    texto = st.text_area("Pega el texto:", height=250)

    if st.button("Generar retroalimentación"):
        if texto.strip():
            with st.spinner("Generando retroalimentación..."):
                st.write(retroalimentar_texto(texto))
        else:
            st.warning("Ingresa un texto primero.")

elif opcion == "Clasificar texto":
    st.header("🏷️ Clasificar texto")
    texto = st.text_area("Pega el texto:", height=250)

    if st.button("Clasificar"):
        if texto.strip():
            with st.spinner("Clasificando..."):
                st.write(clasificar_texto(texto))
        else:
            st.warning("Ingresa un texto primero.")