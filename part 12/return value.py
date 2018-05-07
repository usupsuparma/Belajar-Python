#fungsi return value
def kuadra(argumen):
    total = argumen**2
    return total
print(kuadra(3))


print("*"* 100)

# fungsi dengan multi argument
def tambah(argument, argumen1):
    total = argument + argumen1
    return total

def kali(argumen, argument1):
    total = argumen * argument1
    return total

print(tambah(3,4))
print(kali(3,tambah(3,2)))