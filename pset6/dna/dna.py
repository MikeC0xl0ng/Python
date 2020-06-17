#from cs50 import get_string
import sys, os.path, csv

def contaLunghezza(cosa, dove):
  conta = -1
  stato = True
  buf = cosa
  while stato:
    conta = conta + 1
    num = dove.count(buf)
    if num > 0:
      stato = True
    else:
      stato = False
    buf = buf + cosa
  return conta


def main():
#----------------------------control of input-----------------------------------------------------------------------------------
  if(len(sys.argv) == 3):              #control if number of passed arguments = 2 (sys.argv counts also the filename)
    csvPAF = str(sys.argv[1])          #CSV's path and file name
    dnaPAF = str(sys.argv[2])          #DNA's path and file name
    
    if ((os.path.exists(csvPAF)) and (os.path.exists(dnaPAF))):      #control if DNA and CSV file exist
#---------------------------/control of input----------------------------------------------------------------------------------
#CSV
      c = csvPAF.split("/")
      csvFile = c[-1]                          #CSV file's name

      csvData = []                             #saving CSV data to variable "csvData"                    
      file = open(csvPAF, "r")
      reader = csv.reader(file)
      for row in reader:
        try:
          csvData.append(row)   
        except:
          pass

#DNA
      d = dnaPAF.split("/")
      dnaFile = d[-1]                          #DNA File's name

      dnaData = []                               #saving DNA data to variable "dnaData"
      with open(dnaPAF, 'r') as filehandle:
        for line in filehandle:
          current = line[:-1]                    #remove linebreak which is the last character of the string
          dnaData.append(current)                #add item to the list

      dnaGenoms = []
      for i in range(1,len(csvData[0])):
        dnaGenoms.append(csvData[0][i])          #dnaGenoms contains all genoms of the csv file

#-----------------------analysis--------------------------------    

      strDnaData = ' '.join([str(elem) for elem in dnaData])
      print(dnaGenoms)
      result = []
      for i in range(0, len(dnaGenoms)):
        result.append(contaLunghezza(dnaGenoms[i], strDnaData))
      print(result)
      
      


#----------------------/analysis-----------------------------
    
    else:
      print("One of the arguements is wrong")

  else:
    print("Error: you typed wrong number of arguments")

main()

