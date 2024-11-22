def main():
    pais1 = int(input("Digite a populção do pais A:").strip())
    pais2 = int(input("Digite a populção do pais b:").strip())

    if pais1 > pais2:
        paisB = pais2
        paisA = pais1
    else:
        paisB = pais1
        paisA = pais2
    
    ano = 0

    while True:
        if paisB <= 0 or paisA <= 0: break
        if paisB > paisA: break
        ano += 1
        paisA += paisA * (2/100)
        paisB += paisB * (3/100)
    
    print(f"o país B ultrapassara a população do país A em:{ano}anos.")

if __name__ == '__main__':
    main()