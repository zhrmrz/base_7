class Sol:
    def base_7(self,num):
        res=''
        while (num>0):
            r=num%7
            res+=str(r)
            num=num//7
        return res[::-1]
