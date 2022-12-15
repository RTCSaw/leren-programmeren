from fruitmand import fruitmand

for fruit in range(0,len(fruitmand)):
    if fruitmand[fruit].get('name') == 'druif':
        fruitmand.remove(fruitmand[fruit])
        break
print(fruitmand)                #devhelp

kleuren =[]

for kleur in fruitmand:
    if kleur['color'] not in kleuren:
        kleuren.append(kleur['color'])
    
print(kleuren)
