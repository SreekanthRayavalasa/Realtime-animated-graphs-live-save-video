# Uncomment the next two lines if you want to save the animation

#import matplotlib
#matplotlib.use("Agg")
import numpy
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.animation as animation
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt



# Sent for figure
font = {'size'   : 9}
matplotlib.rc('font', **font)

# Setup figure and subplots
f0 = figure(num = 0, figsize = (12, 8))#, dpi = 100)
f0.suptitle("Moving and scrolling graph", fontsize=12)
ax01 = subplot2grid((2, 2), (0, 0))
ax02 = subplot2grid((2, 2), (0, 1))
ax03 = subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
ax04 = ax03.twinx()
#tight_layout()

# Set titles of subplots
ax01.set_title('Position vs Time')
ax02.set_title('Velocity vs Time')
ax03.set_title('Position and Velocity vs Time')

# set y-limits
ax01.set_ylim(0,10)
ax02.set_ylim(-6,10)
ax03.set_ylim(-0,10)
ax04.set_ylim(-10,10)

# sex x-limits
ax01.set_xlim(0,200)
ax02.set_xlim(0,200)
ax03.set_xlim(0,200)
ax04.set_xlim(0,200)

# Turn on grids
ax01.grid(True)
ax02.grid(True)
ax03.grid(True)

# set label names
ax01.set_xlabel("x")
ax01.set_ylabel("py")
ax02.set_xlabel("t")
ax02.set_ylabel("vy")
ax03.set_xlabel("t")
ax03.set_ylabel("py")
ax04.set_ylabel("vy")

# Data Placeholders
yp1=zeros(0)
yv1=zeros(0)
yp2=zeros(0)
yv2=zeros(0)
t=zeros(0)

# set plots
p011, = ax01.plot(t,yp1,'b-', label="yp1")
p012, = ax01.plot(t,yp2,'g-', label="yp2")

p021, = ax02.plot(t,yv1,'b-', label="yv1")
p022, = ax02.plot(t,yv2,'g-', label="yv2")

p031, = ax03.plot(t,yp1,'b-', label="yp1")
p032, = ax04.plot(t,yv1,'g-', label="yv1")

# set lagends
ax01.legend([p011,p012], [p011.get_label(),p012.get_label()])
ax02.legend([p021,p022], [p021.get_label(),p022.get_label()])
ax03.legend([p031,p032], [p031.get_label(),p032.get_label()])



excel_data_df = pd.read_excel('test.xlsx', sheet_name='test')

# print whole sheet data
print(excel_data_df)

a = np.array(excel_data_df.Year)
b = np.array(excel_data_df.Temperature)

print(a)
print(b)

num = len(a)
print(num)
print(a[0])

plt.xlabel('entry a')
plt.ylabel('entry b')
plt.plot(a,b)

# Data Update
xmin = 0
xmax = 200
x = 0




def updateData(self):
	global x
	global yp1
	global yv1
	global yp2
	global yv2
	global t
	
	
	
	
	

	tmpp1 = b[x]
	tmpv1 = b[x]
	yp1=append(yp1,tmpp1)
	yv1=append(yv1,tmpv1)
	yp2=append(yp2,0.5*tmpp1)
	yv2=append(yv2,0.5*tmpv1)
	t=append(t,a[x])

	x += 1

	p011.set_data(t,yp1)
	p012.set_data(t,yp2)

	p021.set_data(t,yv1)
	p022.set_data(t,yv2)

	p031.set_data(t,yp1)
	p032.set_data(t,yv1)

	if x >= xmax-1.00:
		p011.axes.set_xlim(x-xmax+1.0,x+1.0)
		p021.axes.set_xlim(x-xmax+1.0,x+1.0)
		p031.axes.set_xlim(x-xmax+1.0,x+1.0)
		p032.axes.set_xlim(x-xmax+1.0,x+1.0)

	return p011, p012, p021, p022, p031, p032

# interval: draw new frame every 'interval' ms
# frames: number of frames to draw
simulation = animation.FuncAnimation(f0, updateData, blit=False, frames=5000, interval=1, repeat=False)

# Uncomment the next line if you want to save the animation
#simulation.save(filename='sim.mp4',fps=30,dpi=300)
plt.show()
