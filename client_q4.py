import rpyc
import sys
import os


def seq_vet(n):
    v = []
    for i in range(n):
        v.append(i)
        
    print("v = " + str(v))
    return v

def sum_vector_on_server(conn):
    n = (int(input("Entre com tamanho de v: ")))
    print("n = "+str(n))
    v = seq_vet(n)
    request = conn.root.sum_vector_remote(v)
    return request

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
 
conn = rpyc.connect(server,18861)

request = sum_vector_on_server(conn)

print( "A soma de v é " + str(request ))