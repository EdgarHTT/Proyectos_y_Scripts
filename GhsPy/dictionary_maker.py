from io import open
import pickle

class Hcode:
     
    def __init__(self, *args):
        self.hcode = args[0]
        self.hazard_statement = args[1]
        self.gHS_hazard_class = args[2]
        self.gHS_hazard_category = args[3]
        #The first 4 attributes are fine, the next ones need to be checked case by case
        #TODO make the key word checker
        for index in range(len(args)):
            if str(args[index]).startswith("Div") or str(args[index]).startswith("Class"):
                self.un_model_regulations_class_or_division = args[index]
                pass
            if str(args[index]).startswith("GH"):
                self.pictogram = args[index]
                pass
            if str(args[index]).startswith("Warning") or str(args[index]).startswith("Danger"):
                self.gHS_signal_word = args[index]
                pass
            if str(args[index]).startswith("P"):
                self.pcode = args[index]
                pass
        print(f"The object code: {self.hcode} has been created")
    
    def __str__(self):
        return "Code:{}\n Statement:{}\n Hazard Class:{}\n Hazard Category:{}\n UN Model:{}\n Regulation class:{}\n GHS Pictogram:{}\n GHS Signal Word:{}\n P-Code:{}\n".format(self.hcode,self.hazard_statement,self.gHS_hazard_class,self.gHS_hazard_category,self.un_model_regulations_class_or_division,self.pictogram,self.gHS_signal_word,self.pcode)
          

class Pcode:
     
    def __init__(self, *args):
        self.pcode = args[0]
        self.statement = args[1]
        print(f"The object code: {self.pcode} has been created")

def txt_to_object(txtfile):
    with open(txtfile,"r") as text:
            
        lines = text.readlines()    #Separates the text into lines by their new lines
        hlines = []                 #For separate object lists
        plines = []

        for index,line in enumerate(lines):
            
            line = line.strip('\n') #Removes the \n new line command from the str
            line = line.strip().split("\t")     #Strips empty outsides spaces and splits the str into a list separated by tabulations
            
            line = [x for x in line if x != ""]     #Filters!
            line = [x for x in line if x != "\n"]   #I don't undestand the syntax :,)

            try:                    #Sorts the lines by their code and turns them into objects
                if line[0].startswith("H"):
                    hlines.append(Hcode(*line))
                elif line[0].startswith("P"):
                    plines.append(Pcode(*line))
            except IndexError:      #When the line is just an empty list it doesnt index it
                    print(f"Error: No data in index {index}")
    for index,n in enumerate(hlines):
        print(hlines[index])


    #print(f"The code: {plines[1].pcode} has the hazard statement: {plines[1].statement}")

txt_to_object('ghscode_10.txt')

#TODO object_to_binary_file: