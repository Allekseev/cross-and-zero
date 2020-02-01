from random import choices
import  copy



class Template:
    def __init__(self,array,authority):
        self.authority = authority
        self.sizeX = len(array)
        self.sizeY = len(array[0])
        self.templating(array)

    def templating(self,array):
        self.toStr = ''
        self.variants=[]
        for x in (0, len(array) - 1):
            for y in (0, len(array[0]) - 1):
                for x0y1 in range(2):
                    var = ''
                    varS=''
                    start1 = (x0y1 == 0) * x + x0y1 * y
                    start2 = x0y1 * x + (x0y1 == 0) * y
                    end1 = (x0y1 * len(array[0]) + (x0y1 == 0) * len(array) + 1) * (start1 == 0) - 1
                    end2 = ((x0y1 == 0) * len(array[0]) + x0y1 * len(array) + 1) * (start2 == 0) - 1
                    width=0
                    c=1
                    height=0
                    for i in range(start1, end1, -(start1 != 0)+(start1==0)):
                        for j in range(start2, end2, -(start2 != 0)+(start2==0)):
                            #print(i,j,x0y1,'*',x,y)
                            width+=c
                            var += array[i * (x0y1 == 0) + j * x0y1][j * (x0y1 == 0) + i * x0y1]
                            varS+= array[i * (x0y1 == 0) + j * x0y1][j * (x0y1 == 0) + i * x0y1]
                        height+=1
                        c=0
                        var += '*'
                    if (varS,width,height) not in self.variants:
                        self.variants.append((varS,width,height))
                    if self.toStr:
                        if var > self.toStr:
                            self.toStr = var
                    else:
                        self.toStr = var

    def searching(self,map):
        #print(self.points)
        self.points=[]
        for var in self.variants:
            area={}
            starts={}
            pTurns = {}
            for x in range (16-var[1]):
                for y in range (16-var[2]):
                    area[(x,y)]=[0]
            while area:
                newArea = {}
                for point in area:
                    #print(area)
                    for step in area[point]:
                        start = (point[0] - (step % var[1]), point[1] - (step // var[1]))
                        flag = False
                        if map[point[0]][point[1]] == var[0][step] or var[0][step] == 'n':
                            flag = True
                            if not step:
                                starts[point] = False
                        elif map[point[0]][point[1]] == '0' and var[0][step] == 'I' and (not step or not starts[start]):
                            flag = True
                            starts[start] = True
                            pTurns[start] = point
                        if flag:
                            if step == len(var[0])-1:
                                if starts[start] and pTurns[start] not in self.points:
                                    self.points.append(pTurns[start])
                            else:
                                newPoint = (start[0] + ((step + 1) % var[1]), start[1] + ((step + 1) // var[1]))
                                if newPoint in newArea:
                                    newArea[newPoint].append(step + 1)
                                else:
                                    newArea[newPoint] = [step + 1]
                area = newArea



class AI:
    def __init__(self,name,side):
        if side=='x':
            self.remap = {'x': 'I', 'o': 'e', '.': '0'}
        else:
            self.remap = {'x': 'e', 'o': 'I', '.': '0'}
        self.name=name
        self.humanTemplates1()
        self.end=False
    def humanTemplates1(self):
        def angle(arr):
            l=len(arr)
            result=[]
            for x in range(l):
                line=[]
                for y in range(l):
                    if x == y:
                        line.append(arr[x])
                    else:
                        line.append('n')
                result.append(line)
            return result

        self.templates=[]

        template=['I','I','I','I','I']
        self.templates.append(Template([template, ], 9))
        template = angle(template)
        self.templates.append(Template(template, 9))

        template=['I','e','e','e','e']
        self.templates.append(Template([template, ], 8))
        template = angle(template)
        self.templates.append(Template(template, 8))

        template = ['e', 'I', 'e', 'e', 'e']
        self.templates.append(Template([template, ], 8))
        template = angle(template)
        self.templates.append(Template(template, 8))

        template = ['e', 'e', 'I', 'e', 'e']
        self.templates.append(Template([template, ], 8))
        template = angle(template)
        self.templates.append(Template(template, 8))

        template = ['0', 'I', 'I', 'I', 'I', '0']
        self.templates.append(Template([template, ], 7))
        template = angle(template)
        self.templates.append(Template(template, 7))

        template=['I','e','e','e','0']
        self.templates.append(Template([template, ], 6))
        template = angle(template)
        self.templates.append(Template(template, 6))

        template = ['0', 'e', 'I', 'e', 'e']
        self.templates.append(Template([template, ], 5))
        template = angle(template)
        self.templates.append(Template(template, 5))

        template = ['e', 'I', 'e', 'e', '0']
        self.templates.append(Template([template, ], 5))
        template = angle(template)
        self.templates.append(Template(template, 5))

        template = ['0', 'I', 'I', 'I', '0']
        self.templates.append(Template(template, 4))
        template = angle(template)
        self.templates.append(Template(template, 4))

        template = ['0', 'I', 'I', '0']
        self.templates.append(Template([template, ], 3))
        template = angle(template)
        self.templates.append(Template(template, 3))

        template = ['I', 'e', 'e']
        self.templates.append(Template([template, ], 2))
        template = angle(template)
        self.templates.append(Template(template, 2))

        template = ['I', 'I']
        self.templates.append(Template([template, ], 1))
        template = angle(template)
        self.templates.append(Template(template, 1))

        template = ['I', 'e']
        self.templates.append(Template([template, ], 1))
        template = angle(template)
        self.templates.append(Template(template, 1))

        self.templates.append(Template([['I', ], ], 0))

    def changeMap(self,map):
        newMap=copy.deepcopy(map)
        for x in range(len(newMap)):
            for y in range(len(newMap)):
                newMap[x][y]=self.remap[newMap[x][y]]
        return newMap

        def simpleTurn(self,map):
        newMap=self.changeMap(map)
        for template in self.templates:
            template.searching(newMap)
            if template.points:
                print(template.authority)
                if template.authority==self.templates[0].authority:
                    self.end=True
                bestPoints=[]
                maximum=-1
                for point in template.points:
                    minimum=min((point[0],point[1],14-point[0],14-point[1]))
                    if maximum < minimum:
                        maximum = minimum
                        bestPoints=[point,]
                    elif maximum == minimum:
                        bestPoints.append(point)
                return choices(bestPoints)[0]
        return  0/0


map=[]
for x in range(15):
    ar=[]
    for y in range(15):
        ar.append('.')
    map.append(ar)
#print(a.points)
for x in range(15):
    print(map[x])
ai1=AI('1','x')
ai2=AI('2','o')
print('0')
while not(ai1.end or ai2.end):
    point=ai1.simpleTurn(map)
    map[point[0]][point[1]]='x'
    point = ai2.simpleTurn(map)
    map[point[0]][point[1]] = 'o'
    for x in range(15):
        print(map[x])
    print()
