import pika

# Dirección IP y puerto del servidor RabbitMQ
rabbitmq_host = 'IP_DEL_SERVIDOR_RABBITMQ'
rabbitmq_port = 5672

# Credenciales de RabbitMQ
rabbitmq_user = 'usuario'
rabbitmq_password = 'contraseña'

def callback(ch, method, properties, body):
    print(f" [x] Recibido {body.decode()}")

def consumir_mensajes():
    # Configurar las credenciales
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)

    # Establecer conexión con RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
    )
    channel = connection.channel()

    # Declarar una cola llamada 'hola'
    channel.queue_declare(queue='hola')

    # Configurar el consumidor para usar la cola 'hola'
    channel.basic_consume(queue='hola', on_message_callback=callback, auto_ack=True)

    print('Esperando por mensajes. Presiona CTRL+C para salir')
    channel.start_consuming()

if __name__ == "__main__":
    consumir_mensajes()
