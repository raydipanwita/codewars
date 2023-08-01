def maskify(cc):
    if cc == "" or cc == "1":
        return cc
    else:
        return (len(cc[0:-4]) * "#" + cc[-4:]) # used * as it will multiply as the chars from 0 to -4 with #
    pass