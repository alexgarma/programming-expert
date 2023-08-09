def sort_employees(employees, sort_by):
    def check_sort_key(item,sort_key = sort_by):
        if sort_key == "name":
            return item[0]
        elif sort_key == "age":
            return item[1]
        else:
            return item[2]
    return sorted(employees,key = check_sort_key)