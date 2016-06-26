#Encoding: utf-8
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mtick
'''
w1=x, w2=Vx, w3=y, w4=Vy		
'''
def f1(t,w1,w2,w3,w4): 	# dx/dt
	return w2
def f2(t,w1,w2,w3,w4): 	# dvx/dt
	fact1 =  w1/( (w1**2 + w3**2)*( 1.+ np.sqrt(w1**2 + w3**2)/a_h )) 
	fact2 = a_h*w1*np.log(1. + np.sqrt(w1**2 + w3**2)/a_h )/( (w1**2 + w3**2)**(3./2.) )
	return  -G*Mb*w1/(w1**2 + w3**2 + b**2)**(3./2.) -G*Md*w1/(w1**2 + w3**2 + a**2)**(3./2.) + (4*np.pi*G*rho*a_h**2)*( fact1 - fact2 )
#	return  -G*Mb*w1/(w1**2 + w3**2 + b**2)**(3./2.) -G*Md*np.sqrt(w1**2 + w3**2)/(np.sqrt(a**2+w1**2+w3**2)*(a+np.sqrt(a**2+w1**2+w3**2))**2 ) + (4*np.pi*G*rho*a_h**2)*( fact1 - fact2 )
def f3(t,w1,w2,w3,w4): 	# dy/dt
	return w4
def f4(t,w1,w2,w3,w4): 	# dvy/dt
	fact3 =  w3/( (w1**2 + w3**2)*(1.+ np.sqrt(w1**2 + w3**2)/a_h )) 
	fact4 = a_h*w3*np.log(1. + np.sqrt(w1**2 + w3**2)/a_h )/( (w1**2 + w3**2)**(3./2.) )
	return  -G*Mb*w3/(w1**2 + w3**2 + b**2)**(3./2.) -G*Md*w3/(w1**2 + w3**2 + a**2)**(3./2.) + (4*np.pi*G*rho*a_h**2)*( fact3 - fact4 )
#	return  -G*Mb*w3/(w1**2 + w3**2 + b**2)**(3./2.) -G*Md*w3/(w1**2 + w3**2 + a**2)**(3./2.) + (4*np.pi*G*rho*a_h**2)*( fact3 - fact4 )


# ====================================
# BULBO
Mb = 1293.  #3e10 Mo 
b  = 1.52 #2.0#5.0#2.7#2.7 		#Parámetro de Plummer
# DISCO
Md = 2155   #5e10 Mo
a  = b/0.2 #5.8#5.81 		#Parametro de Kuzmin
# HALO
a_h = 22.25  		#kpc
rho = .258#.38#.4741379#1.6e-3
# ====================================
# Constantes
G = 1.
ti = 0.
tf = 100.

N = 10001 	# N+1  Precisión del cálculo
h = (tf-ti)/N
t = ti 		#Tiempo inicial
ri = 8.0 	#Radio inicial kpc
m = 4 		#numero de ecuaciones (dos de pos. y dos de vel.)
print 'h = ', h

print 'N = ',N

w1 = np.linspace(0,1,N)
w2 = np.linspace(0,1,N)
w3 = np.linspace(0,1,N)
w4 = np.linspace(0,1,N)
tiempo = np.linspace(0,1,N)


# =====================================

# ======= Ciclo para hacer malla en r ======

grr = np.linspace(0.1,50.,100) 	#Para hacer malla en r.  


# =========== Curva de rot de Velocidad circular para malla ===

	#Las listas tienen nombres diferentes
vbb = []
vdd = []
vhh = []
vpp = []
vee = []
ptot = []
for rr in grr:
	vbb.append( np.sqrt( G*Mb*(rr**2)/ (((rr)**2 + (b)**2 )**(3./2.) ) ) )
	vdd.append( np.sqrt( G*Md*(rr**2)/ (((rr)**2 + (a)**2 )**(3./2.) ) ) )
	vhh.append( np.sqrt( abs( (4*np.pi*G*rho*a_h**3) * ( 1./(a_h + rr) - np.log(1. + rr/a_h)/rr ) ) ) )
	vpp.append( np.sqrt( vdd[-1]**2 + vbb[-1]**2 + vhh[-1]**2) ) 
	pb = -Mb/np.sqrt(rr**2 + b**2)
	pd = -Md/np.sqrt(rr**2 + a**2)
	ph = -(4*np.pi*G*rho*a_h**3)*( np.log(1 + rr/a_h)/(rr) ) 
	ptot.append( pb + pd + ph )
	vee.append( np.sqrt(2*abs( ptot[-1] ) )   )
print 'min = ', min(ptot)
print 'max = ', max(ptot)

