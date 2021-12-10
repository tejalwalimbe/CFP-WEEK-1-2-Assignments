# Harmonic Number
def Harmonic(number):
    if number<2:
        return 1
    else:
        return 1/number + Harmonic(number-1)
print(Harmonic(3))
