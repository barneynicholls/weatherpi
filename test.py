from os.path import join

def write():
    print('Creating a new file')
    path = "~/home/pi/Desktop.txt"

    try:
        file = open(join(path),'w')   # Trying to create a new file or open one
        file.write('hello world')
        file.close()

    except:
        print('Something went wrong! Cannot tell what?')

        
if __name__ == "__main__":
    write()