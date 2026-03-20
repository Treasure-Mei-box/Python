#encoding - character to numbers , a -> 97
#decoding - numbers to charater , 65 -> A

#ASCII code = 265 characters -> a,b,b,c, A,B,C # 2 1 + - = ?
#unicode = 65535  characters -> including myanmar words and any other language

#ASCII ENCODING process in PYTHON using (ord) method 
mychar = ord('A')
print(mychar)

mychar1 = ord('a')
print(mychar1)

mychar2 = ord('y')
print(mychar2)

mychar3 = ord('Y')
print(mychar3)

#ASCII DECODING process in PYTHON using (chr) method 

revchar = chr(65)
print(revchar)

revchar1 = chr(97)
print(revchar1)

revchar2 = chr(121)
print(revchar2)

revchar3 = chr(240)
print(revchar3)