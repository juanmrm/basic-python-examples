import useful_tools
from Student import Student
from Chef import Chef
from ChineseChef import ChineseChef

print(useful_tools.roll_dice(10))

student1 = Student("Pam", "Art", 3.8, True)
print(student1)
print(student1.name)
print(student1.on_honor_roll())

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()


