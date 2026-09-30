""" Modelo de datos: Cada tarea se representa como un diccionario (para poder guardarse directamente en tasks.json) con la siguiente estructura:

    {
        "id": 1,               # int  -> identificador único de la tarea
        "title": "Estudiar",   # str  -> nombre de la tarea (no vacío)
        "status": "pendiente"  # str  -> "pendiente" o "completada"
    }

Las demás funcionalidades (agregar, listar, completar, eliminar y guardar) deben usar las constantes y funciones de este módulo en lugar de escribir las claves a mano.
"""

# CLAVES DEL MODELO
# ==============================
KEY_ID = "id"
KEY_TITLE = "title"
KEY_STATUS = "status"

# ESTADOS POSIBLES DE UNA TAREA
# ==============================
STATUS_PENDING = "pendiente"
STATUS_COMPLETED = "completada"
VALID_STATUSES = (STATUS_PENDING, STATUS_COMPLETED)

# Campos obligatorios que debe tener toda tarea
REQUIRED_FIELDS = {KEY_ID, KEY_TITLE, KEY_STATUS}


def generate_id(tasks):
    """
    Genera el siguiente identificador disponible.

    Usa el ID más alto existente + 1, así nunca se repite un ID
    aunque se hayan eliminado tareas.

    Args:
        tasks (list): Lista de tareas existentes.

    Returns:
        int: Nuevo identificador.
    """
    if not tasks:
        return 1
    return max(task[KEY_ID] for task in tasks) + 1


def create_task(tasks, title):
    """
    Crea una nueva tarea con la estructura del modelo.

    Toda tarea nueva inicia con estado "pendiente".

    Args:
        tasks (list): Lista de tareas existentes (para calcular el ID).
        title (str): Nombre de la tarea.

    Returns:
        dict: La tarea creada.

    Raises:
        ValueError: Si el nombre está vacío.
    """
    title = title.strip()
    if not title:
        raise ValueError("El nombre de la tarea no puede estar vacío.")

    return {
        KEY_ID: generate_id(tasks),
        KEY_TITLE: title,
        KEY_STATUS: STATUS_PENDING,
    }


def is_completed(task):
    """Devuelve True si la tarea está completada."""
    return task.get(KEY_STATUS) == STATUS_COMPLETED


def mark_completed(task):
    """Cambia el estado de la tarea a "completada"."""
    task[KEY_STATUS] = STATUS_COMPLETED


def is_valid_task(task):
    """
    Verifica que una tarea cumpla con el modelo:
    - Sea un diccionario con todos los campos obligatorios.
    - El ID sea un entero positivo.
    - El nombre sea un texto no vacío.
    - El estado sea "pendiente" o "completada".
    """
    return (
        isinstance(task, dict)
        and REQUIRED_FIELDS.issubset(task.keys())
        and isinstance(task[KEY_ID], int)
        and task[KEY_ID] > 0
        and isinstance(task[KEY_TITLE], str)
        and task[KEY_TITLE].strip() != ""
        and task[KEY_STATUS] in VALID_STATUSES
    )


def normalize_task(task):
    """
    Convierte tareas guardadas con el formato anterior
    ("completed": True/False) al modelo actual ("status").

    Así los archivos tasks.json antiguos siguen funcionando.
    """
    if isinstance(task, dict) and KEY_STATUS not in task and "completed" in task:
        task = dict(task)
        completed = task.pop("completed")
        task[KEY_STATUS] = STATUS_COMPLETED if completed else STATUS_PENDING
    return task