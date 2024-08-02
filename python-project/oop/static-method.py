class Math:

    @staticmethod  # not changing staying same
    def add5(x):
        return x + 5

    @staticmethod  # not changing staying same
    def add10(x):
        return x + 10

    @staticmethod  # not changing staying same
    def pr():
        print("run")

#print(Math.add5(5))
print(Math.add10(10))
Math.pr()