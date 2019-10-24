name_list = [{"name": "Ram"}, {"name": "Shyam"}, {"name": "Hari"}, {"name": "Ram"}, {"name": "Shyam"}]
all_name_list = []
for name_dict in name_list:
    # name_dict return dictionary
    for name in name_dict.values():
        # return all values from dictionary & append it on a new list
        all_name_list.append(name)
# set don't allow duplicate members
print(set(all_name_list))
