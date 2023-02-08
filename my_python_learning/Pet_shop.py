dog_food = 2.50
cat_food = 4
dog_pack = int(input("Input DOG food packs (0-100): "))
while True:
    try:
        dog_pack 1 <= int(input("Input DOG food packs (0-100): ")) <= 100:
        break
    except ValueError, AssertionError:
        print("Enter a number between 1 and 100: ")

cat_pack = int(input("Input CAT food packs (0-100): "))



end_sum = dog_packs * dog_food + cat_packs * cat_food
print(f"{end_sum} USD.")
