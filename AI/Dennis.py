
class Dennis:
  behavior_string="matrix based approach of learning based on previous states"
  gender="male"
  name="Dennis"
  random = __import__("random")
  math = __import__("math")
  
  def __init__(self):
    #self.np = __import__("numpy")
    self.w1 = self.random.random()
    self.w2 = self.random.random()
    self.b1 = self.random.random()
    self.w3 = self.random.random()
    self.b2 = self.random.random()
  
  def sigmoid(x):
    return 1/(1+(1/(self.math.pow(e,x))))
  def sigPrime(x):
    #derivative of sig
  def activate(x1,y2):
    return self.sigmoid(self.w3*(self.sigmoid(self.w1*x1-self.b1) + self.sigmoid(self.w2*x2-self.b1))-self.b2)
  def train(desired):
  
  # Converts [1,0] for Z into com,cop
  def convertState(x):
    if self.math.round(x)=1: 
      return "compete"
    else:
      return "cooperate"
  
  def first_turn(self):
      return "compete"

  def take_turn(self, data=()):
      return "compete"
