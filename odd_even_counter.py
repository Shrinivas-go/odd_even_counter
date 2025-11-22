import sys
if len(sys.argv) == 2:
  script_name = sys.argv[0] 
  num = int(sys.argv[1])   
  even_count = 0
  odd_count = 0
  while(num != 0):
    if(num % 2 == 0):
      even_count = even_count+1
    else:
      odd_count = odd_count+1
    num = num // 10      

  print("Even Count", even_count)
  print("Odd Count", odd_count)

else:
  script_name = sys.argv[0] 
  num = 45
  even_count = 0
  odd_count = 0
  while(num != 0):
    if(num % 2 == 0):
      even_count = even_count+1
    else:
      odd_count = odd_count+1
    num = num // 10

  print("Even Count", even_count)
  print("Odd Count", odd_count)
