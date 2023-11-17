from usfutils.dir import scandir

if __name__ == '__main__':
    for item in scandir("C:\\Users\\A\\Desktop", suffix=('.png','.md')):
        print(item)
