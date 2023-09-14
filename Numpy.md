```python
#Md.Ibrahim
#ID: 201-35-640
#Section: A2

import numpy as np
```

#Md.Ibrahim
#ID: 201-35-640
#Section: A2

import numpy as np


```python
array=np.array([0,1,2,3,4,5,6,7,8,9])
print(array)
```

    [0 1 2 3 4 5 6 7 8 9]
    


```python
#3*3 array all element true
```


```python
array=np.ones((3,3), dtype='bool')
print(array)
```

    [[ True  True  True]
     [ True  True  True]
     [ True  True  True]]
    


```python
#odd number print
```


```python
array=np.array([0,1,2,3,4,5,6,7,8,9])
odd_number=array[array%2!=0]
print(odd_number)
```

    [1 3 5 7 9]
    


```python
#5.	Replace all odd numbers in arr with -1
```


```python
array[array%2!=0]=-1
print(array)
```

    [ 0 -1  2 -1  4 -1  6 -1  8 -1]
    


```python
new_array = np.where(array % 2 != 0, -1, array)

print(new_array)
```

    [ 0 -1  2 -1  4 -1  6 -1  8 -1]
    


```python
#7.	Convert a 1D array to a 2D array with 2 rows.
```


```python
array_1D=np.array([0,1,2,3,4,5,6,7,8,9])
array_2D=array_1D.reshape(2,-1)
print(array_2D)
```

    [[0 1 2 3 4]
     [5 6 7 8 9]]
    


```python
#Stack arrays a and b vertically.
```


```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

stacked = np.vstack((a, b))

print(stacked)
```

    [[1 2 3]
     [4 5 6]]
    


```python
#9.	Stack the arrays a and b horizontally
```


```python
a = np.array([1, 2, 4])
b = np.array([4, 5, 7])

stacked = np.hstack((a, b))

print(stacked)
```

    [1 2 4 4 5 7]
    


```python
#10.	Create the following pattern without hardcoding. Use only numpy functions and the below input array a. (np.repeat, np.tile)


```


```python
a = np.array([1,2,3,4,5,6])
np.repeat(a,2,axis=None)

```




    array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])




```python
a = np.array([1,2,3,4,5,6])
np.tile(a,5)
```




    array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4,
           5, 6, 1, 2, 3, 4, 5, 6])




```python
#Get the common items between a and b.
```


```python
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

common_items = np.intersect1d(a, b)

print(common_items)
```

    [2 4]
    


```python
#12.	From array a remove all items present in array b.
```


```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

result = np.setdiff1d(a, b)

print(result)

```

    [1 2 3 4]
    


```python
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

matching_positions = np.where(a == b)[0]

print(matching_positions)
```

    [1 3 5 7]
    


```python
#14.	Get all items between 5 and 10 from a.
```


```python
a = np.array([2, 6, 1, 9, 10, 3, 27])

result = a[(a > 5) & (a < 10)]

print(result)
```

    [6 9]
    


```python
#Swap columns 1 and 2 in the array arr.
```


```python
array = np.arange(9).reshape(3, 3)

print("Original Array:")

print(array)

array[:, [1, 2]] = array[:, [2, 1]]

print("Array after swapping columns 1 and 2:")
print(array)
```

    Original Array:
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    Array after swapping columns 1 and 2:
    [[0 2 1]
     [3 5 4]
     [6 8 7]]
    


```python
array = np.arange(12).reshape(3, 4)
```


```python
print(array)
```

    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    


```python
#16.	Swap rows 1 and 2 in the array arr.
```


```python
arr = np.arange(9).reshape(3, 3)
print("Original Array:")
print(arr)

arr[[1, 2], :] = arr[[2, 1], :]

print("Array after swapping rows 1 and 2:")
print(arr)
```

    Original Array:
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    Array after swapping rows 1 and 2:
    [[0 1 2]
     [6 7 8]
     [3 4 5]]
    


```python
#17.	Reverse the rows of a 2D array arr.
```


