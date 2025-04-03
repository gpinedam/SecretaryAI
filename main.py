import os
import openai
import csv
import re
from datetime import date
from datetime import datetime


now = datetime.now()
api_key = os.getenv("OPENAI_API_KEY")
# Configuración de OpenAI
client = openai.OpenAI(api_key=api_key)

# Almacenamiento de citas
appointments = []
# Almacenamiento de historiales
session_histories = {}

def chat_with_secretaryai(user_message, session_id):
    """Gestiona la conversación con SecretaryAI usando ChatGPT y permite agendar citas."""
    try:
        # Inicializar historial de sesión si no existe
        if session_id not in session_histories:
            session_histories[session_id] = []

        # Agregar el mensaje del usuario al historial
        session_histories[session_id].append({"role": "user", "content": user_message})

        # Generar respuesta usando la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Eres un asistente para agendar citas. Solicita el nombre, número de teléfono y la fecha(Ten en cuenta que la fecha actual es {now}) de la cita lo apunta en el formato YYYY-MM-DD y la hora en el formato 24 horas. de la forma"
                                              "- Nombre: "
                                              "- Número de teléfono: "
                                              "- Fecha de la cita:"
                                              "- Hora de la cita:  "}
            ] + session_histories[session_id]
        )

        bot_reply = response.choices[0].message.content

        # Agregar la respuesta al historial
        session_histories[session_id].append({"role": "assistant", "content": bot_reply})

        # Buscar datos de cita en la respuesta del asistente
        appointment = extract_appointment_data(bot_reply)
        if appointment:
            update_appointments_csv(appointment)
            del session_histories[session_id]  # Limpiar historial después de agendar cita
            return f"Cita agendada exitosamente para {appointment['name']} el {appointment['date']}. Archivo actualizado."

        return bot_reply
    except Exception as e:
        return f"Error al procesar la solicitud con ChatGPT: {str(e)}"

def extract_appointment_data(bot_reply):
    """Extrae los datos de la cita de la respuesta del asistente."""
    try:
        name_match = re.search(r"Nombre:\s*(.+)", bot_reply)
        phone_match = re.search(r"Número de teléfono:\s*(\d+)", bot_reply)
        date_match = re.search(r"Fecha de la cita:\s*(\d{4}-\d{2}-\d{2})", bot_reply)
        hour_match = re.search(r"Hora de la cita:\s*(\d{1,2}:\d{2})", bot_reply)

        if name_match and phone_match and date_match:
            return {
                "name": name_match.group(1).strip(),
                "phone": phone_match.group(1).strip(),
                "date": date_match.group(1).strip(),
                "hour": hour_match.group(1).strip(),
            }
    except Exception as e:
        print(f"Error al extraer los datos de la cita: {str(e)}")
    return None

def update_appointments_csv(appointment):
    """Actualiza el archivo CSV con los datos de la cita."""
    file_path = "citas_agendadas.csv"
    try:
        # Leer citas existentes si el archivo existe
        existing_appointments = []
        try:
            with open(file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                existing_appointments = list(reader)
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo.")

        # Añadir la nueva cita
        existing_appointments.append(appointment)

        # Sobrescribir el archivo con todas las citas
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "date", "hour"])
            writer.writeheader()
            writer.writerows(existing_appointments)

        print(f"Cita añadida al archivo: {file_path}")
    except Exception as e:
        print(f"Error al actualizar el archivo CSV: {str(e)}")

# Bucle principal del chatbot
def main():
    print("Bienvenido a SecretaryAI. ¿En qué puedo ayudarte?")
    session_id = "session_1"  # Identificador único para la sesión
    while True:
        user_message = input("Tú: ")
        if user_message.lower() in ["salir", "exit", "quit"]:
            print("SecretaryAI: Hasta luego. ¡Que tengas un buen día!")
            break
        response = chat_with_secretaryai(user_message, session_id)
        print(f"SecretaryAI: {response}")

if __name__ == "__main__":
    main()