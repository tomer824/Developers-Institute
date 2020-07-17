# 1.

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# output = zip(keys, values)
# print(dict(output))


# 2.
store = {
"name" : "Zara",
"creation_date" : 1975,
"creator_name" : "Amancio Ortega Gaona", 
"type_of_clothes" : ["men", "women", "children", "home"],
"international_competitors" : ["Gap", "H&M", "Benetton"],
"number_stores" : 7000,
"major_color" : [{"France" : "blue"}, {"Spain" : "red"}, {"US" : "pink, green"}] 
}

store["number_stores"] = 2
clothes_for = store["type_of_clothes"]
print(f"Zara makes clothing for {clothes_for}")

store["country_creation"] = "spain"

if store["international_competitors"]:
    store["international_competitors"].append("Desigual")

del store["creation_date"]

print(store["international_competitors"][-1])
print(store["major_color"][2])
print(len(store))
print(store.keys())

more_on_zara  = {
    "creation_date": 1975,
    "number_stores" : 10000
}

store.update(more_on_zara)
print(store)
print(store["number_stores"])


# 3.

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 

# disney_users_a = {name: users.index(name) for name in users}
# print(disney_users_a)

# disney_users_b = {users.index(name): name for name in users}
# print(disney_users_b)

# sorted_list = sorted(users)
# disney_users_c = {name: sorted_list.index(name) for name in sorted_list}
# print(disney_users_c)

# disney_users_d = {name: users.index(name) for name in users if "i" in name and name[0] in ["M", "P"]}
# print(disney_users_d)


