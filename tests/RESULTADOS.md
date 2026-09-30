# Resultados de pruebas - TaskFlow

## Responsable

Jaime Sanchez

## Issue

Issue #15 - Testing

## Objetivo

Comprobar el correcto funcionamiento de las principales operaciones
del sistema TaskFlow mediante pruebas automatizadas.

## Pruebas realizadas

Se realizaron pruebas para verificar:

- Agregar una tarea.
- Evitar tareas duplicadas.
- Listar tareas registradas.
- Listar una colección vacía.
- Completar una tarea.
- Manejar un ID inexistente.
- Validar IDs numéricos.
- Validar IDs con letras.
- Validar IDs negativos.
- Eliminar una tarea.
- Cancelar la eliminación de una tarea.
- Manejar un ID inválido al eliminar.

## Comando utilizado

```bash
python3 -m unittest discover -s tests -v