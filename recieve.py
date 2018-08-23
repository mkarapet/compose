import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.1'))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='jenkins',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
