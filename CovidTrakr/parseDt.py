def stripToNum(textToStrip):
    if isinstance(textToStrip, str):
        #every "i" value is a single char in the string price. ord() gets the ascii values and sees if they
        #are in the range to be considered valid numbers
        num = ""
        for i in textToStrip:
            if (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 46:
                num = num + i
        return float(num)

def getNumDataSection(dataSec,data):
    if isinstance(dataSec,str) and isinstance(data,str):
        index = data.find(dataSec)
        if index != -1:
            num = ''
            rem = ''
            data = data.replace(dataSec,'')
            for i in data:
                order = ord(i)
                if (order < 48 or order > 57) and order != 46:
                    rem = rem + i
                else:
                    break
            data = data.replace(rem,'')
            for i in data:
                order = ord(i)
                if (order >= 48 and order <= 57) or order == 46 or order == 44:
                    num = num + i
                else:
                    break
            return num



     
        