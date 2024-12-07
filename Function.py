k = 50
def func_A():
    k = 100

    def func_B():
        global k
        k = 250

    print("k in function [before calling func_B]: ", k)
    func_B()
    print("k in function [after calling func_B]: ", k)

print("k in main [before calling func_A]: ", k)
func_A()
print("k in main [after calling func_A]: ", k)

