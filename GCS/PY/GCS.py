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
    self.attributes("-fullscreen", True )
    self.resizable( width=False , height=False )

#CONTROL PANEL [LEFT]
class control( tk.Frame ):
  def __init__( self , master ,  *args , **kwargs ):
    tk.Frame.__init__( self , master , *args , **kwargs , bg='black' )
    self.master = master

    """LOGO"""
    #TEAM'S LOGO
    logo = tk.PhotoImage( file='axolotl.gif' )
    self.lblLogo = tk.Label(  self ,
                              image=logo ,
                              borderwidth=0 )
    self.lblLogo.image = logo
    self.lblLogo.pack( )

    """ID"""
    #FRAME: ID
    self.frmId = tk.Frame( self , bg='black' )
    self.frmId.pack( pady=10 )

    #LABEL: ID
    self.lblId = tk.Label(  self.frmId ,
                            text='ID: ' ,
                            bg='black' ,
                            fg='white' )
    self.lblId.pack( side=tk.LEFT )

    #LABEL: ID NUMBER
    self.lblIdN = tk.Label( self.frmId ,
                            text='123' ,
                            bg='black' ,
                            fg='white' ,
                            font=( 'Console', 10 ) ,
                            borderwidth=3 ,
                            relief='ridge' )
    self.lblIdN.pack( side=tk.RIGHT )

    """START"""
    #BUTTON: START
    self.btnStart = tk.Button(  self ,
                                text='Start' ,
                                command=self.start ,
                                bg='green' ,
                                fg='white' ,
                                font=( 'Helvetica' , 12 ) ,
                                borderwidth=5 ,
                                relief='raised' )
    self.btnStart.pack( fill=tk.X , pady=10 )

    """PORT"""
    #FRAME: PORT
    self.frmPort = tk.Frame( self , bg='black' )
    self.frmPort.pack( pady=10 )

    #LABEL: PORT
    self.lblPort = tk.Label(  self.frmPort ,
                              text='PORT: ' ,
                              bg="black" , 
                              fg="white" )
    self.lblPort.pack( side=tk.LEFT )

    #PORT'S LIST
    self.lstPort = ttk.Combobox(  self.frmPort ,
                                  state='readonly' )
    self.lstPort[ 'values' ] = [ 'COM1' , 'COM2' , 'COM3' ]
    self.lstPort.set( 'Select port' )
    self.lstPort.pack( side=tk.LEFT )
    
    #PORT STATUS
    self.lblStatus = tk.Label(  self.frmPort ,
                                text='CONNECTED' ,
                                bg="green" ,
                                fg="white" )
    self.lblStatus.pack( side=tk.LEFT )


    """WARNINGNS"""
    #FRAME: WARNINGS
    self.frmAdv = tk.Frame( self , bg='black' )
    self.frmAdv.pack( pady=10 )

    #LABEL: RED
    self.lblR = tk.Label( self.frmAdv ,
                          text='❌' ,
                          bg='red' ,
                          height=2 ,
                          width=5 ,
                          relief='raised' ,
                          borderwidth=5 ,
                          font=( 'Helvetica' , 20 ) )
    self.lblR.pack( side=tk.LEFT , padx=5 , fill=tk.BOTH )

    #LABEL: YELLOW
    self.lblY = tk.Label( self.frmAdv ,
                          text='⚠️' ,
                          bg='yellow' ,
                          height=2 ,
                          width=5 ,
                          relief='raised' ,
                          borderwidth=5 ,
                          font=( 'Helvetica' , 20 ) )
    self.lblY.pack( side=tk.LEFT , padx=5 , fill=tk.BOTH )

    #LABEL: GREEN
    self.lblG = tk.Label( self.frmAdv ,
                          text='✔️' ,
                          bg='green' ,
                          height=2 ,
                          width=5 ,
                          relief='raised' ,
                          borderwidth=5 ,
                          font=( 'Helvetica' , 20 ) )
    self.lblG.pack( side=tk.LEFT , padx=5 , fill=tk.BOTH )

    """EXIT"""
    #BUTTON: EXIT
    self.btnExit = tk.Button( self ,
                              text='Exit' ,
                              command=self.exit , 
                              bg='white' , 
                              fg='red' ,
                              font=( 'Helvetica' , 12 ) ,
                              borderwidth=5 ,
                              relief='raised' )
    self.btnExit.pack( side=tk.BOTTOM , fill=tk.X )

    """STOP"""
    #BUTTON: STOP
    self.btnStop = tk.Button( self , 
                              text='Stop' ,
                              command=self.stop ,
                              bg='red' ,
                              fg='white' ,
                              font=( 'Helvetica' , 12 ) ,
                              borderwidth=5 ,
                              relief='raised' )
    self.btnStop.pack( side=tk.BOTTOM , fill=tk.X , pady=10 )

  #ACTION: START BUTTON
  def start( self ):
    print( 'START' )
    #Calibrar sensores y comienzo de captura de datos

  #ACTION: STOP BUTTON
  def stop( self ):
    print( 'STOP' )
    #Detener lectura de datos, entregar CSV

  def exit( self ):
    self.master.destroy( )

