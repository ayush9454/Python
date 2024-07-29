class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)
    
def add_complex_numbers(complex_numbers):
    result=complex_numbers[0]

    for num in complex_numbers[1:]:
        result=result+num
    return result

N=int(input("Enter the number of complex numbers(N>2)"))

complex_numbers=[]
for i in range(N):
    real_part=int(input(f"Enter the real part of the imaginary number {i+1}"))
    imag_part=int(input(f"Enter imaginary part of the complex number {i+1}"))
    complex_numbers.append(Complex(real_part,imag_part))

result=add_complex_numbers(complex_numbers)

print(f"The sum of {N} Complex numbers: {result.real}+{result.imag}i")
