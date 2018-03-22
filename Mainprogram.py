import sys
from PyQt4 import QtCore, QtGui
import calculator
import math
import length
import weight

num = 0.0
newNum = 0.0
sumAll = 0.0
operator = ""
 
opVar = False
sumIt = 0



class WEIGHT(QtGui.QMainWindow, weight.Ui_Form):
    def __init__(self, parent=None):
        super(WEIGHT, self).__init__(parent)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.frm.addItems(["Kilograms","Pounds","Ounces"])
        self.to.addItems(["Kilograms","Pounds","Ounces"])
        self.one.clicked.connect(self.Nums)
        self.two.clicked.connect(self.Nums)
        self.three.clicked.connect(self.Nums)
        self.four.clicked.connect(self.Nums)
        self.five.clicked.connect(self.Nums)
        self.six.clicked.connect(self.Nums)
        self.seven.clicked.connect(self.Nums)
        self.eight.clicked.connect(self.Nums)
        self.nine.clicked.connect(self.Nums)
        self.zero.clicked.connect(self.Nums)
        self.point.clicked.connect(self.pointClicked)

        self.frm.currentIndexChanged.connect(self.updateUi)
        self.to.currentIndexChanged.connect(self.updateUi)

    def updateUi(self):
        f=self.frm.currentText()
        t=self.to.currentText()
        g=self.input.text()
        num=float(g)
        if ((f=="Kilograms") and (t=="Pounds")):
            result=num*2.20462
        if (f=="Kilograms") and (t=="Ounces"):
            result=num*35.274
        if (f=="Kilograms") and (t=="Kilograms"):
            result=num*1.0
        if (f=="Pounds") and (t=="Ounces"):
            result=num*16.0
        if (f=="Pounds") and (t=="Kilograms"):
            result=num*0.453592
        if (f=="Pounds") and (t=="Pounds"):
            result=num*1
        if (f=="Ounces") and (t=="Kilograms"):
            result=num*0.0283495
        if (f=="Ounces") and (t=="Pounds"):
            result=num*0.06249995
        if (f=="Ounces") and (t=="Ounces"):
            result=num*1.0         
        self.output.setText(str(result))  

    def Nums(self):
        global num
        global newNum
        global opVar
         
        sender = self.sender()
         
        newNum = int(sender.text())
        setNum = str(newNum)
        self.input.setText(self.input.text() + setNum)   

    def pointClicked(self):
        global opVar
         
        if "." not in self.input.text():
            self.input.setText(self.input.text() + ".")            


class LENGTH(QtGui.QMainWindow, length.Ui_Form):
    def __init__(self, parent=None):
        super(LENGTH, self).__init__(parent)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.frm.addItems(["Metre","Inches","Feet"])
        self.to.addItems(["Metre","Inches","Feet"])
        self.one.clicked.connect(self.Nums)
        self.two.clicked.connect(self.Nums)
        self.three.clicked.connect(self.Nums)
        self.four.clicked.connect(self.Nums)
        self.five.clicked.connect(self.Nums)
        self.six.clicked.connect(self.Nums)
        self.seven.clicked.connect(self.Nums)
        self.eight.clicked.connect(self.Nums)
        self.nine.clicked.connect(self.Nums)
        self.zero.clicked.connect(self.Nums)
        self.pushButton.clicked.connect(self.pointClicked)


        self.frm.currentIndexChanged.connect(self.updateUi)
        self.to.currentIndexChanged.connect(self.updateUi)

    def updateUi(self):
        f=self.frm.currentText()
        t=self.to.currentText()
        g=self.input.text()
        num=float(g)
        if ((f=="Metre") and (t=="Inches")):
            result=num*39.3701
        if (f=="Metre") and (t=="Feet"):
            result=num*3.28084
        if (f=="Metre") and (t=="Metre"):
            result=num*1.0
        if (f=="Inches") and (t=="Inches"):
            result=num*1.0
        if (f=="Inches") and (t=="Feet"):
            result=num*0.0833333
        if (f=="Inches") and (t=="Metre"):
            result=num*0.0254
        if (f=="Feet") and (t=="Inches"):
            result=num*12.0
        if (f=="Feet") and (t=="Metre"):
            result=num*0.3048
        if (f=="Feet") and (t=="Feet"):
            result=num*1.0         
        self.output.setText(str(result))  

    def Nums(self):
        global num
        global newNum
        global opVar
         
        sender = self.sender()
         
        newNum = int(sender.text())
        setNum = str(newNum)
        self.input.setText(self.input.text() + setNum)

    def pointClicked(self):
        global opVar
         
        if "." not in self.input.text():
            self.input.setText(self.input.text() + ".")               


