import socket
import threading
import time

#Função do servidor

def udp_server():
    
    print("\n[Server Thread] Iniciando servidor UDP...\n")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 50000))
    print("\n[Server Thread] Servidor operante e no aguardo de mensagens \n...")

    while True:
        try:
            data, address = server_socket.recvfrom(1024)  # No timeout for the server
            message = data.decode()

            if message.lower() == "exit":
                print(f"\n[Server Thread] Cliente {address} desconectou.\n")
                break

            print(f"\n[Server Thread] Recebido de cliente {address}: {message}\n")
            server_socket.sendto(f"Servidor recebeu: {message}".encode(), address)

        except Exception as e:
            print(f"\n[Server Thread] Erro: {e}\n")
            break

    server_socket.close()
    print("\n[Server Thread] O servidor fechou.\n")

#Função do cliente

def udp_client():
    
    time.sleep(1)  #Só pra garantir que o servidor terá tempo de iniciar

    print("\n[Client Thread] Iniciando cliente UDP...\n")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 50000)

    while True:
        try:
            message = input("\n[Client Thread] Entre uma mensagem para enviar ao servidor (digite 'exit' para desconectar): \n")

            
            client_socket.sendto(message.encode(), server_address)

            if message.lower() == "exit":
                print("\n[Client Thread] Fechando conexão com o servidor...\n")
                break

            
            response, _ = client_socket.recvfrom(1024)
            print(f"\n[Client Thread] Resposta do servidor: {response.decode()}\n")

        except Exception as e:
            print(f"\n[Client Thread] Erro: {e}\n")
            break

    client_socket.close()
    
    print("\n[Client Thread] O cliente fechou.\n")

# Criando threads para rodar tanto cliente quanto servidor

server_thread = threading.Thread(target=udp_server)
client_thread = threading.Thread(target=udp_client)

# Aqui iniciam-se ambas as threads

server_thread.start()
client_thread.start()

# Aguardando as threads encerrarem

server_thread.join()
client_thread.join()

print("\nO cliente e o servidor fecharam.\n")