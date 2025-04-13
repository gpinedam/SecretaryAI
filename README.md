# SecretaryAI

Un asistente virtual basado en la API de OpenAI para agendar citas y almacenarlas en formato CSV.

## Descripción

SecretaryAI es una aplicación de línea de comandos que proporciona un asistente conversacional para la gestión de citas. Utiliza el modelo GPT-4o-mini de OpenAI para mantener conversaciones naturales con los usuarios y extraer automáticamente la información relevante para agendar citas.

## Características

- Interfaz conversacional usando la API de OpenAI
- Extracción automática de datos de citas (nombre, teléfono, fecha y hora)
- Almacenamiento persistente en formato CSV
- Gestión de múltiples sesiones de conversación
- Cumplimiento con las convenciones de estilo PEP8

## Requisitos

- Python 3.6+
- Librería OpenAI
- Clave API de OpenAI

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/secretaryai.git
cd secretaryai
```

2. Instala las dependencias:
```bash
pip install openai
```

3. Configura tu clave API:
   - Abre el archivo `secretaryai.py`
   - Reemplaza `"YOUR API KEY"` con tu clave API de OpenAI

## Uso

Para iniciar el asistente:

```bash
python secretaryai.py
```

### Interacción con el asistente

1. Inicia una conversación describiendo tu necesidad de agendar una cita
2. El asistente te guiará solicitando:
   - Nombre
   - Número de teléfono
   - Fecha de la cita (formato YYYY-MM-DD)
   - Hora de la cita (formato 24 horas)
3. Una vez proporcionados todos los datos, la cita se guardará automáticamente

Para salir del asistente, escribe: `salir`, `exit` o `quit`

## Formato de datos

Las citas se almacenan en un archivo CSV (`citas_agendadas.csv`) con los siguientes campos:

| Campo | Descripción |
|-------|-------------|
| name  | Nombre del cliente |
| phone | Número de teléfono |
| date  | Fecha de la cita (YYYY-MM-DD) |
| hour  | Hora de la cita (HH:MM) |

## Ejemplo de diálogo

```
Bienvenido a SecretaryAI. ¿En qué puedo ayudarte?
Tú: Necesito agendar una cita para mañana
SecretaryAI: Claro, estaré encantado de ayudarte a agendar una cita para mañana. Por favor, proporcióneme los siguientes datos:

- Nombre: 
- Número de teléfono: 
- Fecha de la cita:
- Hora de la cita: 

Tú: Mi nombre es Juan Pérez, mi teléfono es 123456789, para mañana a las 15:00
SecretaryAI: Gracias por proporcionar esa información. Permíteme confirmar los detalles:

- Nombre: Juan Pérez
- Número de teléfono: 123456789
- Fecha de la cita: 2025-04-14
- Hora de la cita: 15:00

Cita agendada exitosamente para Juan Pérez el 2025-04-14. Archivo actualizado.
```

## Estructura del código

El código sigue las convenciones PEP8 y está organizado en las siguientes funciones principales:

- `chat_with_secretaryai()`: Gestiona la conversación con la API de OpenAI
- `extract_appointment_data()`: Extrae los datos de cita de las respuestas
- `update_appointments_csv()`: Actualiza el archivo CSV con nuevas citas
- `main()`: Función principal que ejecuta el bucle de interacción

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b feature/amazing-feature`)
3. Haz commit de tus cambios (`git commit -m 'Add some amazing feature'`)
4. Haz push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request


## Autor

George Pineda


