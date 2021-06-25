import my_module as ss

import matplotlib.pyplot as plt


   
obj=ss.beam([[1,10],[3,9],[4,8],[7,2],[9,12]],15,7)
#beam method needs 3 arguments.....1) an array of [point load position from left end,value of point load] 2) length of the beam  3)value of uniformly distributed load

# printing force reactions RA,RB
print(obj.Reactions())

#bmd method return two array of point co ordinate of x and y to draw the Bending moment diagram or to do your stuff..
bmd_x,bmd_y=obj.bmd()

#sfd method return two array of point co ordinate of x and y to draw the Shear force diagram or to do your stuff..
sfd_x,sfd_y=obj.sfd()


#plotting sfd bmd
plt.plot(bmd_x,bmd_y)
plt.show()

plt.plot(sfd_x,sfd_y)
plt.show()