```python
arr = np.arange(9).reshape(3, 3)
print("Original Array:")
print(arr)

reversed_arr = arr[::-1]

print("Array with reversed rows:")
print(reversed_arr)
```

    Original Array:
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    Array with reversed rows:
    [[6 7 8]
     [3 4 5]
     [0 1 2]]
    


```python
#18.	Reverse the columns of a 2D array arr.
```


```python
arr = np.arange(9).reshape(3, 3)
print("Original Array:")
print(arr)

reversed_arr = arr[:, ::-1]

print("Array with reversed columns:")
print(reversed_arr)
```

    Original Array:
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    Array with reversed columns:
    [[2 1 0]
     [5 4 3]
     [8 7 6]]
    


```python
#19.	Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10
```


```python
lower_bound = 5
upper_bound = 10
shape = (5, 3)

random_array = np.random.uniform(lower_bound, upper_bound, size=shape)

print(random_array)
```

    [[9.665 8.521 9.809]
     [9.146 7.453 9.611]
     [9.484 6.649 8.05 ]
     [5.845 6.158 9.096]
     [9.322 9.732 8.21 ]]
    


```python
#20.	Print or show only 3 decimal places of the numpy array rand_arr.



```


```python
rand_arr = np.random.random((5, 3))

np.set_printoptions(precision=3)

print(rand_arr)
```

    [[0.87  0.818 0.979]
     [0.255 0.075 0.854]
     [0.839 0.357 0.494]
     [0.987 0.202 0.613]
     [0.451 0.468 0.535]]
    


```python
#21.	Pretty print rand_arr by suppressing the scientific notation (like 1e10).
```


```python
rand_arr = np.random.random((5, 3))

np.set_printoptions(suppress=True)

print(rand_arr)
```

    [[0.354 0.89  0.638]
     [0.974 0.589 0.124]
     [0.313 0.071 0.364]
     [0.6   0.672 0.004]
     [0.503 0.028 0.564]]
    


```python
#22.	Limit the number of items printed in python numpy array a to a maximum of 6 elements
```


```python
a = np.arange(10)

np.set_printoptions(threshold=6)

print(a)
```

    [0 1 2 ... 7 8 9]
    


```python
#23.	Print the full numpy array a without truncating.


```


```python
a = np.arange(15)

# Reset the threshold to its default value
np.set_printoptions(threshold=np.inf)

print(a)
```

    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
    


