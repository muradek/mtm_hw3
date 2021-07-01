#### PART 1 ####
    
# check if a line in the input file is legal
# if its legal, insert to the dictionary 
def insertLineToDict(line: str, students_dict: dict): 
    # get the values from the line
    line_list = line.split(",")
    id_num = int(line_list[0])
    semester = int(line_list[2])
    hw_avg = int(line_list[3])

    temp_name = line_list[1]
    name_list = temp_name.split(' ')
    no_spaces_name_list = []
    for item in name_list:
        if item != "":
            no_spaces_name_list.append(item)

    name = " ".join(no_spaces_name_list)

    # check if values are legal
    # if not, return
    if (str(id_num)[0] == '0' or len(str(id_num)) != 8):
        return

    for chr in name:
        if (not( 
        (ord(chr) == ord(' ')) #chr is space
        or (ord(chr) <= ord('z') and ord(chr) >= ord('a')) #chr is uppercase
        or (ord(chr) <= ord('Z') and ord(chr) >= ord('A'))) #chr is lowercase
        ): 
            return
    
    if semester < 1:
        return

    if (hw_avg <= 50 or hw_avg > 100):
        return

    # at this point of the function, line is legal
    # insert the student to the dictionary
    students_dict[id_num] = [name , semester , hw_avg]
  




# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    


    
    raise NotImplementedError


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    # TODO: implement here
    raise NotImplementedError
