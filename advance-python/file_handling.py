def read_from_file(filename):
    
    try:
        with open(filename,'r') as f:
            data = f.read()
            print(data) 
    except FileNotFoundError:
        print("File not found")        

def write_to_file(filename,content):
    try:
        with open(filename,'w') as f:
            f.write(content)
    except FileNotFoundError:
        print("File not found")

def append_to_file(filename,content):
    try:

       with open(filename,'a') as f:
         f.write(content)
    except FileNotFoundError:
        print("File not found")        

def copy_binary_file(src,dest):
    try:
        with open(src,'rb') as f_src:
            data = f_src.read()
        with open(dest,'wb') as f_dest:
            f_dest.write(data)    
    except FileNotFoundError:
        print("File not found")        

  
filename = 'example.txt'
content = "Hello welcome to my course\n\n"  
content2 = "Hello how are you!"
append_to_file(filename=filename,content=content)  
append_to_file(filename=filename,content=content2)  

filename_binary = 'bird.png'
filename_binary_dest = 'bird_copy.png'
copy_binary_file(filename_binary,filename_binary_dest)