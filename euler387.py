def is_prime(x):
	if x <= 1:
		return False
	elif x<= 3:
		return True
	elif  x%2== 0 or x%3 == 0:
		return False
	i = 5
	while i*i <= x:
		if x%i == 0 or x%(i+2) == 0:
			return False
		i += 6
	return True


def sum_digits(num):
	sum = 0 
	while num > 0:
		sum += num%10
		num = num/10
	return sum

def isHarshad(num):
	return num%sum_digits(num) == 0 
	
def isTruncHarshad(num):
	while num > 0:
		if not isHarshad(num):
			return False
		num = num/10
	return True

def isStrongHarshad(num):
	return isHarshad(num) and is_prime(num/sum_digits(num))
	
	
def isStrongRTHarshad(num):
	if num < 10:
		return False
	return is_prime(num) and isStrongHarshad(num/10) and isTruncHarshad(num/10)
	
def primes235(limit):
    yield 2; yield 3; yield 5
    if limit < 7: return
    modPrms = [7,11,13,17,19,23,29,31]
    gaps = [4,2,4,2,4,6,2,6,4,2,4,2,4,6,2,6] # 2 loops for overflow
    ndxs = [0,0,0,0,1,1,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,7]
    lmtbf = (limit + 23) // 30 * 8 - 1 # integral number of wheels rounded up
    lmtsqrt = (int(limit ** 0.5) - 7)
    lmtsqrt = lmtsqrt // 30 * 8 + ndxs[lmtsqrt % 30] # round down on the wheel
    buf = [True] * (lmtbf + 1)
    for i in xrange(lmtsqrt + 1):
        if buf[i]:
            ci = i & 7; p = 30 * (i >> 3) + modPrms[ci]
            s = p * p - 7; p8 = p << 3
            for j in range(8):
                c = s // 30 * 8 + ndxs[s % 30]
                buf[c::p8] = [False] * ((lmtbf - c) // p8 + 1)
                s += p * gaps[ci]; ci += 1
    for i in xrange(lmtbf - 6 + (ndxs[(limit - 7) % 30])): # adjust for extras
        if buf[i]: yield (30 * (i >> 3) + modPrms[i & 7])
        
    
def isStrongRTHarshad2(num):
	if num < 10:
		return False
	return isStrongHarshad(num/10) and isTruncHarshad(num/10)    
    
def sum(limit):
	sum = 0
	primes = primes235(limit)
	for i in primes:
		if isStrongRTHarshad2(i):
			sum += i
	return sum
    
 
 def primes2():
    whlPrms = [2,3,5,7,11,13,17]                # base wheel primes
    for p in whlPrms: yield p
    def makeGaps():
        buf = [True] * (3 * 5 * 7 * 11 * 13 * 17 + 1) # all odds plus extra for o/f
        for p in whlPrms:
            if p < 3:
                continue              # no need to handle evens
            strt = (p * p - 19) >> 1            # start position (divided by 2 using shift)
            while strt < 0: strt += p
            buf[strt::p] = [False] * ((len(buf) - strt - 1) // p + 1) # cull for p
        whlPsns = [i + i for i,v in enumerate(buf) if v]
        return [whlPsns[i + 1] - whlPsns[i] for i in range(len(whlPsns) - 1)]
    gaps = makeGaps()                           # big wheel gaps
    def wheel_prime_pairs():
        yield (19,0); bps = wheel_prime_pairs() # additional primes supply
        p, pi = next(bps); q = p * p            # adv to get 11 sqr'd is 121 as next square to put
        sieve = {}; n = 23; ni = 1              #   into sieve dict; init cndidate, wheel ndx
        while True:
            if n not in sieve:                  # is not a multiple of previously recorded primes
                if n < q: yield (n, ni)         # n is prime with wheel modulo index
                else:
                    npi = pi + 1                # advance wheel index
                    if npi > 92159: npi = 0
                    sieve[q + p * gaps[pi]] = (p, npi) # n == p * p: put next cull position on wheel
                    p, pi = next(bps); q = p * p  # advance next prime and prime square to put
            else:
                s, si = sieve.pop(n)
                nxt = n + s * gaps[si]          # move current cull position up the wheel
                si = si + 1                     # advance wheel index
                if si > 92159: si = 0
                while nxt in sieve:             # ensure each entry is unique by wheel
                    nxt += s * gaps[si]
                    si = si + 1                 # advance wheel index
                    if si > 92159: si = 0
                sieve[nxt] = (s, si)            # next non-marked multiple of a prime
            nni = ni + 1                        # advance wheel index
            if nni > 92159: nni = 0
            n += gaps[ni]; ni = nni             # advance on the wheel
    for p, pi in wheel_prime_pairs(): yield p   # strip out indexes
    