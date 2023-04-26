from os import path



THIS_FOLDER = path.dirname(path.abspath(__file__))

compTable = {
              "0" : "0101010",
              "1" : "0111111",
              "-1": "0111010",
              "D" : "0001100",
              "A" : "0110000",
              "!D": "0001101",
              "!A": "0110001",
              "-D": "0001111",
              "-A": "0110011",
              "D+1": "0011111",
              "A+1": "0110111",
              "D-1": "0001110",
              "A-1": "0110010",
              "D+A": "0000010",
              "D-A": "0010011",
              "A-D": "0000111",
              "D&A": "0000000",
              "D|A": "0010101",
              "M":   "1110000",
              "!M":  "1110001",
              "-M":   "1110011",
              "M+1":  "1110111",
              "M-1": "1110010",
              "D+M": "1000010",
              "D-M": "1010011",
              "M-D": "1000111",
              "D&M": "1000000",
              "D|M": "1010101"
}

destTable = {
              "null":"000",
              "M":"001",
              "D": "010",
              "MD":"011",
              "A": "100",
              "AM": "101",
              "AD": "110",
              "AMD": "111"
}

jumpTable = {
              "null":"000",
              "JGT":"001",
              "JEQ": "010",
              "JGE":"011",
              "JLT": "100",
              "JNE": "101",
              "JLE": "110",
              "JMP": "111"
}


class parser:
    def __init__(self,file_path) -> None:
        self.file_path = file_path
        with open(file_path, 'r+') as fp:
            self.lines = fp.readlines()

        self.n=16
        self.symbolTable={
           "SP":"0",
           "LCL":"1",
           "ARG":"2",
           "THIS":"3",
           "THAT":"4",
           "R0":"0",
           "R1":"1",
           "R2":"2",
           "R3":"3",
           "R4":"4",
           "R5":"5",
           "R6":"6",
           "R7":"7",
           "R8":"8",
           "R9":"9",
           "R10":"10",
           "R11":"11",
           "R12":"12",
           "R13":"13",
           "R14":"14",
           "R15":"15",
           "SCREEN":"16384",
           "KBD":"24576"
        }

    def viewAssemblyFile(self)-> None:
        for line in self.lines:
            print(line)



    def removeWhiteSpacesAndComments(self)-> None:
        self.LineswhiteSpacesRemoved = []

        for line in self.lines:
            if ((line[0] =="/" and line[1] =="/") or (line == "")):
                pass
            else:
              line = line.split("//",1)[0]
              self.LineswhiteSpacesRemoved.append(line.strip())
        
        while("" in self.LineswhiteSpacesRemoved):
          self.LineswhiteSpacesRemoved.remove('')

        #for x in self.LineswhiteSpacesRemoved:
          #print(x)


    def convertBinary(self):
      self.LinesBinary=[]
      removed=0
      for idx, instruction in enumerate(self.LineswhiteSpacesRemoved):
          count=1
          if(instruction[0]=="("):
            strippedText = instruction.replace('(','').replace(')','').replace('\'','').replace('\"','')
            if strippedText in self.symbolTable.keys():
               pass
            else:
              if(strippedText == "sys.init"):
                print(idx)
              removed+=1

              while(self.LineswhiteSpacesRemoved[idx+count][0] == "("):
                 count+=1
                 removed+=1
                 
              self.symbolTable.update({strippedText: "{}".format(idx+count-removed)})  
              count=1
              while(self.LineswhiteSpacesRemoved[idx+count][0] == "("):
                  count+=1
                  removed-=1

            if(strippedText == "sys.init"):
               print(removed)
               print(count)
               print(idx+count-removed)    
            self.LineswhiteSpacesRemoved[idx]=" "

      while " " in self.LineswhiteSpacesRemoved:
          self.LineswhiteSpacesRemoved.remove(" ")

      #print(self.LineswhiteSpacesRemoved)
      for idx, instruction in enumerate(self.LineswhiteSpacesRemoved):
          if(instruction[0] == "@"):
            value = instruction.split("@",1)[1]

            if value.isnumeric():
               pass
            elif (value in self.symbolTable.keys()):
                value = self.symbolTable[value]
            else:
                self.symbolTable.update({value: "{}".format(self.n)})
                value = self.symbolTable[value]
                self.n = self.n + 1

            instruction = "0" +  "{:0>15b}".format(int(value))
            self.LinesBinary.append(instruction)
          
          else:
            if(instruction.find("=") != -1):
              dest = (instruction.split("=",1)[0]).strip()
              comp = ((instruction.split("=",1)[1]).split(";",1)[0]).strip()

            else:
              dest="null"
              comp = (instruction.split(";",1)[0]).strip()

            
            if(instruction.find(";") != -1):
                jump = (instruction.split(comp+";",1)[1]).strip()
            else:
                jump = "null"

            instruction ="111" + compTable[comp] + destTable[dest] + jumpTable[jump]
            self.LinesBinary.append(instruction)
      #print(self.LinesBinary)


    def createBinary(self):
      output_path = (self.file_path).split(".asm",1)[0]+".hack"
      with open(output_path, 'w') as of:
        for line in self.LinesBinary:
          of.write(line)
          of.write('\n')
       



myfile= THIS_FOLDER + "/add/Add.asm"
add = parser(myfile)
add.removeWhiteSpacesAndComments()
add.convertBinary()
add.createBinary()