plt.plot(grr,vbb,ls='--',color='k',label=r'$\mathrm{Bulge}\  V_{c,b}$')
plt.plot(grr,vdd,ls=':',color='k',label=r'$\mathrm{Disk}\ V_{c,d}$')
plt.plot(grr,vhh,ls='-.',color='k',label=r'$\mathrm{Halo}\ V_{c,h}$')
plt.plot(grr,vpp,ls='-',color='k',label=r'$\mathrm{Total}\ V_{c,T}$')
plt.grid()
plt.legend(loc='upper left')
plt.xlabel(r'$\mathrm{r\ [kpc]}$')
plt.ylabel(r'$\mathrm{ V_c\ [10\ km/s]} $')
plt.ylim(0,33)

fig2 = plt.axes([0.65, 0.68, .23, .2])
plt.plot(grr,vee,ls='--',color='k',label=r'$V_{e}$')

plt.plot(grr,vpp,ls='-',color='k',label=r'$V_{c,T}$')
plt.xlim(0,30)

plt.xlabel(r'$\mathrm{r\ [kpc]}$')
plt.ylabel(r'$\mathrm{ V_e\ [10\ km/s]} $')

plt.show()

# ================= Inicia metodo Runge Kutta 4 =========================
#gr = np.linspace(0.1,50.,100) 	#Para hacer malla en r. Descomentar para Poincare 

#lis = [3,6,9,12,15,21,25,32,38,45,53,60]
#fig, axes = plt.subplots(4, 3, figsize=(10,10), sharex=False)
#for q, ax in enumerate(axes.flat): # axes is a 2D array.. Need to flat it to run over every ax


gr = [ri] 						#Para una sola órbita. Comentar para Poincare		

for ri in gr:

	# ======= Velocidades Circulares ========
	vb = np.sqrt( G*Mb*(ri**2)/ (((ri)**2 + (b)**2 )**(3./2.) ) )
	vd = np.sqrt( G*Md*(ri**2)/ (((ri)**2 + (a)**2 )**(3./2.) ) )
	vh = np.sqrt( abs( (4*np.pi*G*rho*a_h**3) * ( 1./(a_h + ri) - np.log(1. + ri/a_h)/ri ) )  )
	vt = np.sqrt( vd**2 + vb**2 + vh**2)

	print 'vb = ',vb
	print 'vd = ', vd
	print 'vh = ', vh
	print 'vt = ',vt

	# ======= Cond. iniciales =========
	tiempo[0] = ti
	w1[0]  = ri 	#x
	w2[0]  = 0. 	#Vx
	w3[0]  = 0.		#y
	w4[0]  = vt  	#Vy   Escribir vt si se quiere la velocidad circular. Escribir números diferentes

	caso = 'B' 		# Definir el caso que se trata
	u= 1./2.
	print '--------------------------------'
	print '|xi     Vxi    yi     Vyi |'
	print '|{}    {}    {}    {} |'.format(w1[0],w2[0],w3[0],w4[0])
	print '--------------------------------'
	for i in range(N-1): 	#4
		#5
		k1_1 = h * f1(t,w1[i],w2[i],w3[i],w4[i])
		k1_2 = h * f2(t,w1[i],w2[i],w3[i],w4[i])
		k1_3 = h * f3(t,w1[i],w2[i],w3[i],w4[i])
		k1_4 = h * f4(t,w1[i],w2[i],w3[i],w4[i])
		#6
		k2_1 = h * f1(t+h/2.,w1[i]+u*k1_1,w2[i]+u*k1_2,w3[i]+u*k1_3,w4[i]+u*k1_4)
		k2_2 = h * f2(t+h/2.,w1[i]+u*k1_1,w2[i]+u*k1_2,w3[i]+u*k1_3,w4[i]+u*k1_4)
		k2_3 = h * f3(t+h/2.,w1[i]+u*k1_1,w2[i]+u*k1_2,w3[i]+u*k1_3,w4[i]+u*k1_4)
		k2_4 = h * f4(t+h/2.,w1[i]+u*k1_1,w2[i]+u*k1_2,w3[i]+u*k1_3,w4[i]+u*k1_4)
		#7
		k3_1 = h * f1(t+h/2.,w1[i]+u*k2_1,w2[i]+u*k2_2,w3[i]+u*k2_3,w4[i]+u*k2_4)
		k3_2 = h * f2(t+h/2.,w1[i]+u*k2_1,w2[i]+u*k2_2,w3[i]+u*k2_3,w4[i]+u*k2_4)
		k3_3 = h * f3(t+h/2.,w1[i]+u*k2_1,w2[i]+u*k2_2,w3[i]+u*k2_3,w4[i]+u*k2_4)
		k3_4 = h * f4(t+h/2.,w1[i]+u*k2_1,w2[i]+u*k2_2,w3[i]+u*k2_3,w4[i]+u*k2_4)
		#8
		k4_1 = h * f1(t+h,w1[i]+k3_1,w2[i]+k3_2,w3[i]+k3_3,w4[i]+k3_4)
		k4_2 = h * f2(t+h,w1[i]+k3_1,w2[i]+k3_2,w3[i]+k3_3,w4[i]+k3_4)
		k4_3 = h * f3(t+h,w1[i]+k3_1,w2[i]+k3_2,w3[i]+k3_3,w4[i]+k3_4)
		k4_4 = h * f4(t+h,w1[i]+k3_1,w2[i]+k3_2,w3[i]+k3_3,w4[i]+k3_4)
		#9
		w1[i+1] = w1[i] + (k1_1 + 2.*k2_1 + 2.*k3_1 + k4_1)/6.
		w2[i+1] = w2[i] + (k1_2 + 2.*k2_2 + 2.*k3_2 + k4_2)/6.
		w3[i+1] = w3[i] + (k1_3 + 2.*k2_3 + 2.*k3_3 + k4_3)/6.
		w4[i+1] = w4[i] + (k1_4 + 2.*k2_4 + 2.*k3_4 + k4_4)/6.

		tiempo[i+1] = t
		#10
		t = ti + i*h



