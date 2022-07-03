import random
import hashlib
s = 40
def EUCLIDES(a, b):
    if b == 0 :
        return a
    else:
      return EUCLIDES(b, a % b)
def EUCLIDES_EXT(a, b):
    if a == 0 :
        return b,0,1
    mcd,x1,y1 = EUCLIDES_EXT(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return mcd,x,y
def modulo(a,b):
    r=a%b
    if r < 0:
        r=r+ b
    return r
def INVERSA(a,b):
    m,a,y=EUCLIDES_EXT(a,b)
    if a<0:
      a=modulo(a,b)
    return a
def EXPMOD(a,x,n):
  c=a%n
  r=1
  while(x>0):
    if x%2!=0:
      r=(r*c)%n
    c=(c*c)%n
    x=x//2
  return r
def ES_COMPUESTO(a, n, t, u):
  xi = EXPMOD(a,u,n)
  if xi == 1 or xi == n-1:
    return False
  for i in range(t):
    xi = EXPMOD(xi,2,n)
    if xi == n-1:
      return False
  return True
def MILLER_RABIN(n,s):
  t=0
  u=n-1
  while (u%2==0):
    u=u/2
    t=t+1
  for j in range(1,s):
    a=random.randint(2,n-1)
    if ES_COMPUESTO(a,n,t,u):
      return False
  return True

def RANDOMBITS(b):
    n=random.randint(0,(2**b)-1)
    m=(2**(b-1))+1
    n=n | m
    return n

def RANDOMGEN_PRIMOS(b):
    n=RANDOMBITS(b)
    while MILLER_RABIN(n,s) is False:
        n=n+2
    return n

#-------------------------RSA----------------------------

def RSA_KEY_GENERATOR(K):
  seguir = True
  while seguir:
    P = RANDOMGEN_PRIMOS(K)
    Q = RANDOMGEN_PRIMOS(K)
    if P != Q:
      seguir = False
  N = P*Q
  fi_P=P-1
  fi_Q=Q-1
  FI= fi_P * fi_Q
  seguir = True
  while seguir:
    E=random.randint(3,N-1)
    if (EUCLIDES(E, FI) == 1):
      seguir=False
  D = INVERSA(E,FI)
  #RESPUESTAS
  print("N es : ", N)
  print("E es : ", E)
  print("D es : ", D)
  return(N,E,D)

def FERMAT(a, x, n):
  if x == 0:
    return 1
  elif x%2 == 0:
    t = FERMAT(a, x/2, n)
    return (t*t)%n
  else:
    t = FERMAT(a, x-1, n)
    c = a%n
    return (t*c)%n


def CIFRADO(M,E,N):
  CIFRADO =EXPMOD(M,E,N)
  return CIFRADO

def DESCIFRADO(C,D,N):
  DESCIFRADO = EXPMOD(C,D,N)
  return DESCIFRADO

#-----------------------------------
(N,E,D)=RSA_KEY_GENERATOR(32)
h=hashlib.sha1()

mensajes=["Hola Mundo","paseme profe","oa"]
M=[]
HASH=[]
FIR=[]
DEC=[]
DIC=[]

#---------------------------------------------





e = 65537
n = 999630013489
for x in range(1,n):
  if EUCLIDES(x,n)==1:
    break


phi_n = 999628013860
c = 747120213790

d = INVERSA(e,phi_n)
Dato_c = (c*FERMAT(x,e,n))%n
Dato_m = DESCIFRADO(Dato_c,d,n)
Dato_x =INVERSA(x,n)
m = (Dato_m*Dato_x)%n
p = CIFRADO(m,e,n)

for mensaje in mensajes:
  h.update(bytes(mensaje,encoding='utf-8'))
  hash_mensaje=h.hexdigest()
  HASH.append(hash_mensaje)
  N=random.randint(1,(n-1))
  M.append(N)
  dic={hash_mensaje,N}
  DIC.append(dic)
  fir=DESCIFRADO(m,n,e)
  FIR.append(fir)

for men in FIR:
  dm=CIFRADO(men,n,d)
  DEC.append(dm)

#------Imprime el Valor-------
print('el valor de m es= ', m )
print("FIRMA =",FIR)
print('el mensaje',mensajes)
print("hash",HASH)
print("M =",M)
print("P(A) =",DEC)