import time

for i in range(2, 32):
    start = time.time()
    x = 123

    for j in range(2 ** i):
        x = (x + j ** 2) % 98765432

    print(x)
    end = time.time()

    print("(" + str(i) + ") Elapsed time: " + str(end - start) + " seconds")
