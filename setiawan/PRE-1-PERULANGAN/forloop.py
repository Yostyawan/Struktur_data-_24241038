# PERULANGAN (Loop)

# foor_loop

# for kondisi

a = 0
a =+ 1 # a = a + 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1

angka_list = [0,1,4,8,10]
for i in angka_list:
    print(f"i sekarang -> {i}")

# PERULANGAN DENGAN RANGE
angka_range = range (5) # di ulangan 5 kali 
for i in angka_range: 
    print(f"i sekarang -> {i}")
print("ini akhir for 2/n")

for i in angka_range:
    print(f"i sekarang -> {i}")
print("ini akhir for 3/n")


# perulangan dengan nama
angka_string = "tio agus setiawan"
for i in angka_string:
    print(f"i sekarang -> {i}")
print("ini akhir for 4/n")

data_str = "tio agus setiawan"
for huruf in data_str:
    print(huruf)

print("akhir perulangan string\n")