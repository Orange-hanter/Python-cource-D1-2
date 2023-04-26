## MRO Algorithm in Python:

However, in Python, this confusion of method calling in hybrid inheritance scenarios (A combination of multiple, hierarchal, multilevel inheritances) is cleared through **DFLR (Depth First then Left to Right) concept.**

![No alt text provided for this image](https://media.licdn.com/dms/image/C5612AQGgfL1py0ROVw/article-inline_image-shrink_1000_1488/0/1601410527646?e=1684972800&v=beta&t=793iVJY_-tbn_hqOJXz3N8fgCy2ynURdzOD1z1C7rpo)

In Python, every class is considered to be a child class of the object class. This object class is basically a hidden class.

In reference to following hybrid inheritance representation,

1.  When a method is called using an object of Class A, then  PVM will first check in class A. If the method doesn't exist in Class A then the PVM will check in the object class and would throw 'no attribute found' compiler error. Therefore, mro(A) = A, Obj
2.  If a method is called using an object of Class B, then  PVM will first check in Class B. If the method doesn't exist in Class B then as per **Depth First** concept the PVM will check in Class A. If the method doesn't exist in Class A then the PVM will check in the object class. Therefore, mro(B) = B, A, Obj
3.  Similarly mro(C) = C, A, Obj
4.  If a method is called using an object of Class D, then PVM will first check in Class D. If the method doesn't exist in Class D then as per **Depth First then Left to Right concept** the PVM will check in Class B. If not found in Class B, then PVM will check in Class C. If not found in Class C, then PVM will check in Class A. If not found in Class A then the PVM will check in the object class. Therefore, mro(D) = D,B,C,A,Obj.

## **C3 Algorithm.**

For hybrid inheritance up to two levels, the MRO algorithm works perfectly well. However, for more than two levels, an advanced MRO algorithm known as the C3 algorithm is used.

> mro(X) = X + Merge [mro(P1) + mro(P2) + mro(P3)…...+ Parent List]

> where P1, P2, P3 are direct parent of X

**_Head Element and Tail Element_**_: If for example, an element is ‘XYZA’, then 1st Element ‘X’ would be considered as the head element and the remaining elements ‘YZA’ would be considered as the tail element._

**_Rule 1_**_: If the head not present in the tail part of any other element in the merge list, then add this head to the result and remove it from the element in the merge list._

**_Rule 2_**_: If the head is present in the tail part of any other element in the merge list, then consider the head element of the next element in the list and continue the process defined as per Rule 1._

For the following diagram, with the help of C3 algorithm logic, we would try to find the method resolution order when the method is called using an object of class P :

![No alt text provided for this image](https://media.licdn.com/dms/image/C4E12AQHYEy1-45cVZw/article-inline_image-shrink_1000_1488/0/1601412795946?e=1684972800&v=beta&t=TRT5wXFqvWbr8u02-uruWWYyfqgyks6kzwWSp8ZPlmY)

### 1.   mro(P) = P + Merge [mro(X), mro(Y), mro(C), XYC]

Now, we need to replace the value of mro(X), mro(Y), mro(C) as described earlier using the DFLR concept.

### **2.   mro(P) = P + Merge [XABO, YBCO, CO, XYC]**

On considering the first element ‘XABO’, as per Rule 1, as X is the head element and not present in the tail part of any other elements in the list, therefore X is added to the result & removed from the other elements in the list.

### 3.   mro(P) = P + X + Merge [ ABO, YBCO, CO, YC]

Now, on considering the updated first element ‘ABO’, as per Rule 1, as A is the head element and not present in the tail part of any other elements in the list, therefore A is added to the result & removed from the other elements in the list.

### 4.   mro(P) = P + X + A + Merge [ BO, YBCO, CO, YC]

Beware !! Here comes the tricky part. Now, on considering the updated first element ‘BO’, B is the head element but it is present in the tail element of ‘YBCO’. Therefore, as per Rule 2, the second element i.e ‘YBCO’ will be considered. Here Y is the head element and not present in the tail part of other elements in the list, therefore Y is added to the result & removed from the other elements in the list.

### 5.   mro(P) = P + X + A + Y + Merge [ BO, BCO, CO, C]

Now, again the first element of the updated merge list i.e ‘BO’ will be considered. Here B is the head element and not present in the tail part of other elements in the list, therefore B is added to the result & removed from the other elements in the list.

### 6.   mro(P) = P + X + A + Y + B + Merge [ O, CO, CO, C]

Now, as an element ‘O’ is present in the tail element of element ‘CO’ therefore as per Rule 2, the second element ‘CO’ will be considered. Here C is the head element and not present in the tail part of other elements in the list, therefore C is added to the result & removed from the other elements in the list.

### 7.   mro(P) = P + X + A + Y + B + C + Merge [ O, O, O]

Now as O is the only element left, as per Rule 1, O will be added to the result & removed from the other elements in the list.

### Therefore, the final answer would be mro(P) = P,X,A,Y,B,C,Obj

P.S: I have purposely refrained from using coding syntax so as eliminate confusion and achieve an easy understanding of the internal functionality of the MRO Algorithm performed by PVM.

Reference: Method Resolution Order (MRO) Algorithm by Durga Sir. [Youtube Video Link https://youtu.be/w0GlHaBP364]