import os 
import numpy as np

save_path = '/mnt/sda/CityGML/RealCity3D-master/test_out'
v_path = '/mnt/sda/CityGML/RealCity3D-master/test2/53394535_bldg_6697_op2_v.obj'
f_path = '/mnt/sda/CityGML/RealCity3D-master/test2/53394535_bldg_6697_op2_f.obj'
with open(v_path,'r') as f_v:
    lines_v = f_v.readlines()
with open(f_path,'r') as f_f:
    lines_f = f_f.readlines()

total_length = len(lines_f)
save_index = -1
start_line = lines_f[0][2:]
# print(start_line)
line_temp = ''
min_ = 0
max_ = 0
for index, line in enumerate(lines_f):
    print( 'total: ',total_length, 'index: ',index)
    # print('line[0]: ',line[0])
    # print(type(line[0]))
    
    if line[0] == 'o' :
        nums = line_temp.split(' ')
        #print('nums: ',nums)
        nums_int = []
        print('line_temp: ',line_temp)
        for num in nums:
            try:
                num_int = int(num)
                nums_int.append(num_int)
            except:
                a = 1
        print('nums_int: ',nums_int)
        if nums_int != []:
            min_ = min(nums_int)-1
            max_ = max(nums_int)
            #print('min_: ',min_)
            #print('max_: ',max_)
            #print('num_int: ',nums_int)
            nums_int = (np.array(nums_int)-min_).tolist()
            #print('num_int2: ',nums_int)
        save_f = ''
        #print('len(nums_int)/3: ',len(nums_int)//3)
        #print('nums_int: ',nums_int)
        for i in range(len(nums_int)//3):
            temp = nums_int[3*i:3*i+3]
            tenp_str = "f" + " " + str(temp[0]) + " " + str(temp[1]) + " " + str(temp[2]) + "\n"
            save_f+=tenp_str
        save_f = line_temp[:len('o BLD_cea1cfd0-9f4d-4b5b-a94c-4fd559ecaf19')] +'\n' +save_f
        #print(line_temp[:len('o BLD_9220a79b-6ab2-454c-b3c8-69f72038101f')])
        with open(save_path + f'/{save_index}.obj', 'w') as f_save:
            if line[0] == 'o':
                lines_v_save = ''
                for line_v in lines_v[min_:max_]:
                    lines_v_save +=line_v
                f_save.write(lines_v_save)
            f_save.write(save_f)
        line_temp = ''
        save_index+=1
    line_temp+=line
# 
    if save_index >=2:
        break
