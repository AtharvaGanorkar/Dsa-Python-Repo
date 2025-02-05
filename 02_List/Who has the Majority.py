n= 11
arr=[1,1,2,2,3,3,4,4,4,4,5]
x = 4 
y = 5


def majorityWins(self, arr, n, x, y):
        count_x = arr.count(x)
        count_y = arr.count(y)
        
        if count_x > count_y:
            return x
        elif count_y > count_x:
            return y
        else:
            return min(x,y)
        

#Back-end complete function Template for Python 3

#Function to find element with more appearances between two elements in an array.    
class Solution:
    def majorityWins(self, arr, n, x, y):
        count_x=0;
        count_y=0;
        
        for i in range(0,n):
            #Iterating through the array elements.
            #Incrementing the counter variables accordingly.
            if(arr[i]==x):
                count_x+=1
            if(arr[i]==y):
                count_y+=1
        
        #Comparing the two counters.
        #If both appear same number of times, returning the smaller number.
        if(count_x>count_y or (count_x==count_y and x<y)):
            #Returning the number with more appearances in the array.
            return x
        else:
            #Returning the number with more appearances in the array.
            return y