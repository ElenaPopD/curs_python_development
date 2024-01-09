class BrandedFile():

    def __init__(self, filename):
        self._filename = filename

    def __enter__(self):
        self._file = open(self._filename, "w")
        self._file.write("Scoala Informala\n")
        return self._file
    
    def __exit__(self, *args, **kwargs):
        # print("*args", args)
        # print("**kwargs", kwargs)
        self._file.write("\nCopyright 2023\n")
        self._file.close()
        if args[0] == ValueError:
            return True


with BrandedFile("fisier.txt") as f:
    f.write("Test 1\n")
    raise ValueError()
    f.write("Test 2 \n")


print("gata")
