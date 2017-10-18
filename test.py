rom os.path import join
def write():
        print('Creating a new file')
        path = "home/pi"
        name = raw_input('Enter a name for your file: ')+'.txt'  # Name of text file coerced with +.txt

        try:
            file = open(join(path, name),'w')   # Trying to create a new file or open one
            file.close()

        except:
            print('Something went wrong! Cannot tell what?')
            sys.exit(0) # quit Python