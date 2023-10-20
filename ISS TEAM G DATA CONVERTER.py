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


lines = [4, 7, 8, 16, 17, 18, 19]

print(linecache.getline(src, 4)[19:len(linecache.getline(src, 4))]) # mission clock
print(linecache.getline(src, 7)[22:len(linecache.getline(src, 7))]) # ambient temp
print(linecache.getline(src, 8)[19:len(linecache.getline(src, 8))]) # ambient humidity
print(linecache.getline(src, 16)[7:len(linecache.getline(src, 16))]) # CO2-1       
print(linecache.getline(src, 17)[7:len(linecache.getline(src, 17))]) # CO2-2
print(linecache.getline(src, 18)[8:len(linecache.getline(src, 18))]) # Temp-1
print(linecache.getline(src, 19)[8:len(linecache.getline(src, 19))]) # Temp-2      

read_and_write_text_files("PO0000", "output.txt", 3)