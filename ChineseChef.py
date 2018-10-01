from Chef import Chef


# Inherit from Chef
class ChineseChef(Chef):

    @staticmethod
    def make_special_dish():
        print("The chef makes orange chicken")

    @staticmethod
    def make_fried_rice():
        print("The chef makes fried rice")