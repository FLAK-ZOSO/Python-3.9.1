def Tasse(reddito):
    if reddito <= 1250:
        tasse = round(reddito*0.23)
        print(tasse)
    if reddito > 1250:
        tasse = round(1250*0.23)
        reddito_residuo = round(reddito-1250)
        if reddito  <= 2333:
            tasse = round(tasse + reddito_residuo*0.27)
            print(tasse)
        if reddito > 2333:
            tasse = round(tasse + 1083*0.27)
            reddito_residuo = round(reddito_residuo - 1083)
            if reddito  <= 4583:
                tasse = round(tasse + reddito_residuo*0.38)
                print(tasse)
            if reddito > 4583:
                tasse = round(tasse + 2250*0.38)
                reddito_residuo = round(reddito_residuo - 2250)
                if reddito  <= 6250:
                    tasse = round(tasse + reddito_residuo*0.41)
                    print(tasse)
                if reddito > 6250:
                    tasse = round(tasse + 1667*0.41)
                    reddito_residuo = round(reddito_residuo - 1667)
                    tasse = round(reddito_residuo*0.43)
                    print(tasse)
