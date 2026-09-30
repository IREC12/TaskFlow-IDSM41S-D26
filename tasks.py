# ==============================
# MODELO DE DATOS (definido en models.py)
# ==============================

from models import (
    KEY_ID,
    KEY_TITLE,
    KEY_STATUS,
    create_task,
    is_completed,
    mark_completed,
)


def add_task(tasks, title):
    """
    Agrega una nueva tarea a la lista de tareas.

    Valida que el título no esté vacío y que no exista otra tarea
    con el mismo título. La nueva tarea se registra inicialmente
    como pendiente.
    """
    try:
        # Validar que el título no esté vacío
        if not title.strip():
            print("❌ Error: El título de la tarea no puede estar vacío.")
            return

        # Verificar si ya existe una tarea con el mismo título
        title_lower = title.strip().lower()

        if any(task[KEY_TITLE].lower() == title_lower for task in tasks):
            print("❌ Error: ya existe una tarea con ese título")
            return

        new_task = create_task(tasks, title)

        tasks.append(new_task)
        print(f"✅ Tarea agregada con ID {new_task[KEY_ID]}")

    except ValueError as e:
        print("❌ Error:", e)

    except Exception as e:
        print("❌ Error inesperado al agregar la tarea:", e)
def list_tasks(tasks):
    """
    Muestra en consola todas las tareas registradas.

    Si la lista está vacía, informa al usuario que no hay tareas.
    En caso contrario, imprime cada tarea mostrando su ID, título
    y estado de completado.

    Args:
        tasks (list): Lista de tareas existentes.

    Returns:
        None
    """
    try:
        if not tasks:
            print("No hay tareas")
            return

        for task in tasks:
            task_id = task[KEY_ID]
            title = task[KEY_TITLE]
            status = task[KEY_STATUS]

            icon = "✔" if is_completed(task) else "✘"
            print(f"{task_id}. {title} [{icon} {status}]")

    except Exception as e:
        print("❌ Error al mostrar las tareas:", e)


#  FUNCIÓN DE VALIDACIÓN DE ID
def validar_task_id(task_id):
    """
    Valida que el task_id:
    - Sea un número
    - No sea negativo
    - No rompa el programa si es inválido
    """
    try:
        task_id = int(task_id)
    except ValueError:
        print("❌ Error: El ID debe ser un número (no letras ni símbolos).")
        return None

    if task_id < 0:
        print("❌ Error: El ID no puede ser negativo.")
        return None

    return task_id


def complete_task(tasks, task_id):
    """
    Marca una tarea como completada.

    Valida el ID utilizando la función `validar_task_id`. Si el ID
    es inválido, la función termina sin interrumpir el flujo del
    programa. Si se encuentra la tarea correspondiente, cambia su
    estado a completado. Si no existe una tarea con ese ID, muestra
    un mensaje de error.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea a completar.

    Returns:
        None
    """
    try:
        task_id = validar_task_id(task_id)
        if task_id is None:
            return  # 🔁 No se rompe el menú

        for task in tasks:
            if task[KEY_ID] == task_id:
                if is_completed(task):
                    print("ℹ️ La tarea ya estaba completada")
                    return
                mark_completed(task)
                print("✅ Tarea marcada como completada")
                return

        print("❌ Error: No se encontró una tarea con ese ID")

    except Exception as e:
        print("❌ Error inesperado al completar la tarea:", e)


def delete_task(tasks, task_id):
    """
    Elimina una tarea de la lista de tareas.

    Valida el ID utilizando la función `validar_task_id`. Si el ID
    es inválido, la función termina sin interrumpir el flujo del
    programa. Si la tarea existe, deberá ser eliminada del listado.
    Si no se encuentra una tarea con el ID proporcionado, se mostrará
    un mensaje de error.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea a eliminar.

    Returns:
        None
    """
    try:
        task_id = int(task_id)
    except:
        print("Error: ID inválido")
        return

    for task in tasks:
        if task[KEY_ID] == task_id:
            confirm = input(f"¿Seguro que deseas eliminar '{task[KEY_TITLE]}'? (s/n): ")

            if confirm.lower() != "s":
                print("Eliminación cancelada")
                return
            tasks.remove(task)

            for i, t in enumerate(tasks):
                t[KEY_ID] = i + 1

            print("Tarea eliminada")
            return

    print("Error: ID no encontrado")
def edit_task(tasks, task_id, new_title):
    """
    Edita el nombre de una tarea existente.

    Busca una tarea mediante su ID y modifica su título.
    No permite guardar un nombre vacío.
    """

    try:
        task_id = int(task_id)
    except ValueError:
        print("❌ Error: El ID debe ser un número.")
        return

    if not new_title.strip():
        print("❌ Error: El nombre de la tarea no puede estar vacío.")
        return

    for task in tasks:
        if task[KEY_ID] == task_id:
            task[KEY_TITLE] = new_title.strip()
            print("✅ Tarea editada correctamente")
            return

    print("❌ Error: No se encontró una tarea con ese ID")