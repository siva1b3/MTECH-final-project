import numpy as np
import pandas as pd
import lhsmdu

list_of_parameters = ["Observed_vehicles","Look_ahead_distance_Min","Look_ahead_distance_Max","Look_back_distance_Min","Look_back_distance_Max","Waiting_time_before_Diffusion","Minimum_head_way_front_rear","Average_standstill_distance","Additive_part_of_safety_distance","Multiplicative_part_of_safety_distance","Minimum_lateral_distance_at_0_Kmph_class_10","Minimum_lateral_distance_at_50_Kmph_class_10","Minimum_lateral_distance_at_0_Kmph_class_20","Minimum_lateral_distance_at_50_Kmph_class_20","Minimum_lateral_distance_at_0_Kmph_class_30","Minimum_lateral_distance_at_50_Kmph_class_30","Minimum_lateral_distance_at_0_Kmph_class_40","Minimum_lateral_distance_at_50_Kmph_class_40","Minimum_lateral_distance_at_0_Kmph_class_50","Minimum_lateral_distance_at_50_Kmph_class_50","Minimum_lateral_distance_at_0_Kmph_class_60","Minimum_lateral_distance_at_50_Kmph_class_60","Minimum_longitudinal_speed_for_lateral_movement","Standstill_distance_in_front_of_static_obstacles","Cooperative_lane_change - maximum_speed_difference","average_stand_stil_distance"]
list_of_parameters
# len(list_of_parameters)

list_of_minimum_values = [0,0,30,0,30,3,0.1,1,0.1,0,0.15,0.5,0.2,1,0.5,1,0.5,1,1,2.5,1,2.5,5,0.25,10,0.5]
list_of_maximum_values = [100,30,70,30,70,30,1,2,2,3,0.5,2,1,3,1,3,1,3,2.5,5,2.5,5,15,2.5,35,2.5]
list_of_values = [[0,100],[0,30],[30,70],[0,30],[30,70],[3,30],[0.1,1],[1,2],[0.1,2],[0,3],[0.15,0.5],[0.5,2],[0.2,1],[1,3],[0.5,1],[1,3],[0.5,1],[1,3],[1,2.5],[2.5,5],[1,2.5],[2.5,5],[5,15],[0.25,2.5],[10,35],[0.5,2.5]]
len(list_of_values)


# using naive method 
# to convert lists to dictionary 
parameters_dictionary = {} 
for key in list_of_parameters: 
    for value in list_of_values: 
        parameters_dictionary[key] = value
        list_of_values.remove(value)
        break
# print(parameters_dictionary)


while k = 1:
    try:
        no_of_sample = int(input("enter number of samples needed")
        k = 2
    except:
        print("Enter the value again")
        k = 1

df = pd.DataFrame(index=list(range(no_of_sample)), columns=list_of_parameters)

z = len(df.columns)

for val in range(z):
    k = lhsmdu.sample(1, 150)
    k = (k*(list_of_maximum_values[val]-list_of_minimum_values[val]))+list_of_minimum_values[val]
    k = k.transpose()
    df_temp= pd.DataFrame(k)
    df.iloc[:,val] = df_temp
  
df.to_excel("latin_hypercube_sampling.xlsx")
