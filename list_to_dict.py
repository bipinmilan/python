# convert list to list of dictionaries
color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

for f, c in zip(color_name, color_code):
    print([{
        'color name': f,
        'color code': c
    }])
