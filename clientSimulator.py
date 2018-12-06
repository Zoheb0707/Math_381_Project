import random
import xlwt 
from xlwt import Workbook 

def generateRandomClient():
	x = random.uniform(0,1)
	if (x <= 0.63):
		y = 100000
	elif(0.63 < x <= 0.75): 	
		y = 250000
	elif(0.75 < x <= 0.85):
		y = 500000
	elif(0.85 < x <= 0.92):
		y = 1000000
	elif(0.92 < x <= 0.97):
		y = 1500000
	elif(0.97 < x <= 1):
		y = 2000000
	return y
	
def generateCf2Customer():
	x = random.uniform(0,1)
	if (x <= 1/11):
		cf2Client = 0;
	elif (1/11 < x <= 5/11):
		cf2Client = 1;
	elif (5/11 < x <= 7/11):
		cf2Client = 2;
	elif (7/11 < x <= 10/11):
		cf2Client = 3;
	elif (10/11 < x <= 1):
		cf2Client = 4;
	return cf2Client; 
	
def generateCf1Customer():
	x = random.uniform(0,1)
	if (x <= 14/36):
		cf1Client = 0;
	elif (14/36 < x <= 30/36):
		cf1Client = 1;
	elif (30/36 < x <= 35/36):
		cf1Client = 2;
	elif (35/36 < x <= 1):
		cf1Client = 3;
	return cf1Client;	

def generateAdsCustomer():
    x = random.uniform(0,1)
    if (x <= 3/11):
        adsClient = 0
    elif (3/11 < x <= 8/11):
        adsClient = 1;
    elif (8/11 < x <= 9/11):
        adsClient = 2
    elif (9/11 < x <= 1):
        adsClient = 3;	
    return adsClient

def generateDailyCf1Customer():
    x = random.uniform(0,1)
    if x <= 0.03:
        return 1
    else: 
        return 0

def generateDailyCf2Customer():
    x = random.uniform(0,1)
    if x <= 0.066:
        return 1
    else: 
        return 0
    
def generateDailyAdsCustomer():
    x = random.uniform(0,1)
    if x <= 0.05:
        return 1
    else: 
        return 0

def rainFactory2018(cf1, cf2, ads):
    revenue = 0;
    for i in range(0, cf1):
        type = generateRandomClient()
        revenue = revenue + 50000 + type * 0.05
    
    for i in range(0, cf2):
        type = generateRandomClient()
        revenue = revenue + 25000 + type * 0.1
    
    for i in range(0, ads):
        revenue = revenue + 20000
    
    return revenue 

def simulateYear():
    cf1s = []
    cf2s = []
    adss = []
    rejected = []
    total = 0;
    totalCf1 = 0;
    totalCf2 = 0;
    totalAds = 0;
    revenue = 0
    overload = 0
    
    pm = 4
    es = 1.25
    sn = 3
    dev = 1
    cw = 0.5
    ads = 5
    
    for i in range(0,11):
        cf1 = generateCf1Customer()
        cf2 = generateCf2Customer()
        ads = generateAdsCustomer()
        
        cf1s.append(cf1)
        cf2s.append(cf2)
        adss.append(ads)
    
        totalCf1 = totalCf1 + cf1
        totalCf2 = totalCf2 + cf2
        totalAds = totalAds + ads
        total = totalCf1 + totalCf2 + totalAds
    
        for j in range(0, cf1):
            type = generateRandomClient()
            revenue = revenue + 50000 + 0.05 * type
                
        for j in range(0, cf2):
            type = generateRandomClient()
            revenue = revenue + 25000 + 0.1 * type
                
        for j in range(0, ads):
            revenue = revenue + 25000


    return revenue


