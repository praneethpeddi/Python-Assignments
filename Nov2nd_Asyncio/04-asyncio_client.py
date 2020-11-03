#!/usr/bin/env python

import socket
import time
import asyncio

async def send_n_recv_data(question):
    ip = '127.0.0.1'
    tcp_port = 5005

    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockfd.connect((ip, tcp_port))
    sockfd.send(question.encode())
    data = sockfd.recv(1024)
    await asyncio.sleep(1)
    sockfd.close()

    return(data)

async def get_answer_by_question(question):
    print(f"Quesion: {question}")
    reply = send_n_recv_data(question)
	#await asyncio.sleep(1)
    print(f"Asnwer : {reply}")
    print()

async def main():
    task1 = get_answer_by_question("One-page question")
    #await asyncio.sleep(1)
    task2 = get_answer_by_question("One-line question")
    task3 = get_answer_by_question("Booleon question")
    
    await asyncio.wait([task1, task2, task3])
    return task1, task2, task3
    

if (__name__ == "__main__"):
    print(f"started at {time.strftime('%X')}")
    try:
        loop = asyncio.get_event_loop()
        r1, r2, r3 = loop.run_until_complete(main())
        print(f"{r1.result()}")
        print(f"{r2.result()}")
        print(f"{r3.result()}")
    except Exception as e:
        pass
    finally:
        loop.close()
    print(f"Ended at {time.strftime('%X')}")
