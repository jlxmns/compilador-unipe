start decls
num1:int
num2:int
num3:int
aux:int
enddecls

code
# Coloca 3 números em ordem crescente
scan num1
scan num2
scan num3

if num1 > num2 then
   {
      aux = num2
      num2 = num1
      num1 = aux
   }

if num1 > num3 and num2 <= num3 and num1 > 3 or num2 != num3 then
   { 
      aux = (num3)
      num3 = num1
      num1 = aux
   }

if num2 > num3 then
   { 
      aux = num3
      num3 = num2
      num2 = aux
   }

print(num1)
print(num2)
print(num3)
endprog