def simulateYearByDay():
    cf1s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cf2s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    adss = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    totalCf1 = 0;
    totalCf2 = 0;
    totalAds = 0;
    revenue = 0
    overload = 0
    
    pm = 4
    es = 1.25
    dev = 1
    cw = 0.5
    dsn = 3
    adp = 5
    info = []
	
    availablePm = 4
    availableEs = 1.25 
    availableDev = 1
    availableCw = 0.5
    availableAdp = 5
    availableDsn = 3
    availability = []
    for i in range(4,15):
        for j in range(0, 30):
            cf1 = generateDailyCf1Customer()
            cf2 = generateDailyCf2Customer()
            ads = generateDailyAdsCustomer()
			
            availablePm = 4 - (cf1s[i-1]*(1/6) + cf1s[i-2]*(1/4) + cf1s[i-3]*(1/8) + cf1s[i-4]*(1/8) 
            + cf2s[i-1]*(1/6) + cf2s[i-2]*(1/4) + cf2s[i-3]*(1/8) + cf2s[i-4]*(1/8))
		
            availableEs = 1.25 - (cf1s[i-2]*(1/16) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/10) 
            + cf2s[i-2]*(1/16) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/10))
		
            availableDev = 1 - (cf1s[i-1]*(3/40) + cf1s[i-2]*(1/20) + cf1s[i-3]*(1/10)  
            + cf2s[i-1]*(3/40) + cf2s[i-2]*(1/20) + cf2s[i-3]*(1/10) 
            + adss[i-1]*(1/10))
		
            availableCw = 0.5 - (cf1s[i-1]*(3/40) + cf1s[i-2]*(1/20) 
            + cf2s[i-1]*(3/40) + cf2s[i-2]*(1/20))
		
            availableAdp = 5 - (cf1s[i-1]*(1/10) + cf1s[i-2]*(1/5) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/5) 
            + cf2s[i-1]*(1/10) + cf2s[i-2]*(1/5) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/5)
            + adss[i-1]*(1/5) + adss[i-2]*(1/8) + adss[i-3]*(1/8) + adss[i-4]*(1/8))
		
            availableDsn = 3 - (cf1s[i-1]*(3/20) + cf1s[i-2]*(3/10) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/20) 
            + cf2s[i-1]*(3/20) + cf2s[i-2]*(3/10) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/20) 
            + adss[i-1]*(1/20) + adss[i-2]*(1/40) + adss[i-3]*(1/40) + adss[i-4]*(1/40))

			
            if cf1 == 1:
                if (1/6 <= availablePm and  
					
                    1/16 <= availableEs and  
					
                    1/10 <= availableAdp and 
					
                    3/40 <= availableCw and
					
                    3/40 <= availableDev and 
					
                    3/20 <= availableDsn):
                    cf1s[i] = cf1s[i] + 1
                    type = generateRandomClient()
                    revenue = revenue + 50000 + 0.05 * type
                    totalCf1 = totalCf1 + 1
					
                    availablePm = 4 - (cf1s[i-1]*(1/6) + cf1s[i-2]*(1/4) + cf1s[i-3]*(1/8) + cf1s[i-4]*(1/8) 
                    + cf2s[i-1]*(1/6) + cf2s[i-2]*(1/4) + cf2s[i-3]*(1/8) + cf2s[i-4]*(1/8))
		
                    availableEs = 1.25 - (cf1s[i-2]*(1/16) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/10) 
                    + cf2s[i-2]*(1/16) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/10))
		
                    availableDev = 1 - (cf1s[i-1]*(3/40) + cf1s[i-2]*(1/20) + cf1s[i-3]*(1/10)  
                    + cf2s[i-1]*(3/40) + cf2s[i-2]*(1/20) + cf2s[i-3]*(1/10) 
                    + adss[i-1]*(1/10))
		
                    availableCw = 0.5 - (cf1s[i-1]*(3/40) + cf1s[i-2]*(1/20) 
                    + cf2s[i-1]*(3/40) + cf2s[i-2]*(1/20))
		
                    availableAdp = 5 - (cf1s[i-1]*(1/10) + cf1s[i-2]*(1/5) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/5) 
                    + cf2s[i-1]*(1/10) + cf2s[i-2]*(1/5) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/5)
                    + adss[i-1]*(1/5) + adss[i-2]*(1/8) + adss[i-3]*(1/8) + adss[i-4]*(1/8))
		
                    availableDsn = 3 - (cf1s[i-1]*(3/20) + cf1s[i-2]*(3/10) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/20) 
                    + cf2s[i-1]*(3/20) + cf2s[i-2]*(3/10) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/20) 
                    + adss[i-1]*(1/20) + adss[i-2]*(1/40) + adss[i-3]*(1/40) + adss[i-4]*(1/40))
                else:
                    overload = overload + 1
                    
            if cf2 == 1:
                if (1/6 <= availablePm and  
					
                    1/16 <= availableEs and  
					
                    1/10 <= availableAdp and 
					
                    3/40 <= availableCw and
					
                    3/40 <= availableDev and 
					
                    3/20 <= availableDsn):
                    
                    cf2s[i] = cf2s[i] + 1
                    type = generateRandomClient()
                    revenue = revenue + 25000 + 0.10 * type    
                    totalCf2 = totalCf2 + 1
					
                    availablePm = 4 - (cf1s[i-1]*(1/6) + cf1s[i-2]*(1/4) + cf1s[i-3]*(1/8) + cf1s[i-4]*(1/8) 
                    + cf2s[i-1]*(1/6) + cf2s[i-2]*(1/4) + cf2s[i-3]*(1/8) + cf2s[i-4]*(1/8))
		
                    availableEs = 1.25 - (cf1s[i-2]*(1/16) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/10) 
                    + cf2s[i-2]*(1/16) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/10))
		
                    availableDev = 1 - (cf1s[i-1]*(3/40) + cf1s[i-2]*(1/20) + cf1s[i-3]*(1/10)  
                    + cf2s[i-1]*(3/40) + cf2s[i-2]*(1/20) + cf2s[i-3]*(1/10) 
                    + adss[i-1]*(1/10))
		
                    availableCw = 0.5 - (cf1s[i-1]*(3/40) + cf1s[i-2]*(1/20) 
                    + cf2s[i-1]*(3/40) + cf2s[i-2]*(1/20))
		
                    availableAdp = 5 - (cf1s[i-1]*(1/10) + cf1s[i-2]*(1/5) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/5) 
                    + cf2s[i-1]*(1/10) + cf2s[i-2]*(1/5) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/5)
                    + adss[i-1]*(1/5) + adss[i-2]*(1/8) + adss[i-3]*(1/8) + adss[i-4]*(1/8))
		
                    availableDsn = 3 - (cf1s[i-1]*(3/20) + cf1s[i-2]*(3/10) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/20) 
                    + cf2s[i-1]*(3/20) + cf2s[i-2]*(3/10) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/20) 
                    + adss[i-1]*(1/20) + adss[i-2]*(1/40) + adss[i-3]*(1/40) + adss[i-4]*(1/40))
                else:
                    overload = overload + 1
                
            if ads == 1:
                if (1/5 <= availableAdp and 
					
                    1/10 <= availableDev and 
					
                    1/20 <= availableDsn):
                    
                    adss[i] = adss[i] + 1
                    revenue = revenue + 20000
                    totalAds = totalAds + 1
                    
                    availablePm = 4 - (cf1s[i-1]*(1/6) + cf1s[i-2]*(1/4) + cf1s[i-3]*(1/8) + cf1s[i-4]*(1/8) 
                    + cf2s[i-1]*(1/6) + cf2s[i-2]*(1/4) + cf2s[i-3]*(1/8) + cf2s[i-4]*(1/8))
		
                    availableEs = 1.25 - (cf1s[i-2]*(1/16) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/10) 
                    + cf2s[i-2]*(1/16) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/10))
		
                    availableDev = 1 - (cf1s[i-1]*(3/40) + cf1s[i-2]*(1/20) + cf1s[i-3]*(1/10)  
                    + cf2s[i-1]*(3/40) + cf2s[i-2]*(1/20) + cf2s[i-3]*(1/10) 
                    + adss[i-1]*(1/10))
		
                    availableCw = 0.5 - (cf1s[i-1]*(3/40) + cf1s[i-2]*(1/20) 
                    + cf2s[i-1]*(3/40) + cf2s[i-2]*(1/20))
		
                    availableAdp = 5 - (cf1s[i-1]*(1/10) + cf1s[i-2]*(1/5) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/5) 
                    + cf2s[i-1]*(1/10) + cf2s[i-2]*(1/5) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/5)
                    + adss[i-1]*(1/5) + adss[i-2]*(1/8) + adss[i-3]*(1/8) + adss[i-4]*(1/8))
		
                    availableDsn = 3 - (cf1s[i-1]*(3/20) + cf1s[i-2]*(3/10) + cf1s[i-3]*(1/10) + cf1s[i-4]*(1/20) 
                    + cf2s[i-1]*(3/20) + cf2s[i-2]*(3/10) + cf2s[i-3]*(1/10) + cf2s[i-4]*(1/20) 
                    + adss[i-1]*(1/20) + adss[i-2]*(1/40) + adss[i-3]*(1/40) + adss[i-4]*(1/40))
                else:
                    overload = overload + 1
        
        availability.append([['PM', availablePm],['ES', availableEs], ['Dev', availableDev], ['CW', availableCw], ['ADS', availableAdp], ['DSN', availableDsn]])
              
    info.append(totalCf1)
    info.append(totalCf2)
    info.append(totalAds)
    info.append(overload)
    info.append(revenue)

    return info
	
repeat = 5000
revenue = 0	
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
sheet2 = wb.add_sheet('Sheet 2')
for i in range(0, repeat):
    yearRevenue = rainFactory2018(10,21,16)
    revenue = revenue + yearRevenue
    sheet2.write(i,1,yearRevenue)
print(revenue/repeat)

totalRev = 0

for i in range(0, repeat):
	info = simulateYearByDay()
	sheet1.write(i, 1, info[0])
	sheet1.write(i, 2, info[1])
	sheet1.write(i, 3, info[2])
	sheet1.write(i, 4, info[3])
	sheet1.write(i, 5, info[4])

wb.save('simulation.xls') 	

	
