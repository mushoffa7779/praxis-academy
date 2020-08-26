#proprty : ciri-ciri atau hal-hal yang dimiliki
#method : kemampuan, tugas, atau aktivitas yang dapat dilakukan 

class Kendaraan:
    kecepatan = 0
    cc = 0

# constructor
def _init_(self):
    self.roda = 0

def nyala(self):
    print("brum")

def maju(self):
    if self.roda > 0:
        self.kecepatan = self.kecepatan + 10

def mundur(self):
    pass

# inheritance (pewarisan)
class Motor(Kendaraan):
    pass

m1 = Motor()
m1.roda = 3
print(m1.roda)