import json
import os

from models import REQUIRED_FIELDS, normalize_task, is_valid_task

FILE_NAME = "tasks.json"


def load_tasks():
    """
    Carga las tareas desde el archivo JSON.
    Valida estructura, campos obligatorios y maneja errores.
    Retorna una lista de tareas válida.
    """

    # Si el archivo no existe
    if not os.path.exists(FILE_NAME):
        print("Archivo no encontrado. Se iniciará con una lista vacía.")
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            return []

        data = json.loads(content)

        # Validar que el contenido sea una lista
        if not isinstance(data, list):
            print("Error: El archivo JSON no contiene una lista de tareas.")
            return []

        valid_tasks = []

        for index, task in enumerate(data):
            # Convertir tareas con formato anterior al modelo actual
            task = normalize_task(task)

            # Validar que cada tarea sea un diccionario
            if not isinstance(task, dict):
                print(f"Tarea en posición {index} ignorada: estructura inválida.")
                continue

            # Validar campos obligatorios
            if not REQUIRED_FIELDS.issubset(task.keys()):
                print(
                    f"Tarea en posición {index} ignorada: "
                    f"faltan campos obligatorios {REQUIRED_FIELDS}."
                )
                continue

            # Validar tipos y valores según el modelo
            if not is_valid_task(task):
                print(f"Tarea en posición {index} ignorada: datos inválidos.")
                continue

            valid_tasks.append(task)

        return valid_tasks

    except json.JSONDecodeError as error:
        print("Error: El archivo JSON está mal formado o corrupto.")
        print("Detalle técnico:", error)
        return []

    except Exception as error:
        print("Error inesperado al cargar las tareas.")
        print("Detalle técnico:", error)
        return []


def save_tasks(tasks):
    """
    Guarda las tareas en el archivo JSON.
    """

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
    except Exception as error:
        print("Error al guardar las tareas.")
        print("Detalle técnico:", error)