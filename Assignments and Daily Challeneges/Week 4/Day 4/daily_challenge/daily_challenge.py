matrix = [
    [ 7 , " ",  3 ],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["i", "r", "!"]
]

text = ""
symbol = 0

for col in range(3):
    for row in matrix:
        char = row[col]
        if type(char) is str and char.isalnum():
            if symbol > 1:
                symbol = 0
                text += " " 
            text += char
        else:
            symbol += 1

print(text + ".")





