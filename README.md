🤖 Asistente Académico con LLM

Aplicación desarrollada en Python utilizando Streamlit y Google Gemini para apoyar tareas académicas mediante modelos de lenguaje (LLM).

📚 Descripción

Este proyecto implementa un asistente académico basado en Inteligencia Artificial capaz de:

Resumir textos.
Explicar conceptos.
Generar preguntas de evaluación.
Corregir respuestas de estudiantes.
Proporcionar retroalimentación académica.
Clasificar textos según su propósito.

El objetivo es demostrar cómo integrar modelos LLM dentro de aplicaciones web utilizando Python y Streamlit.

🚀 Tecnologías utilizadas
Python
Streamlit
Google Gemini API
Google GenAI SDK
⚙️ Funcionalidades
📄 Resumir texto

Genera un resumen claro y estructurado a partir de un texto ingresado por el usuario.

📘 Explicar concepto

Explica conceptos académicos incluyendo:

Definición
Explicación sencilla
Ejemplo aplicado
Importancia del concepto

📝 Generar preguntas

Genera automáticamente:

Preguntas teóricas
Preguntas aplicadas
Preguntas de análisis

✅ Corregir respuesta

Evalúa respuestas de estudiantes proporcionando:

Comentarios generales
Aspectos correctos
Aspectos por mejorar
Nota sugerida (0–20)
💬 Retroalimentar texto

Analiza textos y proporciona recomendaciones de mejora.

🏷️ Clasificar texto

Clasifica textos en categorías como:

Explicativo
Argumentativo
Descriptivo
Crítico
Técnico

📂 Estructura del proyecto

LLM-Demo/
│
├── app.py
├── requirements.txt
├── README.md

📦 Instalación local

1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/LLM-Demo.git
cd LLM-Demo
2. Instalar dependencias
pip install -r requirements.txt
3. Ejecutar la aplicación
streamlit run app.py

La aplicación estará disponible en:

http://localhost:8501

🔑 Configuración de la API Key de Gemini

La aplicación utiliza la API de Google Gemini.

Obtener una API Key
Ingresar a Google AI Studio:

https://aistudio.google.com

Seleccionar Get API Key.
Crear una nueva API Key.
Copiar la clave generada.
☁️ Despliegue en Streamlit Cloud
1. Crear aplicación
Ingresar a Streamlit Cloud.
Seleccionar el repositorio GitHub.
Seleccionar:
Repository: TU_REPOSITORIO
Branch: main
Main file path: app.py
2. Configurar Secrets

Antes de desplegar:

Hacer clic en Advanced settings.
Ubicar la sección Secrets.
Agregar:
GEMINI_API_KEY = "TU_API_KEY_DE_GEMINI"

Ejemplo:

GEMINI_API_KEY = "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXX"
3. Desplegar

Presionar:

Deploy
🔒 Seguridad

No almacenar nunca la API Key directamente en:

app.py
GitHub
README

La aplicación obtiene la clave mediante:

st.secrets["GEMINI_API_KEY"]

lo que permite mantener las credenciales protegidas.

📄 Archivo requirements.txt
streamlit
google-genai
🎯 Objetivos de aprendizaje

Este proyecto permite comprender:

Large Language Models (LLM)
Prompt Engineering
Integración de APIs de IA
Desarrollo de aplicaciones con Streamlit
Despliegue de aplicaciones en la nube
Buenas prácticas de seguridad con Secrets
👨‍🏫 Autor

Mg. Sc. Aldo Richard Meza Rodríguez

Universidad Nacional Agraria La Molina

Curso: Ciencia de Datos II

Tema: Large Language Models (LLM) y Prompt Engineering