# ======= Plot de órbitas =========
	
	plt.subplot(111, axisbg='black')
	plt.scatter(w1,w3,alpha=0.1,color='white',label=r'$ V_{} = {}\ km/s$'.format('{iy}',np.round(10*w4[0],3) ),  )
#	plt.plot(tiempo,w1,alpha=0.5,label=r'V_i={}'.format(w4[0])) 	#No descomentar
#	plt.plot(tiempo,w3,alpha=0.5,label=r'V_i={}'.format(w4[0])) 	#No descomentar
	plt.scatter(w1[0],w3[0],color='#00CC00', alpha=1)
	plt.scatter(w1[-1],w3[-1],color='red')
	plt.scatter(0,0,marker='*',s=50,color='orange')
	plt.xlabel('X [kpc]')
	plt.ylabel('Y [kpc]')
#	plt.axis('off')
	#plt.title('Case {}'.format(caso))
	plt.legend()
	plt.grid()
	plt.show()


	'''	
	# == Guardar órbitas =======
	
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())
	figure = plt.gcf()
	figure.set_size_inches(8.47,8.47)		#antes de salvar imagen
	plt.savefig('./rayos2.png',dpi=200) 	#Salva imagen
	plt.clf()
	plt.show()
	'''	
# =================== Energías =========
	
	Ec = np.linspace(0,1,N)
	Epb = np.linspace(0,1,N)
	Epd = np.linspace(0,1,N)
	Eph = np.linspace(0,1,N)
	Et = np.linspace(0,1,N)

	for q in range(len(tiempo)):
		
		Ec[q] = 0.5*(w2[q]**2 + w4[q]**2) 
		Epb[q] = -G*Mb/np.sqrt(w1[q]**2 + w3[q]**2 +b**2  )
		Epd[q] = -G*Md/np.sqrt(w1[q]**2 + w3[q]**2 +a**2  )
		Eph[q] = (-4*np.pi*G*rho*a_h**3)*np.log(1.+ np.sqrt(w1[q]**2 + w3[q]**2)/a_h )/np.sqrt(w1[q]**2 + w3[q]**2)

		Et[q] = Ec[q] + Epb[q] + Epd[q] + Eph[q]

	print 'Et_i = ',Et[0]
	print 'Et_f = ',Et[-1]
	DE = (Et[0] - Et[-1])/Et[0] 
	print 'DE = {}'.format( DE )

	plt.plot(tiempo,Ec,ls='-',dashes=[8, 4, 2, 4, 2, 4],color='k',label='Kinetic energy')
	plt.plot(tiempo,Epb,ls=':',color='k',label='Potential energy (Bulge)')
	plt.plot(tiempo,Epd,ls='--',color='k',label='Potential energy (Disk)')
	plt.plot(tiempo,Eph,ls='-.',color='k',label='Potential energy (Halo)')
	plt.plot(tiempo,Et,ls='-',color='k', label='Total energy')
	plt.xlabel(r'$\mathrm{Time\ [10^8\ yrs]}$')
	plt.ylabel(r'$\mathrm{Energy\ [(10\ km/s)^2]}$')
	plt.text(13, max(Et)+300, r'$ \Delta E =\ {}$'.format(DE), size= 20,color = 'red'  )
	plt.xlim(0,30)
	plt.legend(loc='upper right') #Descomentar solo para caso A
	plt.title('Case {}'.format(caso))
	plt.show()
	


