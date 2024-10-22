import schedule
import time
import asyncio
from auth import authenticate
from post import post_to_bluesky
from threading import Thread

# Crear cliente y autenticar
client = authenticate()

# Función que se ejecuta cada hora
async def job():
    await post_to_bluesky(client)

# Función para ejecutar el trabajo asincrónico
def run_async_job():
    asyncio.run(job())

# Programar la tarea cada hora
schedule.every().hour.at(":00").do(run_async_job)

print("Bot de Bluesky en funcionamiento. Publicando una frase cada hora...")

# Mantener el script en ejecución
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Iniciar el programador en un hilo separado
schedule_thread = Thread(target=run_schedule)
schedule_thread.start()

# Mantener el hilo principal en ejecución
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Deteniendo el bot de Bluesky...")

asyncio.run(job())
