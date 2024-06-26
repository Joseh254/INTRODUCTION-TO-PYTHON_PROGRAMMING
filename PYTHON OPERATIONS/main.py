# PYTHON OPERATIONS
# Operators are used to perform operations on variables and values
#EXAMPLE
a=5
print(a+3)

"""


Operator	Name	            Example

+	        Addition	        x + y	
-	        Subtraction	        x - y	
*	        Multiplication	    x * y	
/	        Division	        x / y	
%	        Modulus	            x % y	
**	        Exponentiation	    x ** y	
//	        Floor division	    x // y

"""


# Python Assignment Operators

"""
Operator	Example	        Same As	
=	        x = 5	        x = 5	
+=	        x += 3	        x = x + 3
-=	        x -= 3	        x = x - 3	
*=	        x *= 3	        x = x * 3	
/=	        x /= 3	        x = x / 3	
%=	        x %= 3	        x = x % 3	
//=	        x //= 3	        x = x // 3	
**=	        x **= 3	        x = x ** 3	
&=	        x &= 3	        x = x & 3	
|=	        x |= 3	        x = x | 3	
^=	        x ^= 3	        x = x ^ 3	
>>=	        x >>= 3	        x = x >> 3	
<<=	        x <<= 3	        x = x << 3	


"""


# Python Comparison Operators

"""

Operator	Name	                    Example

==	        Equal	                    x == y	
!=	        Not equal	                != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y


"""


# Python Logical Operators

"""


Operator	Description	                                                Example	
and         Returns True if both statements are true	                x < 5 and  x < 10	
or	        Returns True if one of the statements is true	            x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true     

"""

# Python Identity Operators

"""
Operator	    Description	Example	

is 	            Returns True if both variables are the same object	x is y	
is not	        Returns True if both variables are not the same object

"""


# Python Bitwise Operators

""""


Operator	Name	Description	                                            Example	

& 	        AND	     Sets each bit to 1 if both bits are 1	                x & y	
|	        OR	     Sets each bit to 1 if one of two bits is 1             x | y	
^	        XOR	     Sets each bit to 1 if only one of two bits is 1	    x ^ y	
~	        NOT	     inverts all the bits	                                ~x

"""

# Operator Precedence

# Operator precedence describes the order in which operations are to be performed.they follow some mathematical rules

# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((5 + 1) - (4 + 3)) #operations inside the brackets are performed first

# Multiplication * has higher precedence than addition
print(15 + 5 * 3)


"""
Operator	                        Description	Try it
()	                                Parentheses	
**	                                Exponentiation	
+x  -x  ~x	                        Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                        Multiplication, division, floor division, and modulus	
+  -	                            Addition and subtraction	
<<  >>	                            Bitwise left and right shifts	
&	                                Bitwise AND	
^	                                Bitwise XOR	
|	                                Bitwise OR	
==  !=  >  >=  <  <=                is  is not  in  not in 	Comparisons, identity, and membership operators	
not	                                Logical NOT	
and	                                AND	
or	                                OR


"""