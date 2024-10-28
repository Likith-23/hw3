def bits(n):
    return bin(n)[2:]  
def consecutive_set_bits(binary_str):
    max_count = 0
    current_count = 0
    for bit in binary_str:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0  
    return max_count  
kf = int(input("ENTER A NUMBER..."))
binary_representation = bits(kf)
print("THE AMOUNT OF CONSECUTIVE SET BITS ARE...", consecutive_set_bits(binary_representation))