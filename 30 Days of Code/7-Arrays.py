if __name__ == '__main__':
      n = int(input())
      #initializing array/list which will take input with spaces
      arr = list(map(int, input().rstrip().split()))  
      arr.reverse()  #to reverse the array
      
      #we are using loop to print the array
      for x in range(len(arr)): 
            print(arr[x],end=" ") 
      
      #we can use it like that
      #>>>>>> print(arr, end=" ")
      #but there an issue if we print like that it print like [1,2,3], which we don't want.