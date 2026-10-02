from tasks import (
    add_task,
    list_tasks,
    complete_task,
    delete_task,
    edit_task,
    filter_tasks_by_status
)

from storage import load_tasks, save_tasks
from utils import show_menu, show_message, pause


tasks = []


def main():
    """
    Función principal del programa.

    Carga las tareas almacenadas y permite agregar, listar,
    completar, eliminar y editar tareas desde el menú principal.
    """
    global tasks

    tasks = load_tasks()

    while True:
        show_menu()

        option = input("Selecciona una opción [1-8]: ").strip()

        # Validar que la opción sea un número
        if not option.isdigit():
            show_message(
                "Debes ingresar un número del 1 al 8.",
                "error"
            )
            pause()
            continue

        # Validar rango de opciones
        if option not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            show_message(
                "La opción seleccionada no existe. Elige del 1 al 8.",
                "error"
            )
            pause()
            continue

        # Agregar tarea
        if option == "1":
            print("\n--- AGREGAR NUEVA TAREA ---")
            title = input("Título de la tarea: ").strip()

            if add_task(tasks, title):
                save_tasks(tasks)
                show_message(
                    "La tarea fue registrada correctamente.",
                    "success"
                )

            pause()

        # Listar tareas
        elif option == "2":
            print("\n--- LISTA DE TAREAS ---")
            list_tasks(tasks)
            pause()

        # Completar tarea
        elif option == "3":
            print("\n--- COMPLETAR TAREA ---")

            task_id = input(
                "ID de la tarea a completar: "
            ).strip()

            if complete_task(tasks, task_id):
                save_tasks(tasks)

            pause()

        # Eliminar tarea
        elif option == "4":
            print("\n--- ELIMINAR TAREA ---")

            task_id = input(
                "ID de la tarea a eliminar: "
            ).strip()

            if delete_task(tasks, task_id):
                save_tasks(tasks)

            pause()

        # Editar tarea
        elif option == "5":
            print("\n--- EDITAR TAREA ---")

            task_id = input(
                "ID de la tarea a editar: "
            ).strip()

            new_title = input(
                "Nuevo nombre de la tarea: "
            ).strip()

            if edit_task(tasks, task_id, new_title):
                save_tasks(tasks)

            pause()

        # Filtrar tareas por estado
        elif option in ("6", "7"):
            filter_tasks_by_status(tasks, option == "7")
            pause()

        # Salir
        elif option == "8":
            save_tasks(tasks)
            show_message(
                "Cambios guardados. Gracias por utilizar TaskFlow.",
                "success"
            )
            break


if __name__ == "__main__":
    main()
