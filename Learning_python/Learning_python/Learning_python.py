#アンバック代入

data = [1,2,3,4,5]
a,b,c,d,e = data
print(a,b,c,d,e)
print()

#アンバック代入の応用、特定の要素だけを取り出してまとめて代入する
m,n,*o = data
print(m,n,o)
print()

m,*n,o = data
print(m,n,o)
print()

*m,n,o = data
print(m,n,o)
print()

#アンバック代入の応用、一部の要素を切り捨てる
a,_,b,_,c = data
print(a,b,c)
print(_)
print()

a,*_,b = data
print(a,b)
print()

#入れ子リストのアンバック
data = [1,2,[31,32,33]]
a,b,c = data
print(a,b,c)
print()

x,y,(z1,z2,z3) = data
print(x,y,z1,z2,z3)