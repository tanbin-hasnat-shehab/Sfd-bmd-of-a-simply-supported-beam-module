

class beam():
    def __init__(self,input_arr,length,omega):
        self.input_arr=input_arr
        self.length=length
        self.omega=omega
        self.RA,self.RB=self.Reactions()


    def Reactions(self):
        c=0
        for i in range(len(self.input_arr)):
            c=c+self.input_arr[i][0]*self.input_arr[i][1]
        RB=(c+self.omega*self.length**2/2)/self.length
        d=0
        for i in range(len(self.input_arr)):
            d=d+self.input_arr[i][1]
        RA=(d+self.omega*self.length)-RB
        self.RB=RB
        self.RA=RA
        return RA,RB
    def sfd(self):
        sfd_x=[]
        sfd_y=[]
        sfd_x.append(0)
        sfd_x.append(0)
        
        for i in range(len(self.input_arr)):
            sfd_x.append(self.input_arr[i][0])
            sfd_x.append(self.input_arr[i][0])
        sfd_x.append(self.length)
        sfd_x.append(self.length)

        sfd_y.append(0)
        if self.input_arr[0][0]==0:
            sfd_y.append(self.RA-self.input_arr[0][1])
        else:
            sfd_y.append(self.RA)
        for i in range(len(self.input_arr)):
            if i==0:
                sfd_y.append(self.RA-self.omega*self.input_arr[i][0])
                sfd_y.append(self.RA-self.omega*self.input_arr[i][0]-self.input_arr[i][1])

            if i>0:
                
                sfd_y.append(sfd_y[len(sfd_y)-1]-self.omega*(self.input_arr[i][0]-self.input_arr[i-1][0]))
                sfd_y.append(sfd_y[len(sfd_y)-1]-self.input_arr[i][1])

        #sfd_y.append(sfd_y[len(sfd_y)]-self.omega*(self.length-self.input_arr[len(self.input_arr)][0]))
        sfd_y.append(self.RB)
        sfd_y.append(0)

        sfd_x.append(0)
        sfd_y.append(0)

        return sfd_x,sfd_y
    def bmd(self):
        bmd_x=[]
        bmd_y=[]
        bmd_x.append(0)
        bmd_y.append(0)

        for i in range(len(self.input_arr)):
            bmd_x.append(self.input_arr[i][0])
            if i==0:
                bmd_y.append(self.RA*self.input_arr[i][0]-self.omega*self.input_arr[i][0]**2/2)
            if i>0:
                tr=0
                for j in range(0,i):
                    tr=tr+(self.input_arr[i][0]-self.input_arr[j][0])*self.input_arr[j][1]
                
                bmd_y.append(self.RA*self.input_arr[i][0]-self.omega*self.input_arr[i][0]**2/2-tr)





        bmd_x.append(self.length)
        bmd_y.append(0)
        bmd_x.append(0)
        bmd_y.append(0)
        return bmd_x,bmd_y