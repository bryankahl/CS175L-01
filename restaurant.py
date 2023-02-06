#CS175L
#Bryan Kahl
#restaurant


    
vegetarian = False
vegan = False
gluten_free = False

joe_gourmet = ("Joe's Gourmet Burgers")
main_street = ("Main Street Pizza Company")
corner_cafe = ("Corner Cafe")
mamas_italian = ("Mama's Fine Italian")
chefs_kitchen = ("Chef's Kitchen")

vegetarian = (input("Is anyone in your party a vegetarian?"))
vegetariananswer = vegetarian.lower()
if vegetariananswer == "yes":
    vegetarian = True
else:
    vegetarian = False

vegan = (input("Is anyone in your party a vegan?"))
vegananswer = vegan.lower()
if vegananswer == "yes":
    vegan = True
else:
    vegan = False

gluten_free = (input("Is anyone in your party gluten free?"))
gluten_freeanswer = gluten_free.lower()
if gluten_freeanswer == "yes":
    gluten_free = True
else:
    gluten_free = False



print("Here are your restaurant choices: ")

if vegetarian == True and vegan == True and gluten_free == True:
    print(f'{corner_cafe:>14}')
    print(f'{chefs_kitchen:>17}')
elif vegetarian == False and vegan == True and gluten_free == True:
    print(f'{corner_cafe:>14}')
    print(f'{chefs_kitchen:>17}')
elif vegetarian == True and vegan == False and gluten_free == True:
    print(f'{main_street:>28}')
    print(f'{corner_cafe:>14}')
    print(f'{chefs_kitchen:>17}')
elif vegetarian == True and vegan == True and gluten_free == False:
    print(f'{corner_cafe:>14}')
    print(f'{chefs_kitchen:>17}')
elif vegetarian == False and vegan == False and gluten_free ==True:
    print(f'{main_street:>28}')
    print(f'{corner_cafe:>14}')
    print(f'{chefs_kitchen:>17}')
elif vegetarian == True and vegan == False and gluten_free == False:
    print(f'{main_street:>28}')
    print(f'{mamas_italian:>22}')
    print(f'{corner_cafe:>14}')
    print(f'{chefs_kitchen:>17}')
elif vegetarian == False and vegan == True and gluten_free == False:
    print(f'{corner_cafe:>14}')
    print(f'{chefs_kitchen:>17}')
elif vegetarian == False and vegan == False and gluten_free == False:
    print(f'{joe_gourmet:>24}')
    print(f'{main_street:>28}')
    print(f'{mamas_italian:>22}')
    print(f'{corner_cafe:>14}')
    print(f'{chefs_kitchen:>17}')


    
    





