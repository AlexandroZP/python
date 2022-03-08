
def binario(n):
    nBinario = '';
    while n > 0:
        nBinario += str (n % 2);
        n = n // 2;
   
    return nBinario;

print(binario(10)[::-1]);

        
