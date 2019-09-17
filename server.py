import rpyc
import time

class MyService(rpyc.Service):
    
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        print(" Iniciando conexão ...")
        
    def on_disconnect(self, conn):
        #  código que é executado quando uma conexão é finalizada, caso seja necessário
        print(" Terminando conexão ...")
        
    def exposed_get_answer(self): # este é um método exposto
        print(" exposed_get_answer...")
        return 42
    print(" exposed_the_real_answer_though...")
    exposed_the_real_answer_though = 43     # este é um atributo exposto
    
    def get_question(self):  # este método não é exposto
        return "Qual é  a cor do cavalo branco de Napoleão?"

    def exposed_sum_vector_remote(self,v):
        start = time.time() 
        sum = 0
        for i in range(len(v)):
            sum += v[i]
        end = time.time()
        print(end-start)
        return sum
#Para iniciar o servidor

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    
    t.start()

