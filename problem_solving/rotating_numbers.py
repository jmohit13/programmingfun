
def select_numbers_from_input(il, k, idx, ol):
    """Select numbers from input ilay with user specified spacing k
       
        Input: [1,2,3,4,5,6,7]
        output = [1,4,7,3,6,2,5,1]
    """
    
    if len(ol) == 0:
        ol.append(il[0])
        idx = 0
        return select_numbers_from_input(il, k, idx, ol)
    elif len(ol) < 8:
        idx = idx + k
        if idx >= len(il):
            idx = idx - len(il)
        ian = il[idx]
        ol.append(ian)
        return select_numbers_from_input(il, k, idx, ol)

if __name__ == '__main__':
    
    il = [1,2,3,4,5,6,7]
    k = 3
    idx = 0
    ol = []

    select_numbers_from_input(il, k, idx, ol)
    print(ol)