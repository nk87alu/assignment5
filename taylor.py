import matplotlib.pyplot as plt
import math

XVals = []
X = -10
while X <= 10:
    XVals.append(X)
    X += 0.1

Approx15 = []
ActualSin = []

for X in XVals:
    TaylorSum = 0
    
    for N in range(15):
        Power = 2*N + 1
        
        Fact = 1
        for I in range(1, Power + 1):
            Fact *= I
        
        Sign = (-1)**N
        
        Term = Sign * (X**Power) / Fact
        TaylorSum += Term
    
    Approx15.append(TaylorSum)
    ActualSin.append(math.sin(X))

X = 2
TaylorSum = 0
for N in range(15):
    Power = 2*N + 1
    
    Fact = 1
    for I in range(1, Power + 1):
        Fact *= I
    
    Sign = (-1)**N
    
    Term = Sign * (X**Power) / Fact
    TaylorSum += Term

print(f"Taylor series: {TaylorSum}")
print(f"Actual: {math.sin(2)}")

plt.figure(figsize=(10, 6))
plt.plot(XVals, Approx15, label='15 non-zero terms', alpha=0.7)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Taylor Series Approximation of sin(x)')
plt.ylim(-10, 10)
plt.legend()
plt.grid(True)
plt.savefig('taylor.png')