#DATA PANEL [RIGHT]
class datos( tk.Frame ):
  def __init__( self , master ,  *args , **kwargs ):
    tk.Frame.__init__( self , master , *args , **kwargs , bg='black' )
    self.master = master

    """LEVELS"""
    #FRAME: LEVELS
    self.frmLevel = tk.Frame( self , bg='black' )
    self.frmLevel.grid( row=0 , column=0 , sticky='NSEW' )

    #ALTITUD
    self.Alt = ttk.Progressbar( self.frmLevel ,
                                orient='vertical' ,
                                length=200 ,
                                mode='determinate' )
    self.Alt.grid( row=0 , column=0 )
    tk.Label( self.frmLevel ,
              text='Altitud' ,
              bg='black' ,
                fg='white' ).grid( row=1 , column=0 )

    #PRESSURE
    self.Pres = ttk.Progressbar(  self.frmLevel ,
                                  orient='vertical' ,
                                  length=200 ,
                                  mode='determinate' )
    self.Pres.grid( row=0 , column=1 )
    tk.Label( self.frmLevel ,
              text='Pressure' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=1 )

    #TEMPERATURE
    self.Temp = ttk.Progressbar( self.frmLevel ,
                                orient='vertical' ,
                                length=200 ,
                                mode='determinate' )
    self.Temp.grid( row=0 , column=2 )
    tk.Label( self.frmLevel ,
              text='Temperature' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=2 )

    #VOLTAGE
    self.Volt = ttk.Progressbar( self.frmLevel ,
                                orient='vertical' ,
                                length=200 ,
                                mode='determinate' )
    self.Volt.grid( row=0 , column=3 )
    tk.Label( self.frmLevel ,
              text='Voltage' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=3 )

    self.frmLevel.grid_columnconfigure( 0 , weight=1 )
    self.frmLevel.grid_columnconfigure( 1 , weight=1 )
    self.frmLevel.grid_columnconfigure( 2 , weight=1 )
    self.frmLevel.grid_columnconfigure( 3 , weight=1 )

    """ACCOUNTANTS"""
    #FRAME: ACCOUNTANTS
    self.frmAcc = tk.Frame( self , bg='black' )
    self.frmAcc.grid( row=0 , column=1 , sticky='E')

    #LABEL: TIME
    self.lblTime = tk.Label(  self.frmAcc ,
                              text='00:00:00' ,
                              bg='black' ,
                              fg='white' ,
                              font=( 'Fixedsys', 40 ) ,
                              borderwidth=3 ,
                              relief='ridge' )
    self.lblTime.pack( side=tk.TOP , fill=tk.BOTH )
    tk.Label( self.frmAcc ,
              text='Mission Time' ,
              bg='black' ,
              fg='white' ).pack( fill=tk.BOTH )

    #LABEL: PACKAGES
    self.lblPack = tk.Label(  self.frmAcc ,
                              text='0' ,
                              bg='black' ,
                              fg='white' ,
                              font=( 'Fixedsys', 40 ) ,
                              borderwidth=3 ,
                              relief='ridge' ,
                              anchor='e')
    self.lblPack.pack( fill=tk.BOTH )
    tk.Label( self.frmAcc ,
              text='Packets' ,
              bg='black' ,
              fg='white' ).pack( fill=tk.BOTH )

    """PLOTS"""
    #FRAME: PLOTS
    self.frmPlots = tk.Frame( self , bg='black' )
    self.frmPlots.grid( row=1 , column=0 , columnspan=2 )

    #PLOT: ALTITUD
    self.pltAlt = tk.Canvas(  self.frmPlots ,
                              width=100 ,
                              height=100 ,
                              bg='white'  )
    self.pltAlt.grid( row=0 , column=0 , padx=2 )
    tk.Label( self.frmPlots ,
              text='Altitud' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=0 , padx=2 )

    #PLOT: PRESSURE
    self.pltPres = tk.Canvas(  self.frmPlots ,
                              width=100 ,
                              height=100 ,
                              bg='white' )
    self.pltPres.grid( row=0 , column=1 , padx=2 )
    tk.Label( self.frmPlots ,
              text='Pressure' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=1 , padx=2 )

    #PLOT: TEMPERATURE
    self.pltTemp = tk.Canvas( self.frmPlots ,
                              width=100 ,
                              height=100 ,
                              bg='white' )
    self.pltTemp.grid( row=0 , column=2 , padx=2 )
    tk.Label( self.frmPlots ,
              text='Temperature' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=2 , padx=2 )

    #PLOT:VOLTAGE
    self.pltVolt = tk.Canvas( self.frmPlots ,
                              width=100 ,
                              height=100 ,
                              bg='white' )
    self.pltVolt.grid( row=0 , column=3 , padx=2 )
    tk.Label( self.frmPlots ,
              text='Voltage' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=3 , padx=2 )

    """GRAPHS"""
    #FRAME: GRAPHS
    self.frmGraphs = tk.Frame( self , bg='black' )
    self.frmGraphs.grid( row=2 , column=0 , columnspan=2 )

    #GRAPH: ROLL
    self.Roll = tk.Canvas( self.frmGraphs ,
                              width=100 ,
                              height=100 ,
                              bg='white' )
    self.Roll.grid( row=0 , column=0 , padx=2 )
    tk.Label( self.frmGraphs ,
              text='Roll' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=0 , padx=2 )

    #SPIN RATE
    self.Rate = ttk.Progressbar( self.frmGraphs ,
                                orient='vertical' ,
                                length=100 ,
                                mode='determinate' )
    self.Rate.grid( row=0 , column=1 , padx=2 )
    tk.Label( self.frmGraphs ,
              text='Spin Rate' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=1 , padx=2 )

    #GRAPH: PITCH
    self.Pitch = tk.Canvas( self.frmGraphs ,
                              width=100 ,
                              height=100 ,
                              bg='white' )
    self.Pitch.grid( row=0 , column=2 , padx=2 )
    tk.Label( self.frmGraphs ,
              text='Pitch' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=2 , padx=2 )

    #GRAP: BONUS
    self.Bonus = tk.Canvas( self.frmGraphs ,
                              width=100 ,
                              height=100 ,
                              bg='white' )
    self.Bonus.grid( row=0 , column=3 , padx=2 )
    tk.Label( self.frmGraphs ,
              text='Direction' ,
              bg='black' ,
              fg='white' ).grid( row=1 , column=3 , padx=2 )


    """GPS"""
    #FRAME: GRAPHS
    self.frmGPS = tk.Frame( self , bg='black' )
    self.frmGPS.grid( row=3 , column=0 , columnspan=2 )

    #LABEL: GPS
    tk.Label( self.frmGPS ,
              text='GPS ' ,
              bg='black' ,
              fg='white' , 
              font=( 'Helvetica' , 20 , 'bold' ) ).grid( row=0 , column=0 , columnspan=8 )

    #LABEL: TIME
    tk.Label( self.frmGPS ,
              text='Time: ' ,
              bg='black' ,
              fg='white' ,
              font=( 'Helvetica' , 15 ) ).grid( row=1 , column=0 )
    self.GPSTime = tk.Label(  self.frmGPS ,
                              text='00:00:00 [s]' ,
                              bg='black' ,
                              fg='white' ,
                              font=( 'Fixedsys' , 20 ) ,
                              borderwidth=3 ,
                              relief='ridge' )
    self.GPSTime.grid( row=1 , column=1 , columnspan=8 )
    
    #LABEL: LATITUD
    tk.Label( self.frmGPS ,
              text='Lat: ' ,
              bg='black' ,
              fg='white' ,
              font=( 'Helvetica' , 15 ) ).grid( row=2 , column=0 )
    self.GPSLat = tk.Label(  self.frmGPS ,
                              text='0°0\'0\"' ,
                              bg='black' ,
                              fg='white' ,
                              font=( 'Fixedsys' , 20 ) ,
                              borderwidth=3 ,
                              relief='ridge' )
    self.GPSLat.grid( row=2 , column=1 )

    #LABEL: LONGITUD
    tk.Label( self.frmGPS ,
              text='Long: ' ,
              bg='black' ,
              fg='white' ,
              font=( 'Helvetica' , 15 ) ).grid( row=2 , column=2 )
    self.GPSLong = tk.Label(  self.frmGPS ,
                              text='0°0\'0\"' ,
                              bg='black' ,
                              fg='white' ,
                              font=( 'Fixedsys' , 20 ) ,
                              borderwidth=3 ,
                              relief='ridge' )
    self.GPSLong.grid( row=2 , column=3 )

    #LABEL: ALTITUD
    tk.Label( self.frmGPS ,
              text='Alt: ' ,
              bg='black' ,
              fg='white' ,
              font=( 'Helvetica' , 15 ) ).grid( row=2 , column=4 )
    self.GPSAlt = tk.Label(  self.frmGPS ,
                              text='0' ,
                              bg='black' ,
                              fg='white' ,
                              font=( 'Fixedsys' , 20 ) ,
                              borderwidth=3 ,
                              relief='ridge' )
    self.GPSAlt.grid( row=2 , column=5 )

    #LABEL: SATTELLITES
    tk.Label( self.frmGPS ,
              text='Sats: ' ,
              bg='black' ,
              fg='white' ,
              font=( 'Helvetica' , 15 ) ).grid( row=2 , column=6 )
    self.GPSSat = tk.Label(  self.frmGPS ,
                              text='0' ,
                              bg='black' ,
                              fg='white' ,
                              font=( 'Fixedsys' , 20 ) ,
                              borderwidth=3 ,
                              relief='ridge' )
    self.GPSSat.grid( row=2 , column=7 )

    #FILL SCREEN
    self.grid_columnconfigure( 0 , weight=1 )
    self.grid_columnconfigure( 1 , weight=1 )
    self.grid_rowconfigure( 0 , weight=1 )
    self.grid_rowconfigure( 1 , weight=1 )
    self.grid_rowconfigure( 2 , weight=1 )
    self.grid_rowconfigure( 3 , weight=1 )

#MAIN
if __name__ == "__main__":
  window = Window( )
  control( window ).pack( side=tk.LEFT ,
                          fill=tk.Y ,
                          padx=10 ,
                          pady=10 )
  datos( window ).pack( side=tk.LEFT ,
                        fill=tk.BOTH ,
                        expand=1 ,
                        padx=10 ,
                        pady=10 )
  window.mainloop( )