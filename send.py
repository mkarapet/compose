import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='172.17.0.1'))
channel = connection.channel()

channel.basic_publish(exchange='',
                      routing_key='jenkins',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
