from hanoi_temples.stack import Stack

class HanoiTemples:
  def __init__(self, num_discs):
    self.stack_A = Stack()
    self.stack_B = Stack()
    self.stack_C = Stack()
    self.temples = {"A": self.stack_A, "B": self.stack_B, "C": self.stack_C}
    self.generate_discs(num_discs)

  def generate_discs(self, num_discs):
    for i in range(num_discs, 0, -1):
      self.stack_A.push(i)
  
  def run(self):
    print("Початковий стан:", self.temples)
    self.discs_mover(self.stack_A.size(), "A", "C", "B")
    print("Кінцевий стан:", self.temples)

  def discs_mover(self, n, source, destination, auxiliary):
    if n == 0:
        return
    
    self.discs_mover(n - 1, source, auxiliary, destination)
    self.move_disc(source, destination)
    self.discs_mover(n - 1, auxiliary, destination, source)

  def move_disc(self, source, destination):
    disk = self.temples[source].pop()
    self.temples[destination].push(disk)
    print(f"Перемістити диск {disk} з {source} на {destination}")
    print("Проміжний стан:", self.temples)