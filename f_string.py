letter="Hii my name is {} and my country is {}"
name="ayush"
country="India"
print(letter.format(name,country))
#same can be written using formatted string in python as:
print(f"Hey my name is {name} and my country is {country}")
text="For only {price:.2f} dollars !"
print(text.format(price=49.0999))
#if you want to show brackets then use:
print(f"Hey my name is{{name}} and my country is {{country}}")
