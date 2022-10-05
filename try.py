
kijken_uit_raam = 0
while kijken_uit_raam >= 0:
            vraag_kijken = input("Wilt u naar buiten kijken?")
            if vraag_kijken == "ja":
                kijken_uit_raam = +10
            
            if vraag_kijken == "nee":
                kijken_uit_raam = -10
            
            if kijken_uit_raam >5:
                    print ("""
                                .              +   .             .   . .     .  .
                                        .                    .       .     *
                        .       *    . . . .  .   .  + .     .    .        .  .
                                    .      .   .  +  . . .  .    .   .
                        .                   .  .   .    .    . .       .      .
                                        .     .     . +.    +  .
                                *         .              .       .   . .
                                . .                  .    * . . .  .  +   .
                                +      .           .   .      +        . 
                                                    .       . +  .+. .
                        .                      .     . + .  . .     .      .
                                .      .    .     . .       .   .    .       
                            *    .    . .  +    .  .       .  .   .    - O -
                                .     .                        .     .      *
                        .      .   . .   .   .   . .  +   .    .            +

                        """)
                    break
            elif kijken_uit_raam <0:
                    print("Ook goed, we gaan door")
                    break

            else:
                    print("Foute input, probeer het opnieuw")

