wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth in wardrobe:
    for color in wardrobe[cloth]:
        print("{} {}".format(color, cloth))