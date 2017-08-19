test = [2]
count = 1

for e in test:
    test.append(e*2)
    count += 1
    if count%500==0:
        print(test)
    if count == 501:
        break


    
