# Erick Jimenez
# PSID: 1463639
# Comments: I really did struggle coming up with something to work and creating this. Due to my lack of understanding and recognition. Going to have to do a lot of the practice labs from the beginning. Don't want to struggle for the final. 
month_list = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6", "july": "7",
              "august": "8", "september": "9", "october": "10", "november": "11", "december": "12"}

input_file = open('C:\\Users\\Infer\\OneDrive\\Desktop\\Python\\Homework 2\\Blackboard\\inputDates.txt', 'r')
output_file = open('C:\\Users\\Infer\\OneDrive\\Desktop\\Python\\Homework 2\\Blackboard\\parsedDates.txt', 'w')

for each in input_file:
    if each != "-1":
        lis = each.split()
        if len(lis) >= 3:
            month = lis[0]
            day = lis[1]
            year = lis[2]

            if month.lower() in month_list:
                comma = day[-1]
                if comma == ',':
                    day = day[:len(day) - 1]
                    month_number = month_list[month.lower()]
                    ans = month_number + "/" + day + "/" + year

                    output_file.write(ans)
                    output_file.write("\n")

output_file.close()
input_file.close()
