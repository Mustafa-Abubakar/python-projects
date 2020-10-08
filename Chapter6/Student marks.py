def main():
    total = 0
    print("This Program Calculates the Sum and Average of Subjects You Enter.")
    # Enters the user num of subjects
    num_sub = int(input("Enter how many subjects do you want to calculate: "))
    # opening th file
    res_file = open('Exam_Result.txt','w')
    # using loop to write the mark in a file
    for sub in range(num_sub):
        print("Enter the name of the subject #",sub+1,": ", end='')
        sub_name = input()
        print("Enter The marks of ",sub_name, ': ', end="")
        sub_mark = int(input())
        res_file.write(sub_name + ': ' + str(sub_mark)+ "\n")
        total += sub_mark
        Average = total / num_sub
    res_file.close()
    res_file = open('Exam_Result.txt', 'r')

    print("*"*50)

    print("This is your Exam Result")
    for line in res_file:
        res = line.rstrip('\n')
        print(res)
    res_file.close()

    print("The total result is : ", total)
    print("And the Average is : ", format(Average, '.2f'))

    res_file = open('Exam_Result.txt', 'a')
    res_file.write("The total result is : " + str(total) + '\n')
    res_file.write("And the Average is : " + str(Average))
    res_file.close()

    print("*" * 50)

    print("NOTE: This Data is also saved in a file")

main()