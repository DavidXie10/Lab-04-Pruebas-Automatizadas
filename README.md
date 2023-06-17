# Lab-04-Pruebas-Automatizadas
Laboratorio 04 - Pruebas Automatizadas (CI-0142)

# Integrantes
- Juan Ignacio Pacheco Castro (B85841)
- Sol Valle Vega (B98050)
- David Xie Li (B88682)
 
# Profesor
Francisco Sánchez Pérez 

# Instrucciones de ejecución

Para ejecutar los casos de prueba automatizados, es necesario seguir los siguientes pasos y tener instalado Firefox:

1. Instalar Selenium con el comando:

```
pip install -U selenium
```

2. Crear una nueva cuenta. Para ello, edite la línea 20 del archivo **create_account.py** para introducir un nuevo correo de una cuenta inexistente (este correo se utilizará en algunos otros casos de prueba para poder iniciar sesión). Seguidamente, ejecute el siguiente comando para crear la cuenta:

```
python .\create_account.py
```

3. Para agregar/eliminar artículos del Wishlist, debe editar la línea 18 del archivo **add_and_remove_wishlist_items.py** para cambiar el correo por el de la cuenta que acaba de registrar:

```
python .\add_and_remove_wishlist_items.py
```

4. Para utilizar el buscador para encontrar items existentes e items no existentes, ejecute el siguiente comando:

```
python .\search_existent_and_non_existent_item.py
```

5. Para realizar una comparación de varios ítems en el sitio, ejecute el siguiente comando:

```
python .\several_items_comparison.py
```

6. Finalmente, para comprar varios artículos en el sitio por medio del uso de menús, filtros y opciones en la página, debe editar la línea 18 del archivo **buy_specific_items.py** para cambiar el correo por el de la cuenta que acaba de registrar. Luego, ejecute el siguiente comando:

```
python .\buy_specific_items.py
```

Todas las pruebas fueron automatizadas exitosamente.
