attribute_codes = ["02419","15344", "01746", "00562", "99999"]
attribute_code_label = ["Style", "Batterie ou pile incluse", "Couleur", "Forme", "Product Class"]

attribute = zip(attribute_codes, attribute_code_label)

for attribute_single in attribute:
    print (attribute_single[0])