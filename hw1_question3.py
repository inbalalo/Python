def max_grade(list)
    """
    Adds every student's maximal grade (in this subject) to the list 
    """
    for i in range(0, len(list)):
        if list[i][1] => list[i][2]:
           list[i][3] = list[i][1]
        else:
            list[i][3] = list[i][2]
    return list

def compare_subjects_within_student(subj1_all_students, subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    subj1_all_students = max_grade(subj1_all_students)
    subj2_all_students = max_grade(subj2_all_students)
    d = {}

    for i in range(0, len(subj1_all_students):
        d[str(subj1_all_students[i][0])] = subj1_all_students[i][3]

    for i in range(0, len(subj2_all_students):
        if str(subj2_all_students[i][0]) in d:
            if subj2_all_students[i][3] = d[str(subj2_all_students[i][0]]):
                d[str(subj2_all_students[i][0])] = "subj2 + subj1"
            if subj2_all_students[i][3] > d[str(subj2_all_students[i][0])]:
                d[str(subj2_all_students[i][0])] = 'subj2'
            else:
                d[str(subj2_all_students[i][0])] = 'subj1'
    
    return d


if __name__ == '__main__':
    # Question 3
    param1 = [['Yosi', 75, 80], ['Dani', 100, 60], ['Amit', 50, 90], ['Nitzan', 90, 95]]
    param2 = [['Yosi', 85, 95], ['Dani', 50, 60], ['Nati', 95, 90], ['Nitzan', 70, 95]]
    return_value = compare_subjects_within_student(param1, param2)
    print(f"Question 3 solution: {return_value}")  