def anos(ano):
    if ano % 4 == 0:
        if ano % 400 != 0 and ano % 100 == 0:
            return False;
        else:
            return True;
    else:
        return False;

print((anos(1994)));