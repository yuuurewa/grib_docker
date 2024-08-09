import pygrib
import os

if __name__ == '__main__':
    print('Search for files in the directory: ' + os.getcwd() +'\n')
    for dirpath, _, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            extension = os.path.splitext(filename)[1].lower()
            if extension == '.grib' or extension == '.grib2':
                grbs = pygrib.open(os.path.join(dirpath, filename))
                grbs.seek(0)
                for grb in grbs:
                    print(grb)
                print()
            else:
                continue
