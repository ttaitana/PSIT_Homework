"""classify"""
def clasroom(st_year):
    """print out data"""
    while True:
        stduent = input()
        if stduent == 'END':
            break
        st_year = year(stduent, st_year)
    list_of_year = list()
    _ = [list_of_year.append(i) for i in st_year]
    list_of_year.sort()
    for i in list_of_year:
        list_of_fac = list()
        for j in st_year[i]:
            list_of_fac.append(j)
        list_of_fac.sort()
 
        count = 0
        for student_id in list_of_fac:
            if count == 0:
                print(i, int(student_id), st_year[i][student_id])
            else:
                print('--', int(student_id), st_year[i][student_id])
            count += 1
 
 
def year(stduent, st_year):
    """filtered student"""
    if stduent[:2] not in st_year:
        st_year[stduent[:2]] = {stduent[2:4]:1}
    else:
        if stduent[2:4] not in st_year[stduent[:2]]:
            st_year[stduent[:2]][stduent[2:4]] = 1
        else:
            st_year[stduent[:2]][stduent[2:4]] += 1
    return st_year
 
clasroom(dict())