```python
url = './Iris.csv'
iris = np.genfromtxt(url, delimiter=',', dtype='str', encoding=None)

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

print(iris)
```

    [['Id' 'SepalLengthCm' 'SepalWidthCm' 'PetalLengthCm' 'PetalWidthCm'
      'Species']
     ['1' '5.1' '3.5' '1.4' '0.2' 'Iris-setosa']
     ['2' '4.9' '3.0' '1.4' '0.2' 'Iris-setosa']
     ['3' '4.7' '3.2' '1.3' '0.2' 'Iris-setosa']
     ['4' '4.6' '3.1' '1.5' '0.2' 'Iris-setosa']
     ['5' '5.0' '3.6' '1.4' '0.2' 'Iris-setosa']
     ['6' '5.4' '3.9' '1.7' '0.4' 'Iris-setosa']
     ['7' '4.6' '3.4' '1.4' '0.3' 'Iris-setosa']
     ['8' '5.0' '3.4' '1.5' '0.2' 'Iris-setosa']
     ['9' '4.4' '2.9' '1.4' '0.2' 'Iris-setosa']
     ['10' '4.9' '3.1' '1.5' '0.1' 'Iris-setosa']
     ['11' '5.4' '3.7' '1.5' '0.2' 'Iris-setosa']
     ['12' '4.8' '3.4' '1.6' '0.2' 'Iris-setosa']
     ['13' '4.8' '3.0' '1.4' '0.1' 'Iris-setosa']
     ['14' '4.3' '3.0' '1.1' '0.1' 'Iris-setosa']
     ['15' '5.8' '4.0' '1.2' '0.2' 'Iris-setosa']
     ['16' '5.7' '4.4' '1.5' '0.4' 'Iris-setosa']
     ['17' '5.4' '3.9' '1.3' '0.4' 'Iris-setosa']
     ['18' '5.1' '3.5' '1.4' '0.3' 'Iris-setosa']
     ['19' '5.7' '3.8' '1.7' '0.3' 'Iris-setosa']
     ['20' '5.1' '3.8' '1.5' '0.3' 'Iris-setosa']
     ['21' '5.4' '3.4' '1.7' '0.2' 'Iris-setosa']
     ['22' '5.1' '3.7' '1.5' '0.4' 'Iris-setosa']
     ['23' '4.6' '3.6' '1.0' '0.2' 'Iris-setosa']
     ['24' '5.1' '3.3' '1.7' '0.5' 'Iris-setosa']
     ['25' '4.8' '3.4' '1.9' '0.2' 'Iris-setosa']
     ['26' '5.0' '3.0' '1.6' '0.2' 'Iris-setosa']
     ['27' '5.0' '3.4' '1.6' '0.4' 'Iris-setosa']
     ['28' '5.2' '3.5' '1.5' '0.2' 'Iris-setosa']
     ['29' '5.2' '3.4' '1.4' '0.2' 'Iris-setosa']
     ['30' '4.7' '3.2' '1.6' '0.2' 'Iris-setosa']
     ['31' '4.8' '3.1' '1.6' '0.2' 'Iris-setosa']
     ['32' '5.4' '3.4' '1.5' '0.4' 'Iris-setosa']
     ['33' '5.2' '4.1' '1.5' '0.1' 'Iris-setosa']
     ['34' '5.5' '4.2' '1.4' '0.2' 'Iris-setosa']
     ['35' '4.9' '3.1' '1.5' '0.1' 'Iris-setosa']
     ['36' '5.0' '3.2' '1.2' '0.2' 'Iris-setosa']
     ['37' '5.5' '3.5' '1.3' '0.2' 'Iris-setosa']
     ['38' '4.9' '3.1' '1.5' '0.1' 'Iris-setosa']
     ['39' '4.4' '3.0' '1.3' '0.2' 'Iris-setosa']
     ['40' '5.1' '3.4' '1.5' '0.2' 'Iris-setosa']
     ['41' '5.0' '3.5' '1.3' '0.3' 'Iris-setosa']
     ['42' '4.5' '2.3' '1.3' '0.3' 'Iris-setosa']
     ['43' '4.4' '3.2' '1.3' '0.2' 'Iris-setosa']
     ['44' '5.0' '3.5' '1.6' '0.6' 'Iris-setosa']
     ['45' '5.1' '3.8' '1.9' '0.4' 'Iris-setosa']
     ['46' '4.8' '3.0' '1.4' '0.3' 'Iris-setosa']
     ['47' '5.1' '3.8' '1.6' '0.2' 'Iris-setosa']
     ['48' '4.6' '3.2' '1.4' '0.2' 'Iris-setosa']
     ['49' '5.3' '3.7' '1.5' '0.2' 'Iris-setosa']
     ['50' '5.0' '3.3' '1.4' '0.2' 'Iris-setosa']
     ['51' '7.0' '3.2' '4.7' '1.4' 'Iris-versicolor']
     ['52' '6.4' '3.2' '4.5' '1.5' 'Iris-versicolor']
     ['53' '6.9' '3.1' '4.9' '1.5' 'Iris-versicolor']
     ['54' '5.5' '2.3' '4.0' '1.3' 'Iris-versicolor']
     ['55' '6.5' '2.8' '4.6' '1.5' 'Iris-versicolor']
     ['56' '5.7' '2.8' '4.5' '1.3' 'Iris-versicolor']
     ['57' '6.3' '3.3' '4.7' '1.6' 'Iris-versicolor']
     ['58' '4.9' '2.4' '3.3' '1.0' 'Iris-versicolor']
     ['59' '6.6' '2.9' '4.6' '1.3' 'Iris-versicolor']
     ['60' '5.2' '2.7' '3.9' '1.4' 'Iris-versicolor']
     ['61' '5.0' '2.0' '3.5' '1.0' 'Iris-versicolor']
     ['62' '5.9' '3.0' '4.2' '1.5' 'Iris-versicolor']
     ['63' '6.0' '2.2' '4.0' '1.0' 'Iris-versicolor']
     ['64' '6.1' '2.9' '4.7' '1.4' 'Iris-versicolor']
     ['65' '5.6' '2.9' '3.6' '1.3' 'Iris-versicolor']
     ['66' '6.7' '3.1' '4.4' '1.4' 'Iris-versicolor']
     ['67' '5.6' '3.0' '4.5' '1.5' 'Iris-versicolor']
     ['68' '5.8' '2.7' '4.1' '1.0' 'Iris-versicolor']
     ['69' '6.2' '2.2' '4.5' '1.5' 'Iris-versicolor']
     ['70' '5.6' '2.5' '3.9' '1.1' 'Iris-versicolor']
     ['71' '5.9' '3.2' '4.8' '1.8' 'Iris-versicolor']
     ['72' '6.1' '2.8' '4.0' '1.3' 'Iris-versicolor']
     ['73' '6.3' '2.5' '4.9' '1.5' 'Iris-versicolor']
     ['74' '6.1' '2.8' '4.7' '1.2' 'Iris-versicolor']
     ['75' '6.4' '2.9' '4.3' '1.3' 'Iris-versicolor']
     ['76' '6.6' '3.0' '4.4' '1.4' 'Iris-versicolor']
     ['77' '6.8' '2.8' '4.8' '1.4' 'Iris-versicolor']
     ['78' '6.7' '3.0' '5.0' '1.7' 'Iris-versicolor']
     ['79' '6.0' '2.9' '4.5' '1.5' 'Iris-versicolor']
     ['80' '5.7' '2.6' '3.5' '1.0' 'Iris-versicolor']
     ['81' '5.5' '2.4' '3.8' '1.1' 'Iris-versicolor']
     ['82' '5.5' '2.4' '3.7' '1.0' 'Iris-versicolor']
     ['83' '5.8' '2.7' '3.9' '1.2' 'Iris-versicolor']
     ['84' '6.0' '2.7' '5.1' '1.6' 'Iris-versicolor']
     ['85' '5.4' '3.0' '4.5' '1.5' 'Iris-versicolor']
     ['86' '6.0' '3.4' '4.5' '1.6' 'Iris-versicolor']
     ['87' '6.7' '3.1' '4.7' '1.5' 'Iris-versicolor']
     ['88' '6.3' '2.3' '4.4' '1.3' 'Iris-versicolor']
     ['89' '5.6' '3.0' '4.1' '1.3' 'Iris-versicolor']
     ['90' '5.5' '2.5' '4.0' '1.3' 'Iris-versicolor']
     ['91' '5.5' '2.6' '4.4' '1.2' 'Iris-versicolor']
     ['92' '6.1' '3.0' '4.6' '1.4' 'Iris-versicolor']
     ['93' '5.8' '2.6' '4.0' '1.2' 'Iris-versicolor']
     ['94' '5.0' '2.3' '3.3' '1.0' 'Iris-versicolor']
     ['95' '5.6' '2.7' '4.2' '1.3' 'Iris-versicolor']
     ['96' '5.7' '3.0' '4.2' '1.2' 'Iris-versicolor']
     ['97' '5.7' '2.9' '4.2' '1.3' 'Iris-versicolor']
     ['98' '6.2' '2.9' '4.3' '1.3' 'Iris-versicolor']
     ['99' '5.1' '2.5' '3.0' '1.1' 'Iris-versicolor']
     ['100' '5.7' '2.8' '4.1' '1.3' 'Iris-versicolor']
     ['101' '6.3' '3.3' '6.0' '2.5' 'Iris-virginica']
     ['102' '5.8' '2.7' '5.1' '1.9' 'Iris-virginica']
     ['103' '7.1' '3.0' '5.9' '2.1' 'Iris-virginica']
     ['104' '6.3' '2.9' '5.6' '1.8' 'Iris-virginica']
     ['105' '6.5' '3.0' '5.8' '2.2' 'Iris-virginica']
     ['106' '7.6' '3.0' '6.6' '2.1' 'Iris-virginica']
     ['107' '4.9' '2.5' '4.5' '1.7' 'Iris-virginica']
     ['108' '7.3' '2.9' '6.3' '1.8' 'Iris-virginica']
     ['109' '6.7' '2.5' '5.8' '1.8' 'Iris-virginica']
     ['110' '7.2' '3.6' '6.1' '2.5' 'Iris-virginica']
     ['111' '6.5' '3.2' '5.1' '2.0' 'Iris-virginica']
     ['112' '6.4' '2.7' '5.3' '1.9' 'Iris-virginica']
     ['113' '6.8' '3.0' '5.5' '2.1' 'Iris-virginica']
     ['114' '5.7' '2.5' '5.0' '2.0' 'Iris-virginica']
     ['115' '5.8' '2.8' '5.1' '2.4' 'Iris-virginica']
     ['116' '6.4' '3.2' '5.3' '2.3' 'Iris-virginica']
     ['117' '6.5' '3.0' '5.5' '1.8' 'Iris-virginica']
     ['118' '7.7' '3.8' '6.7' '2.2' 'Iris-virginica']
     ['119' '7.7' '2.6' '6.9' '2.3' 'Iris-virginica']
     ['120' '6.0' '2.2' '5.0' '1.5' 'Iris-virginica']
     ['121' '6.9' '3.2' '5.7' '2.3' 'Iris-virginica']
     ['122' '5.6' '2.8' '4.9' '2.0' 'Iris-virginica']
     ['123' '7.7' '2.8' '6.7' '2.0' 'Iris-virginica']
     ['124' '6.3' '2.7' '4.9' '1.8' 'Iris-virginica']
     ['125' '6.7' '3.3' '5.7' '2.1' 'Iris-virginica']
     ['126' '7.2' '3.2' '6.0' '1.8' 'Iris-virginica']
     ['127' '6.2' '2.8' '4.8' '1.8' 'Iris-virginica']
     ['128' '6.1' '3.0' '4.9' '1.8' 'Iris-virginica']
     ['129' '6.4' '2.8' '5.6' '2.1' 'Iris-virginica']
     ['130' '7.2' '3.0' '5.8' '1.6' 'Iris-virginica']
     ['131' '7.4' '2.8' '6.1' '1.9' 'Iris-virginica']
     ['132' '7.9' '3.8' '6.4' '2.0' 'Iris-virginica']
     ['133' '6.4' '2.8' '5.6' '2.2' 'Iris-virginica']
     ['134' '6.3' '2.8' '5.1' '1.5' 'Iris-virginica']
     ['135' '6.1' '2.6' '5.6' '1.4' 'Iris-virginica']
     ['136' '7.7' '3.0' '6.1' '2.3' 'Iris-virginica']
     ['137' '6.3' '3.4' '5.6' '2.4' 'Iris-virginica']
     ['138' '6.4' '3.1' '5.5' '1.8' 'Iris-virginica']
     ['139' '6.0' '3.0' '4.8' '1.8' 'Iris-virginica']
     ['140' '6.9' '3.1' '5.4' '2.1' 'Iris-virginica']
     ['141' '6.7' '3.1' '5.6' '2.4' 'Iris-virginica']
     ['142' '6.9' '3.1' '5.1' '2.3' 'Iris-virginica']
     ['143' '5.8' '2.7' '5.1' '1.9' 'Iris-virginica']
     ['144' '6.8' '3.2' '5.9' '2.3' 'Iris-virginica']
     ['145' '6.7' '3.3' '5.7' '2.5' 'Iris-virginica']
     ['146' '6.7' '3.0' '5.2' '2.3' 'Iris-virginica']
     ['147' '6.3' '2.5' '5.0' '1.9' 'Iris-virginica']
     ['148' '6.5' '3.0' '5.2' '2.0' 'Iris-virginica']
     ['149' '6.2' '3.4' '5.4' '2.3' 'Iris-virginica']
     ['150' '5.9' '3.0' '5.1' '1.8' 'Iris-virginica']]
    


