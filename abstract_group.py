from abc import ABC, abstractmethod

class Group(ABC):
    
    @abstractmethod
    def identity(self):
        pass
    
    @abstractmethod
    def binary_operator(self, a, b):
        pass
    
    @abstractmethod
    def inverse(self, a):
        pass
    
    def exponentiation(self, a, n):
        assert(n > 0)
        r = self.identity()
        for i in range(0, n):
            r = self.binary_operator(r, a)
        return r
    
    def check_associative(self, a, b, c):
        return self.binary_operator(self.binary_operator(a, b), c) == self.binary_operator(a, self.binary_operator(b, c))
    
    def check_identity(self, a):
        return self.binary_operator(a, self.identity()) == a
    
    def check_inverse(self, a):
        return self.binary_operator(a, self.inverse(a)) == self.identity()

# Integers with addition
class Z_with_addition(Group):
    
    def identity(self):
        return 0
    
    def binary_operator(self, a, b):
        return a + b
    
    def inverse(self, a):
        return -a
    
    
Z_with_addition = Z_with_addition()

a = 1
b = 2
c = 3

print("Z_with_addition")   
print(Z_with_addition.identity())
print(Z_with_addition.binary_operator(a, b))
print(Z_with_addition.inverse(a))
print(Z_with_addition.exponentiation(a, 1))
print(Z_with_addition.exponentiation(a, 10))

# Check properties
print(Z_with_addition.check_associative(a, b, c))
print(Z_with_addition.check_identity(a))
print(Z_with_addition.check_inverse(a))

# 16-bit bit strings with xor
class strings_16_bits(Group):
    
    def identity(self):
        return 0b0
    
    def binary_operator(self, a, b):
        return a ^ b
    
    def inverse(self, a):
        return a
    
strings_16_bits = strings_16_bits()

a = 0b101010 # 42
b = 0b1111111111111111 # 65535
c = 0b1 # 1

print("\nstrings_16_bits")
print(bin(strings_16_bits.identity()))
print(bin(strings_16_bits.binary_operator(a, b)))
print(bin(strings_16_bits.inverse(a)))
print(bin(strings_16_bits.exponentiation(a, 1)))
print(bin(strings_16_bits.exponentiation(a, 2))) 
print(bin(strings_16_bits.exponentiation(a, 3)))

# Check properties
print(strings_16_bits.check_associative(a, b, c))
print(strings_16_bits.check_identity(a))
print(strings_16_bits.check_inverse(a))
