out1 = open('trainval.txt','w')
for i in range(60091,61891):
    out1.write(str(i)+'\n')
out2 = open('test.txt','w')
for i in range(61891,62091):
    out2.write(str(i)+'\n')