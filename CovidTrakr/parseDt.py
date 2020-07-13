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
            i = index + len(dataSec)
            while(i < len(data)):
                order = ord(data[i])
                if not ((order < 48 or order > 57) and order != 46):
                    break   
                i = i + 1                 
            while(i < len(data)):
                order = ord(data[i])
                if (order >= 48 and order <= 57) or order == 46 or order == 44:
                    num = num + data[i]
                else:
                    break
                i = i + 1 
            return num



     
        