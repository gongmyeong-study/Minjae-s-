 # while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
 
 
# number_list = range(1, 1001)

# for a in number_list: 
#     if a % 3 == 0: 
#         print("3의 배수 : " + str(a))

a = 1
while a <= 1000: 
        
    if a % 3 == 0: 
        print("3의 배수 : " + str(a))
    a = a + 1 