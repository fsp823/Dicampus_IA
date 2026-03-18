📘 README — Analizador de Texto en Python
🧩 Descripción
Este proyecto es un analizador de texto en Python diseñado para extraer información útil a partir de documentos o cadenas de texto. Permite obtener estadísticas básicas, limpiar contenido, calcular frecuencias de palabras y realizar tareas iniciales de procesamiento de lenguaje natural (NLP).
Es una herramienta ligera, extensible y fácil de integrar en otros proyectos.

🚀 Características principales
Conteo total de palabras

Frecuencia de palabras más comunes

Eliminación de stopwords

Normalización del texto (minúsculas, signos, espacios)

Limpieza de caracteres especiales

Análisis de frases clave (opcional)

API interna sencilla de usar

Scripts listos para ejecutarse desde terminal

📂 Estructura del proyecto
Código
contador_palabras/
│── src/
│   └── contador.py      # Lógica principal del análisis
│── tests/
│   └── test_contador.py
|__ main.py
│── requirements.txt
│── README.md
🛠️ Instalación
Clona el repositorio y instala las dependencias:

bash
git clone https://github.com/usuario/analizador-texto.git
cd analizador-texto
pip install -r requirements.txt
▶️ Uso
📌 Desde Python
python
from analizador import AnalizadorTexto

texto = "Hola mundo. Hola Python."
analizador = AnalizadorTexto(texto)

print("Palabras:", analizador.contar_palabras())
print("Frecuencias:", analizador.frecuencia_palabras())
📌 Desde la terminal
bash
python main.py --archivo ejemplo.txt
Opciones disponibles:

Código
--archivo <ruta>     Analiza un archivo de texto
--limpio             Limpia el texto antes de analizarlo
--top <n>            Muestra las n palabras más frecuentes
🧪 Pruebas
Ejecuta los tests con:

bash
pytest tests/
📦 Requisitos
Python 3.10 o superior

pytest (para pruebas)

nltk (si usas stopwords o tokenización avanzada)

Instalación rápida:

bash
pip install nltk pytest
🤝 Contribuciones
Las contribuciones son bienvenidas.
Si deseas proponer mejoras, abre un issue o envía un pull request con una descripción clara de los cambios.

📄 Licencia
Este proyecto está bajo la licencia MIT.
Puedes usarlo, modificarlo y distribuirlo libremente.

⭐ Créditos
Inspirado en herramientas básicas de NLP

Stopwords basadas en listas públicas de NLTK