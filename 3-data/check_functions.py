def clean_currency(value: str) -> float :
    '''
    this functions takes a value as ssstr and remove the $ and , and converts to a float value. it returns the float value
    '''
    value = value.replace(',' , '')
    value = value.replace('$', '')
    float_value = float(value)
    return float_value


if __name__ == '__main__': 
    #test clean_currency 
    assert clean_currency('$1,234.56') == 1234.56
    print("All tests pass")

    

def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    '''
    this function takes in the items per person and price per person for a check, along with the 75th percentile values for each. it returns a strong indicating the type of customer.
    '''

    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return ''