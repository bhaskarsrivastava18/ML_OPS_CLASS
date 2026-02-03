class employee:
    def __init_subclass__(self):
        print("Subclass initialized")
        self.id -123
        self.salary = 50000
        self.designation ="SDE"
        print("Employee details initialized")

        def travel (self, destination):
            print("this travel method is called manually")
            print(f"Traveling to {destination}")
        
        sam = employee()
        sam.travel("New York")