# ==============================
# CONSTANTES DE CLAVES (MEJORA DE LEGIBILIDAD)
# ==============================

KEY_ID = "id"
KEY_TITLE = "title"
KEY_COMPLETED = "completed"


def add_task(tasks, title):
    """
    Agrega una nueva tarea a la lista de tareas.

    Antes de crear la tarea, verifica que no exista otra con el mismo
    título (sin distinguir mayúsculas y minúsculas). Si el título ya
    existe, muestra un mensaje de error y no agrega la tarea.

    Args:
        tasks (list): Lista de tareas existentes.
        title (str): Título de la nueva tarea.

    Returns:
        None
    """
    try:
        # Verificar si ya existe una tarea con el mismo título
        title_lower = title.lower()

        if any(task[KEY_TITLE].lower() == title_lower for task in tasks):
            print("Error: ya existe una tarea con ese título")
            return

        new_task = {
            KEY_ID: len(tasks) + 1,
            KEY_TITLE: title,
            KEY_COMPLETED: False
        }

        tasks.append(new_task)
        print("✅ Tarea agregada")

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
            completed = task[KEY_COMPLETED]

            status = "✔" if completed else "✘"
            print(f"{task_id}. {title} [{status}]")

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
                task[KEY_COMPLETED] = True
                print("✅ Tarea marcada como completada")
                return

        print("❌ Error: No se encontró una tarea con ese ID")

    except Exception as e:
        print("❌ Error inesperado al completar la tarea:", e)


def delete_task(tasks, task_id):
    """
    Elimina una tarea de la lista mediante su ID.

    Valida el ID utilizando la función validar_task_id.
    Si el ID existe, elimina la tarea y muestra un mensaje.
    Si no existe, informa al usuario.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea a eliminar.

    Returns:
        None
    """
    try:
        task_id = validar_task_id(task_id)
        if task_id is None:
            return

        for task in tasks:
            if task[KEY_ID] == task_id:
                confirm = input(
                    f"¿Seguro que deseas eliminar '{task[KEY_TITLE]}'? (s/n): "
                )

                if confirm.lower() != "s":
                    print("Eliminación cancelada")
                    return

                tasks.remove(task)

                for i, task in enumerate(tasks):
                    task[KEY_ID] = i + 1

                print("✅ Tarea eliminada")
                return

        print("❌ Error: No se encontró una tarea con ese ID")

    except Exception as e:
        print("❌ Error inesperado al eliminar la tarea:", e)