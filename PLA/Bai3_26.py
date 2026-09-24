def cost(x):
    return x**2 - 4*x+5
def grad(x):
    return 2*x -4
def myGD2(x0,eta):
    x=[x0]
    for it in range (100):
        x_new=x[-1] - eta*grad(x[-1])
        if abs(x_new-x[-1])<1e-3:
            break
        x.append(x_new)
    return (x, it)
x,it = myGD2(5, 0.2)
print("x =", x[-1])
print("f(x) =", cost(x[-1]))
