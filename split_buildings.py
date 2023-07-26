import os 


data_path = '/mnt/sda/CityGML/tokyo/CityGML_Buildings_tokyo_object_split_one/Tokyo_Buildings_split.obj'
save_path = '/mnt/sda/CityGML/tokyo/CityGML_Buildings_tokyo_object_split'
v_path = '/mnt/sda/CityGML/tokyo/CityGML_Buildings_tokyo_object/CityGML_Buildings_tokyo_object_v.obj'
f_path = '/mnt/sda/CityGML/tokyo/CityGML_Buildings_tokyo_object/CityGML_Buildings_tokyo_object_f.obj'
with open(v_path,'r') as f_v:
    lines_v = f_v.read()
with open(f_path,'r') as f_f:
    lines_f = f_f.readlines()

total_length = len(lines_f)
save_index = -1
start_line = lines_f[0][2:]
# print(start_line)
for index, line in enumerate(lines_f):
    print( 'total: ',total_length, 'index: ',index)
    # print('line[0]: ',line[0])
    # print(type(line[0]))
    if line[0] == 'o':
        save_index+=1
    with open(save_path + f'/{save_index}.obj', 'a') as f_save:
        if line[0] == 'o':
            f_save.write(lines_v)
        f_save.write(line)
        # if save_index >=10:
        #     break
        # with open(save_path+'/CityGML_Buildings_tokyo_object_f.obj','a') as f_save:
        #     f_save.write(line)
        #     print( 'total: ',total_length, 'index: ',index)