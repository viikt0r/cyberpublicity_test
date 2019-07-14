import re
import sys
from datetime import datetime

class Data:

    def __init__(self):
        self._year = None
        self._make = None
        self._model = None
        self._indice = None

    def year(self):
        return self._year

    def make(self):
        return self._make

    def model(self):
        return self._model

    def indice(self):
        return self._indice

    def set_record(self, string, record):
        try:
            if "year" == string:
                self._year = record
            elif "make" == string:
                self._make = record
            elif "model" == string:
                self._model = record
            elif "indice" == string:
                self._indice = record
        except:
            #print("'set_record' Unexpected error:", sys.exc_info()[0])
            pass

    def __str__(self):
        return self._year + self._make + self._model + self._indice

def dict_values(adict):
    try:
        keys = adict.keys()
        keys.sort()
        return map(adict.get, keys)
    except:
        print("'dict_values' Unexpected error:", sys.exc_info()[0])

def verify_datetime(mydate):
    try:
        datetime_object = datetime.strptime(mydate, '"%b %d %Y %H:%M:%S:%f%p"')
        return datetime_object
    except:
        return mydate


def regex_str(string):
    try:
        return re.compile(
            # ",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)").split(newstr)
            "(?:,\s|,)(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)").split(string)
    except:
        print("'regex_str' Unexpected error:", sys.exc_info()[0])
        return string


def read_csv(csv_file):
    try:
        result = {}
        header = []
        with open(csv_file, 'r') as f:

            rows = f.readlines()
            rows = list(map(lambda x: x.strip(), rows))

            titre = True
            full_line = None
            line_count = 0

            for row in rows:

                # build the header line
                if titre:
                    header.append(regex_str(row))
                    total = len(regex_str(row))
                    titre = False
                else:
                    # multi line case management
                    if full_line is None:
                        full_line = row
                    else:
                        full_line += row

                    # if the number of header columns matches the same column number for a row
                    if len(regex_str(full_line)) == total:
                        line_count += 1

                        d = Data()
                        # initializes a default key
                        d.set_record("indice", line_count)

                        myobj = {}

                        indice = 0
                        for line in regex_str(full_line):
                            # get the header
                            mystring = header[0][indice]
                            mystring = mystring.replace('"', '')

                            # convert date
                            line = verify_datetime(line)

                            myobj[mystring] = line

                            # build object d
                            d.set_record(mystring, line)

                            indice += 1

                        full_line = None

                        index = None
                        if d.year() != None and d.make() != None and d.model() != None:
                            index = d.year() + d.make() + d.model() + str(d.indice())
                        else:
                            index = d.indice()
                        result.setdefault(index, myobj)

        return result
    except IOError:
        print("The file doesn't exist.")
    except:
        print("'read_csv' Unexpected error:", sys.exc_info()[0])
        return result


if __name__ == "__main__":
    try:
        csvFile = None
        csvFile = sys.argv[1]

        if csvFile.split('.')[-1] != "csv":
            print("The file must be in the 'csv' format")
            sys.exit()

        # read csv
        objects = read_csv(csvFile)
        if len(objects) == 0:
            print("no data")
        else:
            objects = dict_values(objects)

            for obj in objects:

                # Enter obj["column_name"]
                print (obj["year"]+"\t"+obj["make"]+"\t"+obj["model"])

                """ For show entrydate :
                obj["entrydate"].strftime("%m/%d/%Y, %H:%M:%S")
                """

    except IndexError:
        print("Enter a file name as a parameter")