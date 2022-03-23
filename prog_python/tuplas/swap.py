x  = 10;
y = 20;

#Swap tradicional
print("x e y antes do swap: ", x, y);

temp = x;
x = y;
y = temp;

print("x e y depois do swap: ", x, y);

print();
x = 10;
y = 20;

# Swap com tuplas
print("x e y antes do swap: ", x,y);

x, y = y,x;

print("x e y depois do swap: ", x,y);