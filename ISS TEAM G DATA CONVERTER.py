import os
import linecache 
def read_and_write_text_files(input_prefix, output_filename, num_files):
    with open(output_filename, 'w') as output_file:
        for i in range(1, num_files + 1):
            input_filename = "C:\\Users\\ak4xb\\OneDrive\\Documents\\vscode projects\\python\\iss 2022-20223 team G text file\\data\\" + f"{input_prefix}{i}.TXT"
            try:
                with open(input_filename, 'r') as input_file:
                    file_content = input_file.read()
                    output_file.write(f"=== {input_filename} ===\n")
                    output_file.write(file_content)
                    output_file.write("\n\n")
            except FileNotFoundError:
                print(f"File not found: {input_filename}")

# Specify the input prefix, output filename, and the number of files
#input_prefix = "file_prefix_"  # Replace with the actual prefix of your files
#output_filename = "output.txt"
#num_files = 5  # Replace with the actual number of files you have

# Call the function
#read_and_write_text_files(input_prefix, output_filename, num_files)


src = "C:\\Users\\ak4xb\\OneDrive\\Documents\\vscode projects\\python\\iss 2022-20223 team G text file\\data\\PO00001.TXT"
f = open(src, "r")
def lineCache(directory, lineNum):
    return linecache.getline(directory, lineNum)
print( lineCache(src, 4) [19:len(lineCache(src, 4))] ) # mission clock
print( lineCache(src, 7) [22:len(lineCache(src, 7))] ) # ambient temp
print( lineCache(src, 8) [19:len(lineCache(src, 8))] ) # ambient humidity
print( lineCache(src, 16) [7:len(lineCache(src, 16))] ) # CO2-1       
print( lineCache(src, 17) [7:len(lineCache(src, 17))] ) # CO2-2
print( lineCache(src, 18) [8:len(lineCache(src, 18))] ) # Temp-1
print( lineCache(src, 19) [8:len(lineCache(src, 19))] ) # Temp-2      

read_and_write_text_files("PO0000", "output.txt", 3)
