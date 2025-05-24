MAX_FIB_VALUE: int = 10000  

def main():
    first = 0      
    second = 1     
    
    while first <= MAX_FIB_VALUE:
        print(first, end=' ') 
        next_fib = first + second  
        first = second
        second = next_fib

if __name__ == '__main__':
    main()
