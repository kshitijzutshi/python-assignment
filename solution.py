# import json


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
    expected_output = {"Output": [{"region": "New York","total_cost": "","machines": []},
                                    {"region": "India","total_cost": "","machines": []},
                                    {"region": "China","total_cost": "","machines": []}]}
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
        elif(ans_nyc[i] == 40):
            dict_cap_nyc["2XLarge"]+=1
        elif(ans_nyc[i] == 80):
            dict_cap_nyc["4XLarge"]+=1
        elif(ans_nyc[i] == 160):
            dict_cap_nyc["8XLarge"]+=1
        elif(ans_nyc[i] == 320):
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
        elif(ans_india[i] == 40):
            dict_cap_india["2XLarge"]+=1
        elif(ans_india[i] == 80):
            dict_cap_india["4XLarge"]+=1
        elif(ans_india[i] == 160):
            dict_cap_india["8XLarge"]+=1
        elif(ans_india[i] == 320):
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
        elif(ans_china[i] == 40):
            dict_cap_china["2XLarge"]+=1
        elif(ans_china[i] == 80):
            dict_cap_china["4XLarge"]+=1
        elif(ans_china[i] == 160):
            dict_cap_china["8XLarge"]+=1
        elif(ans_china[i] == 320):
            dict_cap_china["10XLarge"]+=1

    print("Sum is $"+ str(sum_china))
    print("China HERE ")
    print(dict_cap_china)


    # print(expected_output["Output"])
    array1 = expected_output["Output"]
    # print(array1[2])
    out_nyc = array1[0]
    out_india = array1[1]
    out_china = array1[2]
    out_nyc["total_cost"] = "$"+str(sum_nyc)
    out_india["total_cost"] = "$"+str(sum_india)
    out_china["total_cost"] = "$"+str(sum_china)

    # print(array1[2])
    out_nyc["machines"] = [(k, v) for k, v in dict_cap_nyc.items() if v>0]
    out_india["machines"] = [(k, v) for k, v in dict_cap_india.items() if v>0]
    out_china["machines"] = [(k, v) for k, v in dict_cap_china.items() if v>0]
    print("____________________FINAL OUTPUT________________________________________")
    print(expected_output)

    # print(json.dumps(expected_output,indent = 1))


# Driver Code
if __name__ == '__main__':
    n = 1150
    hrs = 1
    print("Following is minimal number",
        "of capacity for", n, ": ", end = "")
    findMin(n,hrs)








# expected_output = {"Output":
#     [{"region": "New York","total_cost": "",
#     "machines": []},
#     {"region": "India","total_cost": "","machines": []},
#     {"region": "China","total_cost": "","machines": []}]}
#
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
# out_india["machines"] = [(k, v) for k, v in dict_cap_india.items() if v>0]
#
# print(out_india["machines"])
