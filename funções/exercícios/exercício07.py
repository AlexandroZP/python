def notas(nota):
    if nota >= 90:
        return "A";
    elif nota >= 80:
        return "B";
    elif nota >= 70:
        return "C";
    elif nota >= 60:
        return "D";
    elif nota >= 50:
        return "E";
    else:
        return "F";
print(notas(75));