```python
iris = np.genfromtxt(url, delimiter=',', dtype='str', encoding=None)

species_column = iris[:, 4]

print(species_column)
```

    ['PetalWidthCm' '0.2' '0.2' '0.2' '0.2' '0.2' '0.4' '0.3' '0.2' '0.2'
     '0.1' '0.2' '0.2' '0.1' '0.1' '0.2' '0.4' '0.4' '0.3' '0.3' '0.3' '0.2'
     '0.4' '0.2' '0.5' '0.2' '0.2' '0.4' '0.2' '0.2' '0.2' '0.2' '0.4' '0.1'
     '0.2' '0.1' '0.2' '0.2' '0.1' '0.2' '0.2' '0.3' '0.3' '0.2' '0.6' '0.4'
     '0.3' '0.2' '0.2' '0.2' '0.2' '1.4' '1.5' '1.5' '1.3' '1.5' '1.3' '1.6'
     '1.0' '1.3' '1.4' '1.0' '1.5' '1.0' '1.4' '1.3' '1.4' '1.5' '1.0' '1.5'
     '1.1' '1.8' '1.3' '1.5' '1.2' '1.3' '1.4' '1.4' '1.7' '1.5' '1.0' '1.1'
     '1.0' '1.2' '1.6' '1.5' '1.6' '1.5' '1.3' '1.3' '1.3' '1.2' '1.4' '1.2'
     '1.0' '1.3' '1.2' '1.3' '1.3' '1.1' '1.3' '2.5' '1.9' '2.1' '1.8' '2.2'
     '2.1' '1.7' '1.8' '1.8' '2.5' '2.0' '1.9' '2.1' '2.0' '2.4' '2.3' '1.8'
     '2.2' '2.3' '1.5' '2.3' '2.0' '2.0' '1.8' '2.1' '1.8' '1.8' '1.8' '2.1'
     '1.6' '1.9' '2.0' '2.2' '1.5' '1.4' '2.3' '2.4' '1.8' '1.8' '2.1' '2.4'
     '2.3' '1.9' '2.3' '2.5' '2.3' '1.9' '2.0' '2.3' '1.8']
    


