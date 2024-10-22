vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

def total_anual (vendas_anuais):
    soma = sum(vendas_anuais)
    print (f"O valor vendido foi: {soma}")
total_anual(vendas_mensais)

def media_mensal(Media_M):
    media = sum(Media_M) / len(Media_M) 
    print(f"A media mensal foi: {media}")
    
media_mensal(vendas_mensais)

def maxima_mensal (max_m):
    maxima = max(max_m)
    print(f"A maxima mensal foi: {maxima}")

maxima_mensal(vendas_mensais)
