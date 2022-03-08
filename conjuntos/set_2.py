#Removendo elementos do conjunto
#Remove
#Se o elemento não estiver presente o código da erro
nums = set([1,2,2,3,3,3]);
nums.remove(2);
print("Números: ", nums);
print();
#Discard
nums_2 = set([1,2,2,3,3,3]);
nums_2.discard(4);
nums_2.discard(2);
print(nums);
print();
#Remover o set inteiro usamos CLEAR
nums_3 = set([1,2,2,3,3,3]);
print("Números", nums_3);
nums_3.clear();
print("Números: ", nums_3);
