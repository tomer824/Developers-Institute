age = input("Enter your birthday DD-MM-YYYY: ")
new_age = age.split("-")
how_old = 2020 - int(new_age[-1])
candles = str(how_old)[-1]
new_candles = int(candles)
top_side = int((11 - new_candles) / 2) *"_"
center_candles = "i" * new_candles
print(f"    {top_side}{center_candles}{top_side}")


print("   |:H:A:P:P:Y:|")
print(" __|___________|_")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:I:R:T:H:D:A:Y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")