# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

def num_teachers(dictionary):
    teachers = dictionary.keys()
    counts = len(teachers)
    return counts

def num_courses(dictionary):
    counts = 0
    for x in dictionary.values():
        counts += len(x)
    return counts

def courses(dictionary):
    single_list = []
    for x in dictionary.values():
        single_list.extend(x)
    return single_list

def most_courses(dictionary):
    name_with_most_courses = None
    max_length = None
    for x in dictionary.keys():
        if max_length == None:
            max_length = len(dictionary[x])
            name_with_most_courses = x
        elif max_length > len(dictionary[x]):
            continue
        else:
            max_length = len(dictionary[x])
            name_with_most_courses = x
    return name_with_most_courses

def stats(dictionary):
    final_list = []
    for x in dictionary.keys():
        temp_list = [x]
        temp_list.append(len(dictionary[x]))
        final_list.append(temp_list)
    return final_list