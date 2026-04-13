import requests
import time
import random
import uuid
from datetime import datetime

URL = "http://api:8000/transacao"

produtos = [
    {"nome": "notebook", "categoria": "eletronicos"},
    {"nome": "celular", "categoria": "eletronicos"},
    {"nome": "tenis", "categoria": "vestuario"},
    {"nome": "camiseta", "categoria": "vestuario"},
    {"nome": "fone", "categoria": "eletronicos"}
]

metodos_pagamento = ["pix", "cartao_credito", "boleto"]

# 🔥 memória de transações antigas (pra duplicar)
historico = []

while True:
    produto = random.choice(produtos)

    # 🔁 20% de chance de duplicar
    if historico and random.random() < 0.2:
        transacao = random.choice(historico)
        print("♻️ DUPLICADO GERADO:", transacao)

    else:
        transacao = {
            "transacao_id": str(uuid.uuid4()),
            "cliente_id": random.randint(1, 100),
            "produto": produto["nome"],
            "categoria": produto["categoria"],
            "valor": round(random.uniform(50, 5000), 2),
            "quantidade": random.randint(1, 3),
            "data_transacao": datetime.now().isoformat(),
            "metodo_pagamento": random.choice(metodos_pagamento)
        }

        # salva no histórico
        historico.append(transacao)

    # ❗ erro proposital
    if random.random() < 0.1:
        transacao["valor"] = None

    try:
        r = requests.post(URL, json=transacao, timeout=5)
        print(f"Status: {r.status_code} | Enviado: {transacao}")
    except Exception as e:
        print("Erro:", e)

    time.sleep(1)