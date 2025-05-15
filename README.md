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
La versión primitiva del programa (primitivo.py) implementa la gestión de contactos usando únicamente variables y estructura condicional, sin listas, diccionarios ni clases. Esto trae consigo varias limitaciones y complicaciones importantes:
  - Capacidad limitada y fija:
    - Solo permite hasta 5 contactos, definidos manualmente con variables como nombre1, telefono1, ..., nombre5, telefono5.
    - Esta limitación impide que el sistema escale o se adapte a un número variable de entradas.
    - 
  - Gestión manual de contactos:
    - Cada operación (insertar, buscar, eliminar) depende de condiciones múltiples y repetidas para cada variable.
    - El código se vuelve extenso y propenso a errores, especialmente al aumentar el número de contactos.
    - 
  - Ineficiencia en operaciones:
    - Las búsquedas y eliminaciones requieren revisar cada variable por separado, lo cual simula un recorrido lineal con complejidad O(n).
    - No hay ningún tipo de optimización como la que ofrecería un árbol AVL (O(log n)).

  - Falta de orden automático:
    - Los contactos se almacenan en el orden en que fueron agregados, sin un sistema de ordenamiento alfabético.
    - No se puede mostrar la lista en orden sin agregar lógica manual para comparar nombres uno por uno.

  - No se controla la duplicación:
    - No existe verificación para evitar múltiples contactos con el mismo nombre.
    - Esto puede generar confusión o sobrescritura accidental de datos.

  - Ausencia total de estructura formal:
    - No se usa programación orientada a objetos, ni estructuras dinámicas.
    - El diseño rígido lo vuelve difícil de mantener, extender y escalar.


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
- AVL_tree.py:
  - Contiene la implementación de un árbol AVL para manejar una agenda de contactos.
  - Define las clases:
    - Contacto: Almacena nombre, teléfono y genera una clave basada en ASCII para ordenamiento.
    - AVLNode: Nodo del árbol AVL que almacena un contacto y sus hijos izquierdo/derecho.
    - AVLTree: Implementación completa del árbol AVL con métodos para:
      - Insertar (insert), buscar (search), eliminar (delete) contactos.
      - Rotaciones (rotate_left, rotate_right) para mantener el balanceo.
      - Funciones auxiliares como get_height, get_balance, get_min.
      - Operaciones adicionales como llamar (simular llamada) y print_pretty (mostrar contactos ordenados).

- main.py:
- Implementa un menú interactivo para gestionar contactos usando el AVLTree.
  - Funciones:
    - menu_de_contactos: Menú principal con opciones para:
    - Agregar, buscar, eliminar, llamar y mostrar contactos.
    - Usa la clase AVLTree y Contacto importadas desde AVL_tree.py.

- primitivo.py:
- Implementación básica de una agenda de contactos sin estructuras de datos avanzadas.
- Usa variables globales (nombre1, telefono1, etc.) para almacenar hasta 5 contactos.
  - Funciones:
  - insertar, buscar, eliminar, imprimir_contactos.

- menu: Menú interactivo similar al de main.py, pero con lógica rudimentaria.
  - run.py:
  - Punto de entrada del programa. Simplemente importa y ejecuta menu_de_contactos() desde main.py.

- [__pycache__](https://github.com/Nachopacca24/Proyecto_Datosfinal/tree/master/__pycache__)
- [AVL_tree.py](https://github.com/Nachopacca24/Proyecto_Datosfinal/blob/master/AVL_tree.py)
- [main.py](https://github.com/Nachopacca24/Proyecto_Datosfinal/blob/master/main.py)
- [primitivo.py](https://github.com/Nachopacca24/Proyecto_Datosfinal/blob/master/primitivo.py)
- [run.py](https://github.com/Nachopacca24/Proyecto_Datosfinal/blob/master/run.py)
