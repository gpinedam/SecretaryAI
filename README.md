SecretaryAI
Este proyecto implementa un asistente virtual para agenda de citas utilizando la API de OpenAI. El asistente recopila información como nombre, número de teléfono, fecha y hora para agendar citas, y guarda estos datos en un archivo CSV.
Características

Interfaz de conversación natural mediante modelos de OpenAI (GPT-4o-mini)
Extracción automática de información relevante para citas
Almacenamiento persistente de citas en formato CSV
Gestión de múltiples sesiones de usuario

Requisitos

Python 3.6+
Librería OpenAI
Acceso a la API de OpenAI (clave API)

Instalación

Clona este repositorio:

git clone https://github.com/tu-usuario/secretaryai.git
cd secretaryai

Instala las dependencias:

pip install openai

Configura tu clave API de OpenAI:
Edita el archivo y reemplaza "YOUR API KEY" con tu clave API real.

Uso
Para iniciar el asistente, ejecuta:
python secretaryai.py
Comandos básicos

Inicia una conversación normal describiendo la cita que deseas agendar
Escribe "salir", "exit" o "quit" para terminar la sesión

Estructura de datos
Las citas se almacenan en citas_agendadas.csv con los siguientes campos:

name: Nombre del cliente
phone: Número de teléfono
date: Fecha de la cita (formato YYYY-MM-DD)
hour: Hora de la cita (formato 24 horas)

Ejemplo de uso
Bienvenido a SecretaryAI. ¿En qué puedo ayudarte?
Tú: Quiero agendar una cita
SecretaryAI: Claro, estaré encantado de ayudarte a agendar una cita. Por favor, proporciona los siguientes datos:

- Nombre:
- Número de teléfono:
- Fecha de la cita:
- Hora de la cita:
Contribuciones
Las contribuciones son bienvenidas. Por favor, siente libre de abrir un issue o enviar un pull request.
