dageninweek = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')

alledagen = "dagen in de week bestaat uit"
for x in dageninweek:
     alledagen +=" " + x +','
print(alledagen)

werkdagen = "werkdagen in week"
for x in dageninweek[:5]:
    werkdagen +=" " + x +','
print(werkdagen)

weekenddagen = "weekenddagen in week in de week"
for x in dageninweek[-2:]:
    weekenddagen +=" " + x +','
print(weekenddagen)

dagenomgekeerd = "alle dagen omgekeerd is "
for x in dageninweek[::-1]:
    dagenomgekeerd +=" " + x +','
print(dagenomgekeerd) 

werkdagenomgekeerd = "alle weekenddagen omgekeerd zijn"
for x in dageninweek[-3::-1]:
   werkdagenomgekeerd +=" " + x +','
print (werkdagenomgekeerd)

weekendagenomgekeerd = "weekend dagen omgekeerd"
for x in dageninweek[:4:-1]:
    weekendagenomgekeerd +=" " + x +','
print(weekendagenomgekeerd)