```python
url = './Iris.csv'
iris = np.genfromtxt(url, delimiter=',', dtype='str', encoding=None)

iris_2d = iris[:, :-1].astype(float)

print(iris_2d)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_1368\2007448729.py in <module>
          2 iris = np.genfromtxt(url, delimiter=',', dtype='str', encoding=None)
          3 
    ----> 4 iris_2d = iris[:, :-1].astype(float)
          5 
          6 print(iris_2d)
    

    ValueError: could not convert string to float: 'Id'



```python
sepallength_column = iris[:, 0].astype(float)

mean = np.mean(sepallength_column)
median = np.median(sepallength_column)
std_dev = np.std(sepallength_column)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_1368\1692814743.py in <module>
    ----> 1 sepallength_column = iris[:, 0].astype(float)
          2 
          3 mean = np.mean(sepallength_column)
          4 median = np.median(sepallength_column)
          5 std_dev = np.std(sepallength_column)
    

    ValueError: could not convert string to float: 'Id'



```python

url = './Iris.csv'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

mean = np.mean(iris)
median = np.median(iris)
std_dev = np.std(iris)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
```

    Mean: nan
    Median: nan
    Standard Deviation: nan
    


```python
url = './Iris.csv'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

# Min-Max normalization formula: (x - min) / (max - min)
normalized_sepal_length = (iris - np.min(iris)) / (np.max(iris) - np.min(iris))

print(normalized_sepal_length)
```

    [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
     nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
     nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
     nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
     nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
     nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
     nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
     nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
     nan nan nan nan nan nan nan]
    


