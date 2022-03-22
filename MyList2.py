myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]    #Create a list with different types of value

for item in myMixedTypeList:                                                 #Run For loop for access element one by one
    print("{} is of the data type {}".format(item,type(item)))               #Print element one by one