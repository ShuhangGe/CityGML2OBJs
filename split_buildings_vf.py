import os 


data_path = '/mnt/sda/CityGML/RealCity3D-master/test2/53394535_bldg_6697_op2_.obj'
save_path = '/mnt/sda/CityGML/RealCity3D-master/test2'

with open(data_path,'r') as f:
    lines = f.readlines()
total_length = len(lines)
save_index = 0
# print(start_line)
for index, line in enumerate(lines):
    print( 'total: ',total_length, 'index: ',index)
    # print('line[0]: ',line[0])
    # print(type(line[0]))
    if line[0] == 'o' or line[0] == 'f':
        with open(save_path + f'/53394500_bldg_6697_op2_f.obj', 'a') as f_f:
            f_f.write(line)
    if line[0] == 'v':
        with open(save_path + f'/53394500_bldg_6697_op2_v.obj', 'a') as f_v:
            f_v.write(line)
        # if save_index >=10:
        #     break
        # with open(save_path+'/CityGML_Buildings_tokyo_object_f.obj','a') as f_save:
        #     f_save.write(line)
        #     print( 'total: ',total_length, 'index: ',index)