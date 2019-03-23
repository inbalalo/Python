def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    best_in_subject = {}

    for name in subj1_all_students:
        if name in subj2_all_students and name != 'course_name':
            if max(subj1_all_students[name]) > max(subj2_all_students[name]):
                best_in_subject[name] = subj1_all_students['course_name']
            else:
                best_in_subject[name] = subj2_all_students['course_name']
            if max(subj1_all_students[name]) == max(subj2_all_students[name]):
                best_in_subject[name] = subj1_all_students['course_name']+' and '+subj2_all_students['course_name']

    return best_in_subject                        

if __name__ == '__main__':
    # Question 3
    param1 = {'course_name': 'Math', 'Yosi': [75, 80], 'Dani': [100, 60], 'Amit': [50, 90], 'Nitzan': [90, 95]}
    param2 = {'course_name': 'History', 'Yosi': [85, 95], 'Dani': [50, 60], 'Nati': [95, 90], 'Nitzan': [70, 95]}
    return_value = compare_subjects_within_student(param1, param2)
    print(f"Question 3 solution: {return_value}")  