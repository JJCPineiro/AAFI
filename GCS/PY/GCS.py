#AXOLOTL V1.0

from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt

#MAIN WINDOW
class Window( tk.Tk ):
  def __init__( self , *args , **kwargs ):
    tk.Tk.__init__( self , *args , **kwargs )
    self.title( 'AXOLOTL' )
    self.iconbitmap( 'axolotl.ico' )
    self.configure( background='black' )
    self.resizable( width=False , height=False )

#CONTROL PANEL [LEFT]
class control( tk.Frame ):
  def __init__( self , master ,  *args , **kwargs ):
    tk.Frame.__init__( self , master , *args , **kwargs , bg='black' )
    self.master = master

    """LOGO"""
    #TEAM'S LOGO
    logo = tk.PhotoImage( file='axolotl.gif' )
    self.lblLogo = tk.Label( self , image=logo , borderwidth=0 )
    self.lblLogo.image = logo
    self.lblLogo.pack( )

    """ID"""
    #FRAME: ID
    self.frmId = tk.Frame( self , bg='black' )
    self.frmId.pack( )

    #LABEL: ID
    self.lblId = tk.Label( self.frmId , text='ID: ' , bg='black' , fg='white' )
    self.lblId.pack( side=tk.LEFT )

    #LABEL: ID NUMBER
    self.lblIdN = tk.Label( self.frmId , text='123' , bg='black' , fg='white' , borderwidth=3 , relief='ridge' )
    self.lblIdN.pack( side=tk.RIGHT )

    """START"""
    #BUTTON: START
    self.btnStart = tk.Button( self , text='Start' , command=self.start , bg='green' , fg='white' )
    self.btnStart.pack( fill=tk.X )

    """PORT"""
    #FRAME: PORT
    self.frmPort = tk.Frame( self )
    self.frmPort.pack( )

    #LABEL: PORT
    self.lblPort = tk.Label( self.frmPort , text='PORT: ' , bg="black" , fg="white" )
    self.lblPort.pack( side=tk.LEFT )

    #PORT'S LIST
    self.lstPort = ttk.Combobox( self.frmPort , state='readonly' , )
    self.lstPort[ 'values' ] = [ 'COM1' , 'COM2' , 'COM3' ]
    self.lstPort.set( 'Select port' )
    self.lstPort.pack( side=tk.LEFT )
    
    #PORT STATUS
    self.lblStatus = tk.Label( self.frmPort , text='CONNECTED' , bg="green" , fg="white" )
    self.lblStatus.pack( side=tk.LEFT )


    """WARNINGNS"""
    #FRAME: WARNINGS
    self.frmAdv = tk.Frame( self )
    self.frmAdv.pack( )

    #LABEL: RED
    self.lblR = tk.Label( self.frmAdv , bg='red' , text='Error' , height=3 )
    self.lblR.pack( side=tk.LEFT )

    #LABEL: YELLOW
    self.lblY = tk.Label( self.frmAdv , bg='yellow' , text='Loss' , height=3  )
    self.lblY.pack( side=tk.LEFT )

    #LABEL: GREEN
    self.lblG = tk.Label( self.frmAdv , bg='green' , text='OK!' , height=3 )
    self.lblG.pack( side=tk.LEFT )

    """STOP"""
    #BUTTON: STOP
    self.btnStop = tk.Button( self , text='Stop' , command=self.stop , bg='red' , fg='white' )
    self.btnStop.pack( side=tk.BOTTOM , fill=tk.X )

  #ACTION: START BUTTON
  def start( self ):
    print( 'START' )
    #Calibrar sensores y comienzo de captura de datos

  #ACTION: STOP BUTTON
  def stop( self ):
    print( 'STOP' )
    #Detener lectura de datos, entregar CSV

#DATA PANEL [RIGHT]
class datos( tk.Frame ):
  def __init__( self , master ,  *args , **kwargs ):
    tk.Frame.__init__( self , master , *args , **kwargs , bg='black' )
    self.master = master

    self.lblTest = tk.Label( self , text='DATA PANEL' , bg='black' , fg='white' )
    self.lblTest.pack( )

#MAIN
if __name__ == "__main__":
  window = Window( )
  control( window ).pack( side=tk.LEFT , fill=tk.Y )
  datos( window ).pack( side=tk.RIGHT , fill=tk.Y )
  window.mainloop( )