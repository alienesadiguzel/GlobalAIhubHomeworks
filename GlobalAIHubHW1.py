a = []
for i in range(1, 6):
    girilecekDeger = int(input("lütfen girmek istediğiniz değeri yazınız: "))
    a.append(girilecekDeger)
    print(type(girilecekDeger))
print("Girdiğiniz değerler {}".format(a))
print(f"Girdiğiniz değer {a}")