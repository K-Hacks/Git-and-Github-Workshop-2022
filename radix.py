num = 0
#---------------------------------------------------------------------------------------
    # finding the largest value
    max = a[0]
    for x in a:
        if x>max:
            max=x   # now the largest value is set at max
#---------------------------------------------------------------------------------------
    # now we need to find the number of digits in the max value
    while (max>0):
        num +=1
        max = max/10  # by doing thing we can find the number of digits in max
#---------------------------------------------------------------------------------------
    # now we need to make B a 3d array with 10 sub sections
    for x in range(0,num):
        B = [[] for _ in range(10)]
        for number in a:            # for every number in a
            temp = number//10**(x)%10      # short cut to get the last second last and soo on at evey itration
            B[temp].append(number)         # add the number to the correct slot
        # take all the values from b and keep in a
        i=0
        for x in range(0,10):
            for j in range(len(B[x])):
                a[i] = B[x][j]
                i+=1 
