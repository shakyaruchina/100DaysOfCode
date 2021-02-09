row1 = ["Z", "Z", "Z"]
row2 = ["Z", "Z", "Z"]
row3 = ["Z", "Z", "Z"]
map = [row1,row2,row3]
print(f" {row1}\n {row2}\n {row3}\n ")
position = input("Where do you want to put your treaure? ")

#assigning user input integer to horizontal and vertical
horizontal = int(position[0])
vertical = int(position[1])
#selected_row = map[vertical-1]
#selected_row[horizontal-1]="X"
map[vertical-1][horizontal-1] = "X"
#treasure dropped
print(f" {row1}\n {row2}\n {row3}\n ")