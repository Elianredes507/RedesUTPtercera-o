import pika

# Dirección IP y puerto del servidor RabbitMQ
rabbitmq_host = '192.168.1.100'  # Reemplaza con la dirección IP de tu servidor RabbitMQ
rabbitmq_port = 5672

# Credenciales de RabbitMQ
rabbitmq_user = 'usuario'
rabbitmq_password = 'contraseña'

def publicar_mensajes(mensajes):
    # Configurar las credenciales
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)

    # Establecer conexión con RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
    )
    channel = connection.channel()

    # Declarar una cola llamada 'hola'
    channel.queue_declare(queue='hola')

    # Publicar cada mensaje en la cola 'hola'
    for mensaje in mensajes:
        channel.basic_publish(exchange='', routing_key='hola', body=mensaje)
        print(f" [x] Enviado {mensaje}")

    # Cerrar la conexión
    connection.close()

if __name__ == "__main__":
    mensajes = ['Hola Mundo!', 'Mensaje 2', 'Mensaje 3', 'Mensaje 4', 'Mensaje 5']
    publicar_mensajes(mensajes)