selected_number = 1234

def reverse_bits(selected_number):
    bits = bin(selected_number)
    print(bits)
    newbits = ""
    for i in range(len(bits) -1, 0, -1):
        newbits += bits[i]
    return newbits

reversed = reverse_bits(selected_number)

print(reversed)

