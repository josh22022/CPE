class Solution(object):
    def findStep(self,cases):
        for i in range(cases):
            position = input()
            x1,y1,x2,y2 = position.split(' ')
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            row1 = x1 + y1
            row2 = x2 + y2
            step1 , step2 = 0, 0
            step3 = 0
            while y1 > 0:
                x1 += 1
                y1 -= 1
                step1 += 1
            while x2 > 0:
                x2 -= 1
                y2 += 1
                step2 +=1
            for j in range(row1+1,row2):
                step3 += j
            total = step1 + step2 + step3 + row2 - row1
            print('Case',i+1,':',total)
