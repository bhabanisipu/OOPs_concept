class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
    def travel(self,destination):
        print(f"employee is traveling to {destination}")

sam = employee()

print(sam.id)
print(sam.salary)
print(sam.designation)
sam.travel("New York")