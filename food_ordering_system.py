factor=[]
while True:
 m_k=int(input('1.kobide 2.salad 3.noshbe 4.peykmotori 5.sefarsh telefoni?---->'))
 if m_k==1:
    k_n=int(input('1.negini 2.negini chili 3.negini spicy?---->'))
    if k_n==1:
        B=int(input('chand ta---?'))
        C=float(input('gheymat chand---?'))
        D=B*C
        print(D) 
        factor.append(f'negini--->{D}')
    elif k_n==2:
       B=int(input('chand ta---?'))
       C=float(input('gheymat chand---?'))
       D=B*C
       print(D) 
       factor.append(f'negini chili--->{D}')
    elif k_n==3:
       B=int(input('chand ta---?'))
       C=float(input('gheymat chand---?'))
       D=B*C
       print(D) 
       factor.append(f'negini spicy--->{D}')
 elif m_k==2:
    m_s=int(input('1.shirazi 2.fasl ?---->'))
    if m_s==1:
     B=int(input('chand ta---?'))
     C=float(input('gheymat chand---?'))
     D=B*C
     print(D)
     factor.append(f'shirazi--->{D}') 
    elif m_s==2:
     B=int(input('chand ta---?'))
     C=float(input('gheymat chand---?'))
     D=B*C
     print(D) 
     factor.append(f'fasl--->{D}')
 elif m_k==3:
    m_no=int(input('1.fanta 2.cola 3.miranda?---->')) 
    if m_no==1:
     B=int(input('chand ta---?'))
     C=float(input('gheymat chand---?'))
     D=B*C
     print(D)
     factor.append(f'fanta--->{D}') 
    elif m_no==2:
     B=int(input('chand ta---?'))
     C=float(input('gheymat chand---?'))
     D=B*C
     print(D)
     factor.append(f'cola--->{D}') 
    elif m_no==3:
     B=int(input('chand ta---?'))
     C=float(input('gheymat chand---?'))
     D=B*C
     print(D)
     factor.append(f'miranda--->{D}') 
 elif m_k==4:
    esm_peyke=input('esm peyke?--->')
    shomare_peyke=input('shomare peyke?--->')
    esm_moshtari=input('esm moshtari?--->')
    shomare_moshtari=input('shomare moshtari?--->')
    shomare_eshterak=input('shomare eshterak?--->')
    esm_restoran=input('esm restorean?--->')
    adres_restoran=input('adres restoran?--->')
    shomare_restoran=input('shomare restoran?--->')
    adres_moshtari=input('adres moshtari?--->')
    shomare_ghabz=input('shomare ghabz?--->')
    saat_tahvil=input('saat tahvil gereftan ghaza az restoran?--->')
    esm_sefaresh=input('esm sefaresh?--->')
    tedad=int(input('tedad sefaresh?--->'))
    gheymat=float(input('gheymat sefaresh?--->'))
    gheymatkol=tedad*gheymat
    print(f'esm peyke:{esm_peyke} shomare peyke:{shomare_peyke} esm moshtari:{esm_moshtari} shomare moshtari:{shomare_moshtari} shomare eshterak:{shomare_eshterak} esm retoran:{esm_restoran} adres restoran:{adres_restoran} shomare restoran:{shomare_restoran} adres moshtari:{adres_moshtari} shomare ghabz:{shomare_ghabz} saat tahvil gereftan ghaza az restoran:{saat_tahvil} esm sefaresh:{esm_sefaresh}')
    print(f'tedad sefaresh:{tedad} gheymat sefaresh:{gheymat}')
    print(f'gheymatkol:{gheymatkol} komision peyke:{gheymatkol*0.05}')
 elif m_k==5:
    print('shomare restoran:02631766449') 
 X=input('braye khoroj dokme E ra feshar dahid --->')
 if X=='E':
   print('kharej shodid⛔')
   print(factor)
   break
