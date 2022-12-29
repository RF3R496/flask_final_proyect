def verification(carnet):
    if len(carnet) == 6: 
        if carnet[0] == 'A': 
            if carnet[2] == '5': 
                if carnet[5] == '1' or carnet[5] ==  '3' or  carnet[5] =='9' : 
                    if carnet.find('0') == -1:
                        return True
                    else :
                        return False

    return False



