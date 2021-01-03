details_list=["idan hakimi" , 28 , "idan@gmail,com" , "0551234567"]
print("full name: " + details_list[0] + "\nage: " + str(details_list[1]) + "\nmail: " + details_list[2] + "\nphone: " + details_list[3])
ip_list=["1.1.1.1","2.2.2.2"]
print(ip_list)
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
print(ip_list)
ip_list.pop(2)
print(ip_list)
print("ip list length is: " + str(len(ip_list)) + "\n and the ip list is: " + str(ip_list))