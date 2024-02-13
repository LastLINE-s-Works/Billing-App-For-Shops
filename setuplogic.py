def setupcheck():
    check_key = input("Enter 22 Digit Setup Key: ")
    with open("setupkey","r") as f:
        valid_key = f.read()
    if check_key != valid_key:
        print("Wrong Key")
        quit()

#int(good_a_mrp)+int(good_extra_1_mrp)+int(good_extra_2_mrp)+int(good_extra_3_mrp)+int(good_extra_4_mrp)+int(good_extra_5_mrp)+int(good_extra_6_mrp)+int(good_extra_7_mrp)+int(good_extra_8_mrp)+int(good_extra_9_mrp)+int(good_extra_10_mrp)