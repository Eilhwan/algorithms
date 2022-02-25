class pot:
    def cook(self, ingredient1, ingredient2):
        if ingredient1 == "tomato source" and ingredient2 == "noodle":
            print("pasta")
        elif ingredient1 == "wheat" and ingredient2 == "water":
            print("bread")
        elif ingredient1 == "fish" and ingredient2 == "chips":
            print(ingredient1 + "and" + ingredient2)
        else:
            print("망쳤다")


pot1 = pot()

# pot1.cook("fish", "chips")

# for => ~동안 in 안에 range(10):
for i in range(10):
    print(i)

a = "1234"

b = 123


a + b
