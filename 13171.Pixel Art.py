class Solution(object):
    def fillColor(self,m,y,c,color):
        color_dict = {'M':[1,0,0],'Y':[0,1,0],'C':[0,0,1],'R':[1,1,0],'V':[1,0,1],'G':[0,1,1],'B':[1,1,1],'W':[0,0,0]}
        need = [0,0,0]
        error = 0
        for i in range(len(color)):
            for j in range(3):
                need[j] += color_dict[color[i]][j]
        m -= need[0]
        y -= need[1]
        c -= need[2]
        for i in range(len(need)):
            if m < 0 or y < 0 or c < 0:
                error += 1
        if error > 0:
            print('NO')
        else:
            print('YES',m,y,c)
while True:
	times = eval(input(''))
	sol = Solution()
	for i in range(times):
		m,y,c,color = input().split(' ')
		m,y,c = int(m),int(y),int(c)
		sol.fillColor(m,y,c,color)
