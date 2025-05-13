## Proyecto_Datosfinal

Propósito del Proyecto
Implementar un sistema de gestión de contactos que demuestre:
- Eficiencia con Árbol AVL: Búsquedas/inserciones en tiempo O(log n).
- Versión primitiva: Comparación con árbol AVL (limitación a 5 contactos).

Como usarlo
Ejecutar la versión AVL:
python3 run.py

Opciones:
- Agregar contacto
  - Inserta un nuevo contacto (nombre y teléfono) al árbol AVL.
  - El árbol se auto-balancea automáticamente tras la inserción para garantizar eficiencia en operaciones futuras.
  - No se permiten duplicados (según clave ASCII del nombre, ignorando mayúsculas/minúsculas).

- Buscar contacto
    - Busca un contacto por nombre.
    - Utiliza comparación por clave ASCII, ignorando mayúsculas/minúsculas.
    - Retorna el número de teléfono si se encuentra o indica si no existe.

- Eliminar contacto
  - Elimina un contacto del árbol dado su nombre.
  - Se actualan las conexiones del árbol y se hacen rotaciones si es necesario para mantener el balance.
  - No hay mensaje si el contacto no existe, pero se maneja internamente sin error.

- Llamar a contacto
  - Simula una llamada al contacto: si el nombre está en el árbol, muestra un mensaje con el número.
  - Si no se encuentra, informa que no existe.

- Mostrar contactos (ordenados)
  - Muestra todos los contactos en orden alfabético (orden in-order del árbol AVL).
  - Esto garantiza una lista ordenada eficientemente en O(n) tiempo.


Ejecutar la versión primitiva:
python3 primitivo.py
(solo permite 5 contactos máximo)

Dificultades encontradas en la versión primitiva
- La versión alterna (en primitivo.py) usa una simple lista para almacenar los contactos. Esto trae varias limitaciones y complicaciones importantes:
  - Limitación de tamaño: Solo permite hasta 5 contactos. Esto impide escalar el programa para un uso realista.
  - Ineficiencia en búsquedas y eliminaciones:
  - Las búsquedas recorren la lista entera (tiempo O(n)) en lugar de O(log n) como el AVL.
  - Lo mismo ocurre para eliminar contactos, lo que afecta el rendimiento conforme crece la lista.

  - Falta de orden automático:
    - No hay ordenamiento de contactos al insertarlos.
    - No se puede mostrar la lista alfabéticamente a menos que se ordene manualmente.

  - Duplicación no controlada:
    - Permite insertar contactos con el mismo nombre sin restricción.

  - Ausencia de estructura formal:
    - No se usa orientación a objetos ni claves organizadas.
    - Esto vuelve el código más difícil de extender, mantener y escalar.


Por qué usar un árbol AVL?
- Auto-balanceo: Mantiene eficiencia incluso con datos desordenados.
- Óptimo para contactos: Búsquedas rápidas por nombre.


Información adicional:
- Los contactos se ordenan por nombre utilizando sus valores ASCII para permitir comparaciones eficientes.
- El programa ignora mayúsculas/minúsculas al ordenar.
- No se permiten nombres duplicados en la versión AVL.
- El árbol AVL se mantiene balanceado automáticamente con rotaciones (simples y dobles).
- Se usa sys.setrecursionlimit(10000) para soportar inserciones grandes sin errores de recursión.
- La versión primitiva sirve como línea base para comparar rendimiento, escalabilidad y eficiencia.
- Y elegimos el AVL tree porque ese fue el que nos toco al azar.


Archivos:

- [__pycache__](https://github.com/Nachopacca24/Proyecto_Datosfinal/tree/master/__pycache__)
- [AVL_tree.py](https://github.com/Nachopacca24/Proyecto_Datosfinal/blob/master/AVL_tree.py)
- [main.py](https://github.com/Nachopacca24/Proyecto_Datosfinal/blob/master/main.py)
- [primitivo.py](https://github.com/Nachopacca24/Proyecto_Datosfinal/blob/master/primitivo.py)
- [run.py](https://github.com/Nachopacca24/Proyecto_Datosfinal/blob/master/run.py)