```python
url = './Iris.csv'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

percentile_5 = np.percentile(iris, 5)
percentile_95 = np.percentile(iris, 95)

print("5th Percentile:", percentile_5)
print("95th Percentile:", percentile_95)
```

    5th Percentile: nan
    95th Percentile: nan
    


```python
url = './Iris.csv'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

# Generate random row and column indices
random_rows = np.random.choice(iris_2d.shape[0], 20, replace=True)
random_cols = np.random.choice(iris_2d.shape[1], 20, replace=True)

# Insert np.nan values at random positions
iris_2d[random_rows, random_cols] = np.nan

print(iris_2d)
In this code, np.random.choice(iris_2d.shape[0], 20, replace=True) generates 20 random row indices, and np.random.choice(iris_2d.shape[1], 20, replace=True) generates 20 random column indices. Then, iris_2d[random_rows, random_cols] = np.nan assigns np.nan values to the specified random positions in the iris_2d array. The result will be the iris_2d dataset with 20 `np.nan

```


      File "C:\Users\User\AppData\Local\Temp\ipykernel_1368\648856012.py", line 12
        In this code, np.random.choice(iris_2d.shape[0], 20, replace=True) generates 20 random row indices, and np.random.choice(iris_2d.shape[1], 20, replace=True) generates 20 random column indices. Then, iris_2d[random_rows, random_cols] = np.nan assigns np.nan values to the specified random positions in the iris_2d array. The result will be the iris_2d dataset with 20 `np.nan
           ^
    SyntaxError: invalid syntax
    



