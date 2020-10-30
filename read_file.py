with open("ciou.txt", "r") as f:
    t = f.readline()

ind = 0
cnt = 0
while True:
    temp = t.find("Epoch mAP", ind)
    if temp == -1 : break
    print(t[temp+11:temp+20])
    ind = temp + 1
    cnt += 1
print(cnt)
#t.find("Epoch mAP")
#print(t)