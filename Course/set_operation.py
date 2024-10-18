#union: combining all elements and and only one coccurence of common elements
#intersection: common elements
#difference: only mentioning elements of first mentioned set and there will be no common elements
#symmetric difference: all elements except common elements

a = {1,2,3,10,6,9,17}
b = {72,1,4,10,54,2,20}

print("The union is: ",a | b)
print("The intersection is: ",a & b)
print("The difference is: ", a - b)
print("The symmetric difference is: ", a ^ b)