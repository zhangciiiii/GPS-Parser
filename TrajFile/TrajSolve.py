
start_time = 1156.5986
end_time = 1184.3985

num_lines = 0
for _ in open("gps_odom1.txt"): 
    num_lines += 1

current_time = start_time

with open("New_gps_odom1.txt","w") as f:

    for Line in open("gps_odom1.txt"):  
        LineList = Line.replace("\n", "").split(" ")
        #print(LineList)
        current_time = current_time +(end_time-start_time)/num_lines
        f.write (str(current_time)+ " " + LineList[0] + " " + LineList[1] + " " + LineList[2] + " " + "0 0 0 1" +"\n")  

with open("New_odom51_20.txt","w") as f:

    for Line in open("odom51_20.txt"):  
        LineList = Line.replace("\n", "").split("\t")
        
        f.write (LineList[0] + " " + LineList[1] + " " + LineList[2] + " " + LineList[3]  + " " + "0 0 0 1" +"\n") 
