# 🔄 Diagrama de Flujo – Proceso de Préstamo (Texto)

```
[Inicio]
   |
   v
¿Libro existe?
   |---- No ----> [Mostrar error: Libro no encontrado] --> [Fin]
   |
  Sí
   |
   v
¿Libro disponible?
   |---- No ----> [Mostrar error: Libro no disponible] --> [Fin]
   |
  Sí
   |
   v
¿Usuario existe?
   |---- No ----> [Mostrar error: Usuario no encontrado] --> [Fin]
   |
  Sí
   |
   v
[Registrar préstamo]
   |
   v
[Guardar fecha de préstamo]
   |
   v
[Cambiar estado del libro a "No disponible"]
   |
   v
[Confirmar préstamo exitoso]
   |
   v
[Fin]
```