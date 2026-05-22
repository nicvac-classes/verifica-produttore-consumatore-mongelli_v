import threading
import random

DIM_BUFFER = 5
N_PRODUTTORI = 3
N_CONSUMATORI = 2
N_ORDINI = 6

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_ordine():
    return f"ORD-{random.randint(10000, 99999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx
        self.dato = idx * 100 + 1
    def run(self):
        global metti
        while (true):
            vuoto.acquire()
            mutexP.acquire()
            i_metti= metti
            metti = (metti + 1) %DIM_BUFFER
            mutexP.release()
            buffer[i_metti]=self.dato
            print(f"PROD-{self.idx}) prodotto{self.dato} in buffer [i_metti]"
            self.dato += 1
            pieno.release()
            

class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx
        def run(self):
            global togli
            while true:
                pieno.acquire()
                mutexC.acquire()
                i_togli = togli
                togli = (togli + 1) %DIM_BUFFER
                mutexC.release()
                dato= buffer[i_togli]
                print(f"CONS-{self.idx}) consumato {dato} da buffer[{i_togli}]
                vuoto.release()

def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    for c in consumatori:
        p.start()
    for p in produttori:
        p.start()
    for p in produttori:
        p.join()
    print("Tutti i canali hanno terminato. Chiusura addetti...")
    for _ in range(N_CONSUMATORI)
    vuoto.acquire()
    buffer[metti] = None
    metti = (metti + 1) %DIM_BUFFER
    pieno.release()
    for c in consumatori:
        c.join()
    for _ in range(N_CONSUMATORI):
            vuoto.acquire()
    buffer[metti] = None
    metti = (metti + 1) %DIM_BUFFER
    pieno.release()
    for c in consumatori:
        c.join()
        pass

    print("Magazzino chiuso.")


if __name__ == "__main__":
    main()
