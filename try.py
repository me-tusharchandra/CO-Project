def convertToDecimal(bin_str):
    """Handles binary number as strings"""
    bin_num = str(bin_str)
    # print(bin_num)
    toRet = 0
    n = len(bin_num)
    for i in range(n):
        if bin_num[n - i - 1] == "1":
            toRet += pow(2, i)
        else:
            continue
    return toRet


num = "00001111"

print(convertToDecimal(str(num)))
