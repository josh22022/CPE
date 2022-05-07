class Solution(object):
    def findMissPage(self,total):
        page = []
        i=1
        find=0
        if total != 0:
            while True:
                page.append(i)
                i += 1
                for j in range(1,len(page)+1):
                    if sum(page) - j == total:
                        find += j
                if find > 0:
                    return find, len(page)
        elif total == 0:
            return 0,0
