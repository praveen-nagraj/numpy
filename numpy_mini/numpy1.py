import numpy as np

def basic_arthmetic(arr1,arr2):
   '''Performs Addition, Substraction,multiplication,division, mod and power'''
   try:
      print("Addition: ",np.add(arr1,arr2))
      print("substraction:",np.subtract(arr1,arr2))
      print("multiplication: ",np.multiply(arr1,arr2))
      print("Divide: ",np.divide(arr1,arr2))
      print("mod:",np.mod(arr1,arr2))
      print("Power: ",np.power(arr1,arr2))
   except ValueError:
      print("invalid input")
   except Exception as e:
       print("An unexpected error occured")


def static_func(arr):
   '''Performs mean,median,standard deviation,variance,min,max,sum,product'''
   try:
      print("mean :",np.mean(arr))
      print("Median :",np.median(arr))
      print("standard deviation",np.std(arr))
      print("variance",np.var(arr))
      print("max",np.max(arr))
      print("min",np.min(arr))
      print("sum",np.sum(arr))
      print("Product",np.prod(arr))
      print("shape",arr.shape)
      print("size",arr.size)
      print("data type",arr.dtype)
   except ValueError:
      print("Invalid Inputs")
   except Exception as e:
      print("An unexpected error occured")


def array_manipulation(arr):
   '''Performs sorting,unique,filter,extract,reshape'''
   try:
      if arr.size == 0:
         raise ValueError("Array cannot be empty for manipulation operations.")
        
      # 1. Sorting
      print("Sorted Array :", np.sort(arr))
        
      # 2. Unique Value Extraction
      print("Unique Values :", np.unique(arr))
        
      # 3. Filtering Values Greater Than the Mean
      mean_val = np.mean(arr) 
        
      filter_arr = arr[arr > mean_val]
      print("Mean Value Used for Filtering :", mean_val)
      print("Filtered Values (> Mean) :", filter_arr)

      # 4. Extracting First Few Elements (using Numpy Slicing)
      extract_count = 3
      first_elements = arr[:extract_count]
      print(f"First {extract_count} Elements :", first_elements)
        
      # 5. Reshaping (using arr.reshape)
      size = arr.size
      if size >= 4 and size % 2 == 0:
         new_shape = (size // 2, 2)
         reshaped_arr = arr.reshape(new_shape)            
         print(f"Reshaped Array{new_shape} :\n",reshaped_arr)
      else:
         print("Reshaping (2 columns) : Not possible (array size is odd or too small)")

   except ValueError:
      print("Invalid Inputs")
   except Exception as e:
      print("An unexpected error occured")


def main():
      print("\n  \t\t\t Numpy calculator Menu\t\t\t")
      print("Press 1  - Arthmetic Operation")
      print("Press 2  - Statiscal Operation")
      print("Press 3  - Array Manipulation")
      print("Press 4  - Exit")

      try:
         raw_choice = input()
               
         if not raw_choice.isdigit():
            print("Please enter a number from 1 to 4")
            return
      
         choice = int(raw_choice)
      
         if choice == 1:
            try:
               arr1_list = list(map(int,input("Enter element for array1 as (1,2,3): ").split()))
               arr2_list = list(map(int,input("Enter element for array1 as (1,2,3): ").split()))

               arr1 = np.array(arr1_list)
               arr2 = np.array(arr2_list)
               print("Array 1 : ",arr1)
               print("Array 2 : ",arr2)

               if arr1.size == arr2.size and arr1.size > 0:
                   basic_arthmetic(arr1,arr2)
               elif arr1.size != arr2.size:
                  print("Array must be the same size")
               else:
                  print("Invalid input")
            
            except ValueError:
                print("Invalid Input")

         elif choice == 2:
            try:
               arr_list = list(map(int,input("Enter element for array1 as (1,2,3): ").split()))
               arr = np.array(arr_list)
               static_func(arr)
            except ValueError:
                  print("Invalid Input")

         elif choice == 3:
            try:
               arr_list = list(map(int,input("Enter element for array1 as (1,2,3): ").split()))
               arr = np.array(arr_list)
               array_manipulation(arr)
            except ValueError:
                  print("Invalid Input")
            
         elif choice == 4:
               print("Exiting the Calculator")
               

         else:
            print("invalid Choice")
      
      except ValueError:
       print("Invalid Input")         

if __name__ == "__main__":
   main()
