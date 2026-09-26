from tasks import (
    add_task,
    list_tasks,
    complete_task,
    delete_task,
    filter_tasks_by_status
)
from storage import load_tasks, save_tasks
from utils import show_menu

tasks = []


def main():
    global tasks
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("Selecciona una opción: ").strip()

        # Validar que sea un número
        if not option.isdigit():
            print("Error: Debes ingresar un número.")
            continue

        # Validar rango de opciones
        if option not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Error: Opción fuera de rango.")
            continue

        if option == "1":
            title = input("Título de la tarea: ").strip()
            add_task(tasks, title)
            save_tasks(tasks)

        elif option == "2":
            list_tasks(tasks)

        elif option == "3":
            try:
                task_id = int(
                    input("ID de la tarea a completar: ").strip()
                )
                complete_task(tasks, task_id)
                save_tasks(tasks)
            except ValueError:
                print("ID inválido. Debe ser un número.")

        elif option == "4":
            try:
                task_id = int(
                    input("ID de la tarea a eliminar: ").strip()
                )
                delete_task(tasks, task_id)
                save_tasks(tasks)
            except ValueError:
                print("ID inválido. Debe ser un número.")

        elif option == "5":
            save_tasks(tasks)
            print("¡Hasta luego!")
            break

        elif option == "6":
            filter_tasks_by_status(tasks, False)

        elif option == "7":
            filter_tasks_by_status(tasks, True)


if __name__ == "__main__":
    main()