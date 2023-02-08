animal = input()
type = {
    "dog": "mammal",
    "crocodile": "reptile",
    "tortoise": "reptile",
    "snake": "reptile",
}
print(type.get(animal, "unknown"))