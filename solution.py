# Python 3 program to find minimum
# number of denominations

def findMin(V,H):

    # All denominations of Indian Currency
    deno = [10,20,40,80,160]
    dict_nyc = {10: 120,20:230,40:450,80:774,160:1400,320:2820}
    dict_india={}
    dict_china={}
    dict_cap_nyc={}
    dict1 = {"Large":10,"XLarge":20,"2XLarge":40,"4XLarge":80,
"8XLarge":160,"10XLarge":320}

    n = len(deno)

    # Initialize Result
    ans = []

    # Traverse through all denomination
    i = n - 1
    while(i >= 0):

        # Find denominations
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])

        i -= 1
    sum_nyc = 0
    # Print result
    for i in range(len(ans)):
        sum_nyc+= (dict_nyc[ans[i]]*H)



        print(ans[i], end = " ")

    print("Sum is $"+ str(sum_nyc))









# Driver Code
if __name__ == '__main__':
    n = 1150
    hrs = 1
    print("Following is minimal number",
        "of change for", n, ": ", end = "")
    findMin(n,hrs)


# JS CODE
# function calculateChange(coins, total) {
#   var sum = 0;
#   var dispatched = [];
#   for (var i = 0; i < coins.length;i++) {
#     dispatched[i] = 0;
#   }
#
#   while (sum < total) {
#     for (var c = 0; c < coins.length; c++) {
#       while (total - sum >= coins[c]) {
#         sum += coins[c];
#         dispatched[c]++;
#       }
#     }
#   }
#   return dispatched;
# }
#
# console.log(calculateChange([50,25,10,5,1],137));




def findMin(V,H):


    deno_nyc = [10,20,40,80,160]
    deno_india = [10,40,80,160]
    deno_china = [10,20,80,160]
    dict_nyc = {10: 120,20:230,40:450,80:774,160:1400,320:2820}
    dict_india={10: 140,40:413,80:890,160:1300,320:2970}
    dict_china={10: 110,20:200,80:670,160:1180}
    dict_cap_nyc={"Large":0,"XLarge":0,"2XLarge":0,"4XLarge":0,"8XLarge":0,"10XLarge":0}
    dict_cap_india={"Large":0,"XLarge":0,"2XLarge":0,"4XLarge":0,"8XLarge":0,"10XLarge":0}
    dict_cap_china={"Large":0,"XLarge":0,"2XLarge":0,"4XLarge":0,"8XLarge":0,"10XLarge":0}
    expected_output = {  "Output": [{"region": "New York","total_cost": "","machines": []},
                                    {"region": "India","total_cost": "","machines": []},
                                    {"region": "China","total_cost": "","machines": []}]     }
    v_nyc = V
    v_india = V
    v_china = V
    n_nyc = len(deno_nyc)
    n_india = len(deno_india)
    n_china = len(deno_china)


    # Initialize Result
    ans_nyc = []
    ans_india = []
    ans_china = []

    # Traverse through all for NYC
    i = n_nyc - 1
    while(i >= 0):

        # Find denominations
        while (v_nyc >= deno_nyc[i]):
            v_nyc -= deno_nyc[i]
            ans_nyc.append(deno_nyc[i])

        i -= 1




     # Traverse through all for india
    i = n_india - 1
    while(i >= 0):

        # Find denominations
        while (v_india >= deno_india[i]):
            v_india -= deno_india[i]
            ans_india.append(deno_india[i])

        i -= 1


     # Traverse through all for china
    i = n_china - 1
    while(i >= 0):

        # Find denominations
        while (v_china >= deno_china[i]):
            v_china -= deno_china[i]
            ans_china.append(deno_china[i])

        i -= 1




    sum_nyc = 0
    sum_india = 0
    sum_china = 0
    # Print result nyc
    for i in range(len(ans_nyc)):
        sum_nyc+= (dict_nyc[ans_nyc[i]]*H)
        print(ans_nyc[i], end = " ")
        if(ans_nyc[i] == 10):
            dict_cap_nyc["Large"]+=1
        elif(ans_nyc[i] == 20):
            dict_cap_nyc["XLarge"]+=1
        elif(ans_nyc[i] == 20):
            dict_cap_nyc["2XLarge"]+=1
        elif(ans_nyc[i] == 20):
            dict_cap_nyc["4XLarge"]+=1
        elif(ans_nyc[i] == 20):
            dict_cap_nyc["8XLarge"]+=1
        elif(ans_nyc[i] == 20):
            dict_cap_nyc["10XLarge"]+=1

    print("Sum is $"+ str(sum_nyc))


    # Print result india
    for i in range(len(ans_india)):
        sum_india+= (dict_nyc[ans_india[i]]*H)
        print(ans_india[i], end = " ")

        if(ans_india[i] == 10):
            dict_cap_india["Large"]+=1
        elif(ans_india[i] == 20):
            dict_cap_india["XLarge"]+=1
        elif(ans_india[i] == 20):
            dict_cap_india["2XLarge"]+=1
        elif(ans_india[i] == 20):
            dict_cap_india["4XLarge"]+=1
        elif(ans_india[i] == 20):
            dict_cap_india["8XLarge"]+=1
        elif(ans_india[i] == 20):
            dict_cap_india["10XLarge"]+=1

    print("Sum is $"+ str(sum_india))

    # Print result china  dict_cap_china  ans_china
    for i in range(len(ans_china)):
        sum_china+= (dict_nyc[ans_china[i]]*H)
        print(ans_china[i], end = " ")
        if(ans_china[i] == 10):
            dict_cap_china["Large"]+=1
        elif(ans_china[i] == 20):
            dict_cap_china["XLarge"]+=1
        elif(ans_china[i] == 20):
            dict_cap_china["2XLarge"]+=1
        elif(ans_china[i] == 20):
            dict_cap_china["4XLarge"]+=1
        elif(ans_china[i] == 20):
            dict_cap_china["8XLarge"]+=1
        elif(ans_china[i] == 20):
            dict_cap_china["10XLarge"]+=1

    print("Sum is $"+ str(sum_china))
    print("China HERE ")
    print(dict_cap_china)



# Driver Code
if __name__ == '__main__':
    n = 1150
    hrs = 1
    print("Following is minimal number",
        "of capacity for", n, ": ", end = "")
    findMin(n,hrs)







# 
# expected_output = {"Output":
#     [{"region": "New York","total_cost": "",
#     "machines": [("8XLarge", 7),("XLarge", 1)]},
#     {"region": "India","total_cost": "","machines": []},
#     {"region": "China","total_cost": "","machines": []}]}
#
# dict_cap_nyc={"Large":1,"XLarge":1,"2XLarge":0,"4XLarge":0,"8XLarge":7,"10XLarge":0}
# dict_cap_india={"Large":0,"XLarge":0,"2XLarge":0,"4XLarge":0,"8XLarge":0,"10XLarge":0}
# dict_cap_china={"Large":0,"XLarge":0,"2XLarge":0,"4XLarge":0,"8XLarge":0,"10XLarge":0}
#
# # print(expected_output["Output"])
# array1 = expected_output["Output"]
# # print(array1[2])
# out_nyc = array1[0]
# out_india = array1[1]
# out_china = array1[2]
# out_china["total_cost"] = "$"+str(10150)
#
# # print(array1[2])
#
# out_nyc["machine"] --> list of tuples
