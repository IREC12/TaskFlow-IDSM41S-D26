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

    Args:
        tasks (list): Lista de tareas existentes.
        title (str): Título de la nueva tarea.

    Returns:
        bool: True si la tarea se agregó correctamente.
              False si no pudo agregarse.
    """
    try:
        if not title.strip():
            print("❌ Error: El título de la tarea no puede estar vacío.")
            return False

        title_lower = title.strip().lower()

        if any(
            task[KEY_TITLE].lower() == title_lower
            for task in tasks
        ):
            print("❌ Error: ya existe una tarea con ese título")
            return False

        new_task = create_task(tasks, title.strip())

        tasks.append(new_task)

        print(f"✅ Tarea agregada con ID {new_task[KEY_ID]}")
        return True

    except ValueError as e:
        print("❌ Error:", e)
        return False

    except Exception as e:
        print("❌ Error inesperado al agregar la tarea:", e)
        return False


def list_tasks(tasks):
    """
    Muestra en consola todas las tareas registradas.

    Si la lista está vacía, informa al usuario que no hay tareas.
    En caso contrario, muestra el ID, título y estado de cada tarea.

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

            print(
                f"{task_id}. {title} [{icon} {status}]"
            )

    except Exception as e:
        print("❌ Error al mostrar las tareas:", e)


def validar_task_id(task_id):
    """
    Valida el identificador de una tarea.

    Convierte el valor recibido a entero y verifica que sea mayor
    que cero.

    Args:
        task_id (int | str): Identificador de la tarea.

    Returns:
        int | None: ID válido convertido a entero.
                    None si el valor es inválido.
    """
    try:
        task_id = int(task_id)

    except (ValueError, TypeError):
        print(
            "❌ Error: El ID debe ser un número "
            "(no letras ni símbolos)."
        )
        return None

    if task_id <= 0:
        print("❌ Error: El ID debe ser mayor que cero.")
        return None

    return task_id


def complete_task(tasks, task_id):
    """
    Marca una tarea como completada.

    Valida el ID y busca la tarea correspondiente. Si la tarea
    existe y aún no está completada, actualiza su estado.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea.

    Returns:
        bool: True si la tarea fue completada correctamente.
              False si no se realizó ningún cambio.
    """
    try:
        task_id = validar_task_id(task_id)

        if task_id is None:
            return False

        for task in tasks:
            if task[KEY_ID] == task_id:

                if is_completed(task):
                    print("ℹ️ La tarea ya estaba completada")
                    return False

                mark_completed(task)

                print("✅ Tarea marcada como completada")
                return True

        print(
            "❌ Error: No se encontró una tarea "
            "con ese ID"
        )
        return False

    except Exception as e:
        print(
            "❌ Error inesperado al completar la tarea:",
            e
        )
        return False


def delete_task(tasks, task_id):
    """
    Elimina una tarea de la lista.

    Valida el ID, solicita confirmación y elimina la tarea.
    Después reorganiza los IDs restantes.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea.

    Returns:
        bool: True si la tarea fue eliminada.
              False si no se realizó ningún cambio.
    """
    task_id = validar_task_id(task_id)

    if task_id is None:
        return False

    for task in tasks:
        if task[KEY_ID] == task_id:

            confirm = input(
                f"¿Seguro que deseas eliminar "
                f"'{task[KEY_TITLE]}'? (s/n): "
            ).strip().lower()

            if confirm != "s":
                print("Eliminación cancelada")
                return False

            tasks.remove(task)

            # Reorganizar IDs
            for index, task_item in enumerate(
                tasks,
                start=1
            ):
                task_item[KEY_ID] = index

            print("✅ Tarea eliminada")
            return True

    print("❌ Error: ID no encontrado")
    return False


def edit_task(tasks, task_id, new_title):
    """
    Edita el título de una tarea existente.

    Valida el ID, verifica que el nuevo título no esté vacío
    y evita títulos duplicados.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea.
        new_title (str): Nuevo título de la tarea.

    Returns:
        bool: True si la tarea fue editada correctamente.
              False si no se realizó ningún cambio.
    """
    task_id = validar_task_id(task_id)

    if task_id is None:
        return False

    new_title = new_title.strip()

    if not new_title:
        print(
            "❌ Error: El nombre de la tarea "
            "no puede estar vacío."
        )
        return False

    # Evitar títulos duplicados
    for task in tasks:
        if (
            task[KEY_ID] != task_id
            and task[KEY_TITLE].lower()
            == new_title.lower()
        ):
            print(
                "❌ Error: ya existe una tarea "
                "con ese título"
            )
            return False

    for task in tasks:
        if task[KEY_ID] == task_id:

            task[KEY_TITLE] = new_title

            print("✅ Tarea editada correctamente")
            return True

    print(
        "❌ Error: No se encontró una tarea "
        "con ese ID"
    )
    return False