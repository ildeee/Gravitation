import numpy as np 
import matplotlib.pyplot as plt

G = 6.67430e-11
deltaT = 60

def calc_r(x, y):
    return (x**2+y**2)**0.5

def acc_func(x,y):
    '''For acceleration

Arguements :
    x  : float
        position wrt stationery object in x dir
    y  : float
        position wrt stationery object in y dir

Returns :
    ax  : function
        acceleration in x dir
    ay  : float
        acceleration in y dir'''

    rsquare = (x**2  + y**2  )
    r = rsquare ** 0.5
    k  = G * M / rsquare
    a_x = -k * x / r
    a_y = -k * y / r

    return a_x, a_y

def calculate_trajectory(M, R, m, v, Time):
    """
    Calculate gravitational trajectory
    for heavy mass M at origin and
    satellite object of mass m, with distance
    R between them and initial velocity v.

    Arguments :
        M      : float
             Mass of stationery object.        
        R      : float
             Initial distance between both objects.        
        m      : float
             Mass of revolving object.
        v      : float
             Initial velocity.
        Time   : float
             Max time till which values are obtained

    Returns : (dict[str: list]) with keys
        'x'  : x coordinates considering object as origin
        'y'  : y coordinates considering object as origin
        'ti' : time (s)
        'ux' : Velocity in x direction
        'uy' : Velocity in y direction
        'ax' : Acceleration in x direction
        'ay' : Acceleration in y direction
    """

    X =  []
    Y = []
    Ti =[]
    UX = []
    UY = []
    AX = []
    AY = []
    Rad =[]

    x0,y0 = R,0
    ux,uy = 0,v
    ax,ay =acc_func(x0,y0)
    T =0
    r = calc_r(x0, y0)
    
    while T< Time and r > R_earth and r < 20*R:
    
        X.append(x0)
        Y.append(y0)
        r = calc_r(x0, y0)
        Rad.append(r)
    
        UX.append(ux)
        UY.append(uy)
    
        AX.append(ax)
        AY.append(ay)
    
        Ti.append(T)
    
        T+= deltaT
    
        dvx = ax* deltaT
        ux += dvx
    
        dvy =ay*deltaT
        uy +=dvy
    
        dx = ux*deltaT
        x0 += dx
    
        dy = uy* deltaT
        y0 += dy
    
        ax,ay =acc_func(x0,y0)  
        

    return {'x': X,'y': Y,'t': Ti,'ux': UX,'uy': UY, 'ax': AX, 'ay': AY, 'r': Rad}

def plot(traj, string):
    """Plots a gravitational trajectory.

    Arguments :
        traj : (dict) containing trajectory data given by calculate_trajectory()
        string : string
            if string = 'X/Y'
             : distance(x, y)
            if string = 'UX/UY'
             : velocity(ux, uy)
            if string = 'AX/AY'
             : acceleration(ax, ay)
            if string = 'Time'
             : x/time , y/time
            if string = 'all'
             : plots all above graph
    """



    if string == 'X/Y' or string == 'all':
        plt.plot(traj['x'], traj['y'])
        plt.grid()
        plt.title('Distance')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

    if string == 'UX/UY' or string == 'all':
        plt.plot(traj['ux'], traj['uy'])
        plt.grid()
        plt.title('Velocity')
        plt.xlabel('UX')
        plt.ylabel('UY')
        plt.show()

    if string == 'AX/AY' or string == 'all':
        plt.plot(traj['ax'], traj['ay'])
        plt.title('Acceleration')
        plt.xlabel('AX')
        plt.ylabel('AY')
        plt.grid()
        plt.show()

    if string == 'Time' or string == 'all':
        plt.plot(traj['t'], traj['y'])
        plt.title('Y/Time')
        plt.xlabel('Time')
        plt.ylabel('Y')
        plt.plot(traj['t'], traj['x'])
        plt.title('X/Time')
        plt.xlabel('Time')
        plt.ylabel('X')
        plt.grid()
        plt.show()
    

def days2sec(t):
    return t*24*60*60

def months2sec(t):
    return days2sec(30*t)

#Sample -
M = 5.972e+24  # Mass of Earth
R_earth = 6400E3  # Earth radius
R = 3.84400e8
m = 0.07346e24
v = 1.022e+3
Time = days2sec(30.0)
string = 'all'
trajectory = calculate_trajectory(M, R, m, v, Time)
plot(trajectory, string)
