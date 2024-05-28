# Colas de mensajes con RabbitMQ
### ¿Como se ejecutan los scripts?
- Utilizaremos el servicio de RabbitMQ.
- Por entorno usamos la VPS que porporciona la uniersidad.
- Tambien confuguraremos las credenciales para acceder al servidor RabbitMQ
### Configuracion de RabbitMQ 
Lo primero que debemos hacer es crear un usuario y su contraseña con el siguiente comando:
```
sudo rabbitmqctl add_user usuario contraseña
```
Luego le daremos permisos al usuario:
```
sudo rabbitmqctl set_permissions -p / usuario ".*" ".*" ".*" 
```
Esto es opcional pero podemos asignar los tags de administrador al usuario con el siguiente comando: 
```
sudo rabbit set_user_tags usuario administrator
```
Podemos ver la listas de usuarios con el siguiente comando: 
```
sudo rabbitmqctl list_users 
```
Para ver los permisos que tiene un usuario podemos utilizar el siguiente comando: 
```
sudo rabbitmqctl list_user_permissions usuario
```
### Ejecucion de los scripts
La ejecucion para los codigos de productor y consumidor en lo que es la IP, el puesto es la misma solo tendres que cambiar la IP a la de nuestro servidor, el puerto que utiliza el RabbitMQ por defecto es el 5672, en usuario colocaremos el usuario que creamos y para la contraseña Tambien la que hemos creado. Es posible que tendremos que poner una letra al principio del usuario (N) y una letra al principio de la contraseña (C) como vemos en el siguiente ejemplo:
```
rabbitmq_user = '(N) NOMBRE_USUARIO'
rabbitmq_password = '(C) CONTRASEÑA'
```
Las letras se pondran en mayusculas y sin los parentesis.
Ahora se reemplaza la IP del servidor de rabbitmq de la siguieente manera:
```
rabbitmq_host = 'IP_DEL_SERVIDOR_RABBITMQ'
rabbitmq_port = '5672'
```
Si queremos añadir o cambiar los mensajes que enviara el productor podemos modificar la lista de mensajes, la cual es la siguiente:
```
 mensajes = ['Hola Mundo!', 'Mensaje 2', 'Mensaje 3', 'Mensaje 4', 'Mensaje 5']
```
# Con esto podriamos ya ejecutar el productor y el consumidor de forma correcta.
