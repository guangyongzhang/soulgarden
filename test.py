# Load Data from file
import xlrd
import json
workbook =xlrd.open_workbook('E:\\Work\\DoubleColorBall\\Book1.xlsx')
worksheets = workbook.sheet_names()
print('worksheets is %s' %worksheets)

print("Read Data From Sheet1")
worksheet1 = workbook.sheet_by_name(u'Sheet1')
num_rows = worksheet1.nrows
num_column = worksheet1.ncols


arr=[]
for curr_row in range(num_rows):
    row = worksheet1.row_values(curr_row)
    jsonRow = "{"
    for curr_column in range(num_column):
    	cell_value = worksheet1.cell_value(curr_row, curr_column) 
    	if(curr_column == 0):
    	
    		jsonRow = jsonRow + "Number:"+str(int(cell_value))+","
    	
    	elif(curr_column == num_column-1 ):
    	
    		jsonRow = jsonRow +"BlueNumber:"+str(int(cell_value))+"}"
    	
    	else :
    	
    		jsonRow = jsonRow +"RedNumber"+str(curr_column)+":"+str(int(cell_value))+","
    	
    arr.append(jsonRow)
    

jsonData= json.dumps(arr,sort_keys=True,indent=4)
print(jsonData)

# define a dictionary
# Calculate Region 1-11 , 12-22,23-33 and Append  to dictionary
# Caluclate Average Data of region in history(1,2,3)

# Calculate  length of last number in vertical(Maximum space)
# Given 20 record with same range

# Calculate Linked Number(2,3,4,5)
# Calculate Two Linked Number(2,3)
# Calculate repeat number in vertical 
# Calculate right hash number and length   (345)
# Calculate left hash number and length (543)

