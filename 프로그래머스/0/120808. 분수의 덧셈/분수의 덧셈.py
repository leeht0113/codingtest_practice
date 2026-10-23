import math
def solution(numer1, denom1, numer2, denom2):
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2
    
    gcd_value = math.gcd(boonmo, boonja)
    
    answer = [boonja/gcd_value, boonmo/gcd_value]
    
    return answer