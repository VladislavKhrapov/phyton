my_list = [345, 56.6, 20, 73, 983.2, 5, 25.33, 120.5, 57, 3024]
for view in my_list:
    rub = int(view)
    kk = (view - int(view)) * 100
    print(f'{rub} руб {kk:02.0f} коп')

my_list2 = [345, 56.6, 20, 73, 983.2, 5, 25.33, 120.5, 57, 3024]
print(id(my_list2 ))
my_list2 .sort()
print(id(my_list2 ))
for view2 in my_list2:
    rub = int(view2)
    kk = (view2 - int(view)) * 100
    print(f'{rub} руб {kk:02.0f} коп')


my_list3 = [345, 56.6, 20, 73, 983.2, 5, 25.33, 120.5, 57, 3024]
for view3 in sorted(my_list3)[::-1][:5]:
    rub = int(view3)
    kk = (view3 - int(view3)) * 100
    print(f'{rub} руб {kk:02.0f} коп')

print([f'{int(view3)} руб {(view3 - int(view3)) * 100:02.0f} коп' for view3 in sorted(my_list3)[::-1][:5]])