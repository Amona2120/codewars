def increment_string(strng):
    if strng == "" or not strng[-1].isnumeric():
        return strng + "1"

    if strng[-1] != "9":
         return strng[:-1]+f"{int(strng[-1])+1}"

    if strng[-1].isnumeric() and int(strng[-1]) == 9:
        strng = strng[:-1] + "0"
    n = 2
    while strng[-n].isnumeric() and int(strng[-n]) == 9:
        strng = strng[:-n] + "0" + strng[-n+1:]
        n+=1
    if strng[-n].isnumeric():
        return strng[:-n] + f"{int(strng[-n])+1}" + strng[-n+1:]
    return strng[:-n+1] + "1" + strng[-n+1:]