```python
url = './Iris.csv'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

missing_values = np.isnan(iris_2d[:, 0])  # Check missing values in the sepallength column
num_missing_values = np.sum(missing_values)
positions_missing_values = np.where(missing_values)[0]

print("Number of missing values:", num_missing_values)
print("Positions of missing values:", positions_missing_values)

```

    Number of missing values: 1
    Positions of missing values: [0]
    


```python
url = './Iris.csv'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

filtered_rows = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]

print(filtered_rows)
```

    [[1.  5.1 3.5 1.4]
     [2.  4.9 3.  1.4]
     [3.  4.7 3.2 1.3]
     [4.  4.6 3.1 1.5]]
    


```python
url = './Iris.csv'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

sepal_length = iris_2d[:, 0]
petal_length = iris_2d[:, 2]

correlation = np.corrcoef(sepal_length, petal_length)[0, 1]

print("Correlation between SepalLength and PetalLength:", correlation)
```

    Correlation between SepalLength and PetalLength: nan
    


```python
url = './Iris.csv'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

has_missing_values = np.any(np.isnan(iris_2d))

if has_missing_values:
    print("The dataset has missing values.")
else:
    print("The dataset does not have missing values.")
```

    The dataset has missing values.
    


```python
# Example array with NaN values
arr = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0])

# Replace NaN values with 0
arr[np.isnan(arr)] = 0

print(arr)
```

    [1. 2. 0. 4. 0. 6.]
    


```python
iris = np.genfromtxt(url, delimiter=',', dtype='str', encoding=None)

species_column = iris[:, 4]

unique_species, counts = np.unique(species_column, return_counts=True)

for species, count in zip(unique_species, counts):
    print("Species:", species, "Count:", count)
```

    Species: 0.1 Count: 6
    Species: 0.2 Count: 28
    Species: 0.3 Count: 7
    Species: 0.4 Count: 7
    Species: 0.5 Count: 1
    Species: 0.6 Count: 1
    Species: 1.0 Count: 7
    Species: 1.1 Count: 3
    Species: 1.2 Count: 5
    Species: 1.3 Count: 13
    Species: 1.4 Count: 8
    Species: 1.5 Count: 12
    Species: 1.6 Count: 4
    Species: 1.7 Count: 2
    Species: 1.8 Count: 12
    Species: 1.9 Count: 5
    Species: 2.0 Count: 6
    Species: 2.1 Count: 6
    Species: 2.2 Count: 3
    Species: 2.3 Count: 8
    Species: 2.4 Count: 3
    Species: 2.5 Count: 3
    Species: PetalWidthCm Count: 1
    


```python

```


```python

```


```python

```


```python

```


```python

```
