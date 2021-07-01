#### PART 1 ####
def insertLineToDict(line: str, students_dict: dict): 
    # get the values from the line
    line_list = line.split(",")

    # if value is illegal, return

    # checking the student's ID
    str_with_tabs_and_spaces = line_list[0]
    # removing spaces from the ID
    list_with_tabs_no_spaces = str_with_tabs_and_spaces.split(" ")
    str_with_tabs_no_spaces = "".join(list_with_tabs_no_spaces)
    # removing tabs from the ID
    list_no_tabs_no_spaces = str_with_tabs_no_spaces.split("\t")
    id_str = "".join(list_no_tabs_no_spaces)
    id_num = int(id_str)
    if (id_str[0] == '0' or len(str(id_num)) != 8):
        return

    # checking the student's name
    temp_name = line_list[1]

    # remove tabs from the string
    name_list_no_tabs = temp_name.split("\t")
    name_str_no_tabs = " ".join(name_list_no_tabs)

    #remove unnecessary spaces
    name_list_with_null = name_str_no_tabs.split(' ')
    name_list_no_null = []
    
    for item in name_list_with_null:
        if item != "":
            name_list_no_null.append(item)

    name = " ".join(name_list_no_null)

    for chr in name:
        if (not( 
        (ord(chr) == ord(' ')) #chr is space
        or (ord(chr) <= ord('z') and ord(chr) >= ord('a')) #chr is uppercase
        or (ord(chr) <= ord('Z') and ord(chr) >= ord('A')) #chr is lowercase 
        )):
            return

    # checking the student's semester
    semester = int(line_list[2])
    if semester < 1:
        return

    # checking the student's HW AVG
    hw_avg = int(line_list[3])
    if (hw_avg <= 50 or hw_avg > 100):
        return


    # at this point of the function, line is legal
    # insert the student to the dictionary
    students_dict[id_num] = [name , semester , hw_avg]
    return
  
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    input_file = open(input_path, "r")
    output_file = open(output_path, "w")
    students_dictionary = {}
    for line in input_file:
        insertLineToDict(line, students_dictionary)
    
    ids_list = []
    for id_num in students_dictionary:
        ids_list.append(id_num)

    ids_list.sort()
    
    grades_sum = 0
    grades_count = 0

    for id_num in ids_list:
        # student's grade is the avg of his hw grade
        # and the last two digits of his ID num
        hw_avg = students_dictionary[id_num][2]
        student_final_grade = (hw_avg + id_num%100)//2
        grades_sum += student_final_grade
        grades_count += 1

        line_to_print = str(id_num) + ", " + str(hw_avg) + ", " + str(student_final_grade) + '\n'
        output_file.write(line_to_print)

    if grades_count == 0:
        return 0
    
    return (grades_sum//grades_count)
    

#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    # Create a count array and count
    # frequencies characters in s2
    s1=s1.lower()
    s2=s2.lower()
    
    if len(s1) == 0 and len(s2) == 0:
        return True
    if len(s1)>len(s2):
        return False
    count = {s2[i] : 0 for i in range(len(s2))}
    
    for i in range(len(s2)):
        count[s2[i]] += 1
    
    # Now traverse through str1 to check
    # if every character has enough counts
    for i in range(len(s1)):
        if (count.get(s1[i]) == None or count[s1[i]] == 0):
            return False
        count[s1[i]] -= 1
    return True