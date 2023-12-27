#Immortal_Empires
import random
import math
#AI_CLASS
class Peceptron():
  def __init__(self,input_size):
    self.weights = [random.uniform(-1,1) for _ in range(input_size)]
    self.bias = random.uniform(-1,1)
    self.learning_rate = 0.1
  def predict(self, inputs):
    weighted_sum = sum(w * x for w, x in zip(self.weights,inputs)) + self.bias
    return 1 if weighted_sum > 0 else 0
  def train(self,training_data,epochs):
    for epoch in range(epochs):
      for inputs, target in training_data:
        prediction = self.predict(inputs)
        error = target - prediction
        self.weights = [w + self.learning_rate * error * x for w, x in zip(self.weights,inputs)]
        self.bias += self.learning_rate * error


#CLASSES
class Empire():
  def __init__(self,traits):
    self.traits = traits
    self.relations = [] #relations with other empires
  def relationSetup(self,otherEmpireTraits):
    self.relations.append(otherEmpireTraits)
  def techIncrease(self):
    self.traits[2] = int(self.traits[2]) + 1
  def productionIncrease(self):
    self.traits[3] = int(self.traits[3]) * int(self.traits[2])
  def warshipIncrease(self):
    self.traits[4] = (int(self.traits[4]) + int(self.traits[3])) * int(self.traits[2])

#VARIBLES & LISTS & ARRAYS
listOfEmpires = []
#EmpireName EmpirePosture EmpireTechnology EmpireProduction EmpireWarringCapability
empire1 = Empire(["Empire1",50,1,1,0])
empire2 = Empire(["Empire2",-50,1,1,0])
listOfEmpires.append(empire1)
listOfEmpires.append(empire2)

#SETUP_EMPIRE_RELATIONS
for currentEmpire in range(len(listOfEmpires)):
  for otherEmpire in range(len(listOfEmpires)):
    if listOfEmpires[currentEmpire] != listOfEmpires[otherEmpire]:
      listOfEmpires[currentEmpire].relationSetup(listOfEmpires[otherEmpire].traits)

#ACTUAL_RUN
training_data = [([0,0],0),
                 ([0,1],1),
                 ([1,0],1),
                 ([1,1],1),]
peceptron = Peceptron(2)
peceptron.train(training_data,epochs=100)
empire1.warshipIncrease
empire2.warshipIncrease
print("Empire1Relations:",empire1.relations)
print("Empire1Traits:",empire1.traits)
print("Empire2Relations:",empire2.relations)
print("Empire2Traits:",empire2.traits)
