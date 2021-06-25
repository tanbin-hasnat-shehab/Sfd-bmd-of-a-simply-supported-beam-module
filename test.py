import my_module as ss

import matplotlib.pyplot as plt


   
obj=ss.beam([[1,10],[3,9],[4,8],[7,2],[9,12]],15,7)
print(obj.Reactions())
x_x,y_y=obj.bmd()

plt.plot(x_x,y_y)
plt.show()


