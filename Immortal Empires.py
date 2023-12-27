#Immortal_Empires

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
#EmpireName EmpirePosture EmpireTechnology
empire1 = Empire(["Empire1",50,1,1,0])
empire2 = Empire(["Empire2",-50,1,1,0])
empire3 = Empire(["Empire3",75,1,1,0])
listOfEmpires.append(empire1)
listOfEmpires.append(empire2)
listOfEmpires.append(empire3)

#RUN
for currentEmpire in range(len(listOfEmpires)):
  for otherEmpire in range(len(listOfEmpires)):
    if listOfEmpires[currentEmpire] != listOfEmpires[otherEmpire]:
      listOfEmpires[currentEmpire].relationSetup(listOfEmpires[otherEmpire].traits)

print(empire1.relations)
print(empire1.traits)
print(empire2.relations)
print(empire2.traits)
print(empire3.relations)
print(empire3.traits)
