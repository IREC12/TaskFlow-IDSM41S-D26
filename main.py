from tasks import (
    add_task,
    list_tasks,
    complete_task,
    delete_task,
    edit_task
)
from storage import load_tasks, save_tasks
from utils import show_menu, show_message, pause

tasks = []


def main():
    global tasks
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("Selecciona una opción [1-6]: ").strip()

        # Validar que sea un número
        if not option.isdigit():
            show_message(
                "Debes ingresar un número del 1 al 6.",
                "error"
            )
            pause()
            continue

        # Validar rango de opciones
        if option not in ["1", "2", "3", "4", "5", "6"]:
            show_message(
                "La opción seleccionada no existe. Elige del 1 al 6.",
                "error"
            )
            pause()
            continue

        if option == "1":
            print("\n--- AGREGAR NUEVA TAREA ---")
            title = input("Título de la tarea: ").strip()

            if not title:
                show_message(
                    "El título de la tarea no puede estar vacío.",
                    "warning"
                )
            else:
                add_task(tasks, title)
                save_tasks(tasks)
                show_message(
                    "La tarea fue registrada correctamente.",
                    "success"
                )

            pause()

        elif option == "2":
            print("\n--- LISTA DE TAREAS ---")
            list_tasks(tasks)
            pause()

        elif option == "3":
            print("\n--- COMPLETAR TAREA ---")

            task_id = input("ID de la tarea a completar: ").strip()
            complete_task(tasks, task_id)
            save_tasks(tasks)
            pause()

        elif option == "4":
            print("\n--- ELIMINAR TAREA ---")

            try:
                task_id = int(
                    input("ID de la tarea a eliminar: ").strip()
                )
                delete_task(tasks, task_id)
                save_tasks(tasks)
            except ValueError:
                show_message(
                    "El ID debe ser un número.",
                    "error"
                )

            pause()

        elif option == "5":
            print("\n--- EDITAR TAREA ---")

            try:
                task_id = int(
                    input("ID de la tarea a editar: ").strip()
                )
                new_title = input(
                    "Nuevo nombre de la tarea: "
                ).strip()

                edit_task(tasks, task_id, new_title)
                save_tasks(tasks)

            except ValueError:
                show_message(
                    "El ID debe ser un número.",
                    "error"
                )

            pause()

        elif option == "6":
            save_tasks(tasks)
            show_message(
                "Cambios guardados. Gracias por utilizar TaskFlow.",
                "success"
            )
            break


if __name__ == "__main__":
    main()