# ============= Plot de potenciales ======
	
	X = np.linspace(-20,20,250)
	Y = np.linspace(-20,20,250)


	#for x in range(len(X)):
	#	for y in range(len(Y)):
	def pot(X,Y):
		halo = (-4*np.pi*G*rho*a_h**3)*np.log(1.+ np.sqrt(X**2 + Y**2)/a_h )/np.sqrt(X**2 + Y**2)
		bulbo = -G*Mb/np.sqrt(X**2 + Y**2 +b**2  ) 
		disco = -G*Md/np.sqrt(X**2 + Y**2 +a**2  )
		return bulbo + disco + halo

	for i in range(len(X)):
		po = plt.scatter([X[i]]*len(Y),Y, c= pot(X[i],Y) ,vmin=min(ptot),vmax=max(ptot), edgecolor='none', alpha=1);
	plt.colorbar(po).set_label('Potential Intensity', rotation=270, labelpad=-70, y=0.5)
	plt.arrow(8, 0, 0, 3, head_width=0.5, head_length=0.5, fc='k', ec='k')
	plt.xlabel('X [kpc]')
	plt.ylabel('Y [kpc]')
	plt.tight_layout()
	plt.show()
	
	# ===== Momento angular =========
	
	L = np.linspace(0,1,N)
	for p in range(len(tiempo)):
		L[p] = w1[p]*w4[p] - w3[p]*w2[p]
	
	print '=== Mom Ang. ==='
	print 'L_i = ',L[0]
	print 'L_f = ',L[-1]
	DL = (L[0] - L[-1])/L[0]
	print 'DL = {}'.format( DL )
	plt.plot(tiempo, L)
	plt.xlim(0,30)
	plt.ylabel(r'$\mathrm{Angular\ Momentum\ [10\ kpc\ km /s]}$')
	plt.xlabel(r'$\mathrm{Time\ [10^8\ yrs]}$')
	plt.text(13,max(L)-.5*(max(L)-min(L)), r'$ \Delta L =\ {}$'.format(DL), size= 20,color = 'red' )
	plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	plt.ylim(min(L), max(L))
	plt.title('Case {}'.format(caso))
	plt.show()
	

	
	# ===== Diagrama de Poincaré =====
	#Recomendable correrlo en computadora rápida, y comentar todas las subrutinas 
	#anteriores que arrojan figuras
'''
	xPon = []
	VxPon = []

	for u in range(len(w3)):
		if (abs(w3[u]) <= 0.005 ):
			xPon.append( abs(w1[u]) )
			VxPon.append( abs(w2[u]) )

	sc = plt.scatter(xPon, VxPon, c=[ri]*len(xPon),vmin=min(gr),vmax=max(gr), edgecolor='none', alpha=0.5); # Sizes and colors depend on valyues of other variables

#==== Método de punto fijo  ===============
# para encontrar radio al cual se encuentra una velocidad
# circular dada.

rs =  5. 	#Valor semilla en r para diag de poncaire
vcp =  20 #w4[0] #20.	 	#Velocidad Circular Propuesta
flag = True
while flag == True:
	g1 = abs( 1./(a_h*(1.+ rs/a_h) ) - np.log( 1.+ rs/a_h)/rs )
	g2 = Mb/(( rs**2 + b**2)**(3./2.) ) + Md/(( rs**2 + a**2)**(3./2.) )
	rsa = rs
	rs = np.sqrt( (vcp**2 -  (4.*np.pi*G*rho*a_h**3)*g1  )/(G*g2 )  )
	
	if (abs(rs - rsa) <=0.00001 ):
		print 'rs = ',rs
		flag = False

# ======
#plt.scatter(xPon,VxPon,color='red',alpha=0.7)  #Para plot de una partícula
plt.xlabel(r'$\mathrm{ X\ [kpc]}$')
plt.ylabel(r'$\mathrm{V_{x}\ [10\ km/s]}$')
plt.colorbar(sc).set_label('Initial radius', rotation=270, labelpad=-45, y=0.7)
plt.axvline(x=rs, color='k', ls='--',label=r'$R_C = {}\ kpc $'.format(np.round(rs,3) )) # linea que indica el radio al cual ocurre la velocidad circular dada
plt.text(30,10, r'$V_c = {}\ km/s$'.format(np.round(10*w4[0],2) ) ,size= 20,color = 'red')
#plt.tight_layout()
plt.legend()
plt.title('Case {}'.format(caso))
plt.show()
'''

#mng = plt.get_current_fig_manager()
#mng.resize(*mng.window.maxsize())
#figure = plt.gcf()
#figure.set_size_inches(11.47,8.47)		#antes de salvar imagen
#plt.savefig('./Diag_Poinc{}.png'.format(caso))#,dpi=200) 	#Salva imagen




