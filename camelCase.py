def camel_case(txt): 
      txt_Split = txt.split()
      List = [txt_Split[0].lower()]


      #loop
      for j in range(1, len(txt_Split)):
         word = txt_Split[j].capitalize()
         List.append(word)
   
      return "" .join(List)
      
def main():
    
   txt = input('Enter your sentence: ')
   camelcased= camel_case(txt)
   print(camelcased) 
   
if __name__ == "__main__":
    main()