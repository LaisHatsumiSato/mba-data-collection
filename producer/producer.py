from kafka import KafkaProducer
import json
import time
from kafka.admin import KafkaAdminClient, NewTopic

def criar_topico():
    try:
        admin = KafkaAdminClient(bootstrap_servers="kafka:29092")

        topic = NewTopic(
            name="transacoes",
            num_partitions=1,
            replication_factor=1
        )

        admin.create_topics([topic])
        print("Topico criado com sucesso")

        admin.close()

    except Exception as e:
        print(f"Topico ja existe ou erro: {e}")


time.sleep(5)

criar_topico()

producer = KafkaProducer(
    bootstrap_servers="kafka:29092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Producer iniciado")

while True:
    try:
        data = {
            "id": int(time.time())
        }

        print(f"Enviando: {data}")

        producer.send("transacoes", value=data)
        producer.flush()

        time.sleep(2)

    except Exception as e:
        print(f"Erro ao enviar: {e}")
        time.sleep(5)