

def func(n):
    '''
    1^2+2^2+3^2....+n^2=(n(n+1)(2n+1))/6
    (1+2+3+4..+n)^2=(n(n+2)/2)^2

    func(n)=(n(n+2)/2)^2-(n(n+1)(2n+1))/6

    func(n)=>(3n^4+2n^3-3n^2-2n)/12
    '''
    return int((3*n*n*n*n+2*n*n*n-3*n*n-2*n)/12)

print(func(100)) # answer is func(100) (25164150) :)
