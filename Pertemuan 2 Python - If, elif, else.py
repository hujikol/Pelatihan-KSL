# a = 4
# b = 4

# if a < b:
#     print("a kurang dari b")
# elif a > b:
#     print("a lebih besar dari b")
# else:
#     print("a sama dengan b")

# print("diluar if")

#shorthand if else
#print("A") if a > b else print("B")


# # if else biasa
# if a != b: 
#     if a > b: 
#         print("a lebih besar dari b") 
#     else: 
#         print("b lebih besar dari a") 
# else: 
#     print("A dan B bernilai sama") 

# Tenary Operator Python in version 2.5.
# #tenary 
# print("A dan B bernilai sama oke" if a == b else "a lebih besar dari b oke" if a > b else "b lebih besar dari a oke") 


# angka = 27
# bilangan = 27
# #if else biasa
# if angka % 2 == 0 or angka != bilangan:
#     if angka > 0:
#         print(str(angka) + " Adalah Genap Positif")
#     else:
#         print(str(angka) + " Adalah Genap Negatif")
# else:
#     if angka > 0:
#         print(str(angka)+" Adalah Ganjil Positif atas")
#     else:
#         print(str(angka)+" Adalah Ganjil Negatif")
    
# #tenary
# print(str(bilangan) + " Adalah Genap Positif" if bilangan > 0 and bilangan % 2 == 0 
# else str(bilangan) + " Adalah Genap Negatif" if bilangan % 2 == 0 
#      else str(bilangan) + " Adalah Ganjil Positif" if bilangan > 0 and bilangan % 2 == 1 
#           else str(bilangan) + " Adalah Ganjil Negatif")

#assign variable linear
x = b = c = 2

y = 5
#statement biasa
if 0 < x and x < y and y < 10: # 0 < x < y < 10
    print(str(x + y) + "<- hasil penjumlahan")
    print(str(b + c) + " <- hasil penjumlahan")
else:
    print("gagal menjumlah")

#statement linear
if not (0 < x < y < 10):
    print(str(x * y) + "<- hasil perkalian")
else:
    print("gagal mengkalikan")

#penggunaan negasi dan jika didalam (in) suatu sting/list/tuple/dict/dan sebagainya
kata = ["apel","jeruk","mangga"]
if "lemon" not in kata:
    print("kami tidak jual lemon")
else:
    print("ga ketemu kak")


# # Print dengan enter
# print("Hello")
# print("World") 

# print("Hello", end =",") #isi dalam end adalah akhiran dari yang di print *default \n atau new line, biar hilangin enter isikan dengan ="" atau =" "
# print("World") 
