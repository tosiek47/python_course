name = "Antek Pszenica"

first_name = name[0:5] #[:5]
last_name = name[6:14] #[6:]
funky_name = name[0:14:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)



website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])