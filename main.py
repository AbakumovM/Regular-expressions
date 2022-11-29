from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  new_list = []

def formatting_name():
   for i in contacts_list:
      str1 = ' '.join(i[:3])
      if str1.strip().count(' ') == 1:
         contacts_list[contacts_list.index(i)] = str1.split() + i[2:]
      else:
         contacts_list[contacts_list.index(i)] = str1.split() + i[3:]
   
   return 
   
def formatting_number():
   for j in contacts_list:
      pattern1 = r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?'
      j[5] = re.sub(pattern1, r'+7(\2)\3-\4-\5\7\8\9', j[5])
   return
   

def union_name():
   for i in range(1, len(contacts_list)):
      for j in range(1, len(contacts_list)):
         if contacts_list[i][:2] == contacts_list[j][:2]:
            for k in range(len(contacts_list[i])):
               if contacts_list[i][k] == '': 
                  contacts_list[i][k] = contacts_list[j][k]
               
   
   for d in contacts_list:
      if d not in new_list:
         new_list.append(d)
   return      


                

		

if __name__ == '__main__':
   formatting_name()
   formatting_number()
   union_name()
   # print(new_list)

   with open("phonebook.csv", "w", encoding='utf-8') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(new_list)