from fruitmand import fruitmand

del fruitmand[4]

kleuren =[]

for kleur in fruitmand:
    if kleur['color'] not in kleuren:
        kleuren.append(kleur['color'])
    elif kleur in kleuren:
        pass
print(kleuren)
