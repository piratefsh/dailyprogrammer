
def std_dev(inputs):
    values      = [int(elem) for elem in inputs.split(' ')]
    mean        = sum(values) * 1.0 / len(values)
    variance    = sum([(elem - mean) ** 2 for elem in values]) / len(values)
    std_dev     = variance ** 0.5
    print "%.4f" % std_dev

std_dev('5 6 11 13 19 20 25 26 28 37')
std_dev('266 344 375 399 409 433 436 440 449 476 502 504 530 584 587')
std_dev('809 816 833 849 851 961 976 1009 1069 1125 1161 1172 1178 1187 1208 1215 1229 1241 1260 1373')