class Mainclass(QtGui.QMainWindow, calculator.Ui_Form):
    def __init__(self):
        super(Mainclass, self).__init__()
        self.setupUi(self)  
        self.line.setText("0")
        self.toolButton.setPopupMode(1)
        self.m=QtGui.QMenu()
        self.m.addAction("Length",self.length)
        self.toolButton.setMenu(self.m)

    
        self.one.clicked.connect(self.Nums)
        self.two.clicked.connect(self.Nums)
        self.three.clicked.connect(self.Nums)
        self.four.clicked.connect(self.Nums)
        self.five.clicked.connect(self.Nums)
        self.six.clicked.connect(self.Nums)
        self.seven.clicked.connect(self.Nums)
        self.eight.clicked.connect(self.Nums)
        self.nine.clicked.connect(self.Nums)
        self.zero.clicked.connect(self.Nums)
        self.add.clicked.connect(self.Operator)
        self.sub.clicked.connect(self.Operator)
        self.div.clicked.connect(self.Operator)
        self.mul.clicked.connect(self.Operator)
        self.rem.clicked.connect(self.Operator)
        self.equal.clicked.connect(self.Equal)
        self.fact.clicked.connect(self.FACT)
        self.sqr.clicked.connect(self.SQR)
        self.LN.clicked.connect(self.Ln) 
        self.LOG.clicked.connect(self.Log)
        self.inv.clicked.connect(self.INV)
        self.base10.clicked.connect(self.BASE10)
        self.basee.clicked.connect(self.BASEE)
        self.bckspc.clicked.connect(self.Back)
        self.clear.clicked.connect(self.CE)
        self.allclear.clicked.connect(self.C)
        self.per.clicked.connect(self.Operator)
        self.com.clicked.connect(self.Operator)
        self.power.clicked.connect(self.Operator)
        self.point.clicked.connect(self.pointClicked)
        self.Sin.clicked.connect(self.SIN)
        self.Cos.clicked.connect(self.COS)
        self.Tan.clicked.connect(self.TAN)
        self.AS.clicked.connect(self.As)
        self.AC.clicked.connect(self.Ac)
        self.AT.clicked.connect(self.At)
        self.hex.clicked.connect(self.HEX)
        self.Oct.clicked.connect(self.OCT)

        self.toolButton.setPopupMode(1)
        self.m=QtGui.QMenu()
        self.m.addAction("Length",self.length)
        self.m.addAction("Weight",self.weight)
        self.toolButton.setMenu(self.m)


    def weight(self):
        win = WEIGHT(self)
        win.show()        



    def length(self):
        window = LENGTH(self)
        window.show()    



    def HEX(self):
        global n
        global x
        x=int(self.line.text())
        n=hex(x) 
        self.line.setText(str(n))   


    def OCT(self):
        global n
        global x
        x=int(self.line.text())
        n=oct(x) 
        self.line.setText(str(n))       
            


    def SIN(self):
         global n
         global x
         x=float(self.line.text())
         n=math.sin(x) 
         self.line.setText(str(n))   



    def COS(self):
         global n
         global x
         x=float(self.line.text())
         n=math.cos(x) 
         self.line.setText(str(n))   


    def TAN(self):
         global n
         global x
         x=float(self.line.text())
         n=math.tan(x) 
         self.line.setText(str(n))   
         


    def As(self):
         global n
         global x
         x=float(self.line.text())
         n=math.asin(x) 
         self.line.setText(str(n))   
         

    def Ac(self):
         global n
         global x
         x=float(self.line.text())
         n=math.acos(x) 
         self.line.setText(str(n))   
         

    def At(self):
         global n
         global x
         x=float(self.line.text())
         n=math.atan(x) 
         self.line.setText(str(n))                       
    


    def Nums(self):
        global num
        global newNum
        global opVar
         
        sender = self.sender()
         
        newNum = int(sender.text())
        setNum = str(newNum)
 
 
        if opVar == False:
            self.line.setText(self.line.text() + setNum)
 
 
        else:
            self.line.setText(setNum)
            opVar = False


    def Operator(self):
        global num
        global opVar
        global operator
        global sumIt
 
        sumIt += 1
 
        if sumIt > 1:
            self.Equal()
 
        num = self.line.text() 
        sender = self.sender() 
        operator = sender.text()         
        opVar = True



    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar
        global sumIt
        global f
        global fa
        global fa1
        fa=fa1=fa2=1
 
        sumIt = 0
 
        newNum = self.line.text()
 
        
         
        if operator == "+":
            sumAll = float(num) + float(newNum)
            self.line.setText(str(sumAll))
            opVar = True    
 
        elif operator == "-":
            sumAll = float(num) - float(newNum)
            self.line.setText(str(sumAll))
            opVar = True    
 
        elif operator == "/":
            if(float(newNum)!=0.0):
              sumAll = float(num) / float(newNum)
              self.line.setText(str(sumAll))
            else:
              self.line.setText("Math error")   
            opVar = True    
 
        elif operator == "*":
            sumAll = float(num) * float(newNum)
            self.line.setText(str(sumAll))
            opVar = True    

        elif operator =="%":  
            if(float(newNum)!=0.0):  
               sumAll = float(num)%float(newNum)
               self.line.setText(str(sumAll))
            else:
              self.line.setText("Math error")      
            opVar = True    

        elif operator == "npr":
            if(int(num)>=int(newNum)):

                for f in range(1,(int(num)+1)):
                   fa=fa*f
                for f in range (1,(int(num)-int(newNum)+1)):
                    fa1=fa1*f
                self.line.setText(str(fa/fa1))    
            else:
                self.line.setText("Math error")                             
            

        elif operator == "ncr":
            if(int(num)>=int(newNum)):
                for f in range(1,(int(num)+1)):
                   fa=fa*f
                for f in range (1,(int(num)-int(newNum)+1)):
                   fa1=fa1*f
                for f in range(1,(int(newNum)+1)):
                   fa2=fa2*f 
                f=fa2*fa1     
                self.line.setText(str(int(fa/f))) 
            else:
                self.line.setText("Math error")        


        elif operator == "x^y":
            global s
            if(x>=0):
              s=math.pow(int(num),newNum)
              self.line.setText(str(s))
            else:
              self.line.setText("Math error")
                   


                    
    def pointClicked(self):
        global opVar
         
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")            
        
        
     
    def FACT(self):

        global n
        global f
        global fa
        fa=1
        n=int(self.line.text())
        if(n>0):
          for f in range(1,(n+1)):
            fa=f*fa
        elif(n==0):
            fa=1
        else:
             self.line.setText("Math error")         
        self.line.setText(str(fa))
        



    def SQR(self):
        global n
        global num
        n=float(self.line.text())
        num=n**2
        self.line.setText(str(num))
        

    def Ln(self):
        global n
        global num
        n=float(self.line.text())
        if(n>0):
           num=2.303*math.log10(n)
           self.line.setText(str(num))
        else:
            self.line.setText("Math error")

    def Log(self):
        global n
        global num
        n=float(self.line.text())
        if(n>0):
           num=math.log10(n)
           self.line.setText(str(num))
        else:
            self.line.setText("Math error")


    def INV(self):
        global n
        global num
        n=float(self.line.text())
        if(n!=0.0):
           num=1.0/n
           self.line.setText(str(num))
        else:
           self.line.setText("Math error")
   


    def BASE10(self):
        global n
        global num
        n=float(self.line.text())
        num=10**n
        self.line.setText(str(num))
        

    def BASEE(self):
        global n
        global num
        n=float(self.line.text())
        num=2.71828**n
        self.line.setText(str(num))

    def Back(self):
        self.line.backspace()
 
    def C(self):
        global newNum
        global sumAll
        global operator
        global num
         
        self.line.clear()
 
        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        operator = ""
        self.line.setText("0")

 
    def CE(self):
        self.line.clear()    
        

         


if __name__ == '__main__':  # if we're running file directly and not importing it
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = Mainclass()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app
    