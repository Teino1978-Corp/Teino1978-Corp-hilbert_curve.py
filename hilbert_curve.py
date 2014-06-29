import numpy

def obfuscated_hilbert():
    """
    Return NumPy array of shape (512, 3) containing successive coordinates
    for a third-order three-dimensional Hilbert curve.

    """
    a,b,c=numpy.indices((8,)*3).reshape(3,-1)
    d=c[:8];r=abs(d-3>>1);g=(d^d>>1)*73;f=g[abs(d-1)&6]
    x,y=[g[c]>>r[b]^f[b],g[b]]>>r[a]^f[a]
    return(([[x],[y],[g[a]]]>>c[:3,None]&1).T<<c[:3]).sum(2)
