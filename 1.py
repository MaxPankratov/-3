name = "Maxim"
surname = "Pankratov"
birthYear = 2004

print(name + '_' + surname + '_' + str(birthYear))

surname, name = name, surname
birthYear += 60

print(name + '_' + surname + '_' + str(birthYear))