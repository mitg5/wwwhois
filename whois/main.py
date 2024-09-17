#!/usr/bin/env python3
import socket
import sys

if len(sys.argv) != 2:
    print("Uso: python script.py <domínio>")
    sys.exit(1)

dominio = sys.argv[1]

# Criando socket
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

try:
    # Estabelecer conexão
    s.connect(("whois.iana.org", 43))

    # Enviar consulta
    s.sendall((dominio + "\r\n").encode('utf-8'))

    # Resposta do servidor
    resposta = b''
    while True:
        parte = s.recv(1024)
        if not parte:
            break
        resposta += parte

    # Decodificar a resposta
    try:
        print(resposta.decode('utf-8'))
    except UnicodeDecodeError:
        # Se ocorrer erro de decodificação, tentar uma abordagem alternativa
        print("Resposta recebida, mas não foi possível decodificar com UTF-8:")
        print(resposta.decode('latin1'))  # ou usar 'iso-8859-1' se necessário

except Exception as e:
    print(f"Erro: {e}")

finally:
    s.close()
