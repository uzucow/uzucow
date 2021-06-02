import random
import math
import time


repeat = total = int(input("How many times you want to repeat the calculation?: "))

start = time.time()
in_circle = 0
out_circle = 0
# total = 0

while repeat:
    x = random.random()
    y = random.random()
    distance = math.sqrt(math.pow(x,2)+math.pow(y,2))
    # distance = "{:.2f}".format(distance)
    if distance < 1:
        # print('distance = ' + "{:.3f}".format(distance) + ', it is in the circle!')
        in_circle = in_circle + 1
    else:
        # print('distance = ' + "{:.3f}".format(distance) + ', it is out the circle!')
        out_circle = out_circle + 1
    repeat = repeat - 1
        
estimated_pi = 4 * (in_circle/total)

print("Total number of repeat is: "+ str(total))
print("Estimated pi is   :  " + str(estimated_pi))
print("Python pi value is: ", math.pi)
print("Error: ", "{:.2f}".format((estimated_pi/math.pi)*100 - 100),"%.")
print("Elapsed time: ", time.time()-start, "seconds.")








