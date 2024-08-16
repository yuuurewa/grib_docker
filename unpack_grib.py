import os
import pygrib
from typing import Iterator, Any

PATH_TO_GRIB = os.path.join(os.path.dirname(__file__), 'grib_files')


def get_grib_files() ->Iterator[str]:
    return (f for f in os.listdir(PATH_TO_GRIB) if f.lower().endswith(('.grib', '.grib2')))


def unpack_grib_files(grib_file: str) -> list[Any]:
    print('Unpack file ' + grib_file + '\n')
    grib_list = pygrib.open(os.path.join(PATH_TO_GRIB, grib_file)).read()
    return grib_list


def main() -> None:
    for grib_file in get_grib_files():
        for grib_msg in unpack_grib_files(grib_file):
            print(grib_msg)
        print(50 * '-')


if __name__ == '__main__':
    main()
