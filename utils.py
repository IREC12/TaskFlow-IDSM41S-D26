def show_menu():
    print("\n" + "*" * 40)
    print("*        🚀 TASKFLOW DEVOPS        *")
    print("*" * 40)
    print("📌 ¿Qué deseas hacer?")
    print()
    print("  [1] ➕ Agregar nueva tarea")
    print("  [2] 📋 Ver lista de tareas")
    print("  [3] ✅ Marcar tarea como completada")
    print("  [4] 🗑️  Eliminar una tarea")
    print("  [5] ✏️  Editar una tarea")
    print("  [6] 🚪 Salir del sistema")
    print()
    print("*" * 40)


def show_message(message, message_type="info"):
    """Muestra mensajes claros según el resultado de una operación."""

    if message_type == "success":
        prefix = "[OK]"
    elif message_type == "error":
        prefix = "[ERROR]"
    elif message_type == "warning":
        prefix = "[AVISO]"
    else:
        prefix = "[INFO]"

    print(f"\n{prefix} {message}")


def pause():
    """Permite al usuario leer el resultado antes de volver al menú."""
    input("\nPresiona ENTER para volver al menú...")