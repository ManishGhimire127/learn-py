# temperature = 25
# if temperature > 30:
#     print("It's hot day")
#     print("Drink pleanty of water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Enjoy the day")

# Exercise
weight = int(input("Weight: "))
unit = str(input("(K)g or (L)bs: "))
if unit.upper() == "K":
    convert = weight / 0.45
    print("Weight in Lbs: ", convert) # convert is str or srt(covert)
else:
    convert = weight * 0.45
    print("Weight in Kg: ", convert) # convert is str or srt(covert)
print("Thank You")