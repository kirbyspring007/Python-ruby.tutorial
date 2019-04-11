class Cs:
    @staticmethod
    def static_method():
        print("static_method")
    @classmethod
    def class_method(cls):
        print("class_method")
    def instance_method(self):
        print("instance_method")

i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()
