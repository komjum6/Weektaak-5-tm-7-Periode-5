
# coding: utf-8

# Vergelijken van excelsheets om dezelfde eiwitten tegen te komen in verschillende eiwitten

# Eerst worden de bestanden gelezen (KR, DD, mpk3, mpk6)

# In[2]:

import pandas as pd
KR = pd.ExcelFile("D:\Bio-Infmap\KR.xlsx")
print(KR.sheet_names)
df_kr = KR.parse("all detected proteins")
df_kr.head()


# In[38]:

DD = pd.ExcelFile("D:\Bio-Infmap\DD.xlsx")
print(DD.sheet_names)
df_dd = DD.parse("all detected proteins")
df_dd.head()


# In[39]:

mpk3 = pd.ExcelFile("D:\Bio-Infmap\mpk3.xlsx")
print(mpk3.sheet_names)
df_mpk3 = mpk3.parse("all detected proteins")
df_mpk3.head()


# In[40]:

mpk6 = pd.ExcelFile("D:\Bio-Infmap\mpk6.xlsx")
print(mpk6.sheet_names)
df_mpk6 = mpk6.parse("all detected proteins")
df_mpk6.head()


# Vind alle dezelfde eiwitten door te zoeken naar overeenkomende accessiecodes

# In[30]:




# In[49]:

import re

Excellijst = [df_kr,df_dd,df_mpk3,df_mpk6]
Excellijstnamen = ['df_kr','df_dd','df_mpk3','df_mpk6']
y = 0

for x in Excellijst:
    string = ""
    for ding in str(x):
        string = string + ding
    #print(string)
    regex = r'([A-Z]\w+\.[1234])'
    pattern = re.compile(regex) 
    accessiecodes = re.findall(pattern, string)
    print('Dit is de', Excellijstnamen[y], 'lijst' ,accessiecodes)
    y += 1
    #print(string) deze later weghalen

#print(df_kr[2:])



# Wat is ['RPL2.1', 'ATPDX1.1', 'PDX1.1'] hierboven op het eind van df_mpk6 en ATPM24.1 in df_mpk3? -Deze zijn eruit gegooit (de regex was niet perfect)

# In[69]:

#Ik ga even wat aangepaste lijsten gebruiken
df_kr_eiwitten = ['ATCG00490.1', 'AT2G07732.1', 'ATMG00280.1', 'AT4G33010.1', 'AT4G33010.2', 'AT5G17920.1', 'AT2G43800.1', 'AT5G20980.1', 'AT2G26080.1', 'AT4G29060.1', 'AT4G29060.2', 'AT4G37930.1', 'AT5G26780.1', 'AT5G25980.2', 'AT5G25980.1', 'AT4G24280.1', 'AT3G29320.1', 'AT2G05710.1', 'AT3G52930.1', 'AT3G26650.1', 'AT2G36530.1', 'AT4G24620.1', 'AT4G24620.2', 'AT1G66200.1', 'AT1G66200.2', 'AT1G66200.3', 'AT1G79920.1', 'AT1G79930.1', 'AT3G08590.1', 'AT3G04120.1', 'AT3G46970.1', 'AT3G09840.1', 'AT3G53230.1', 'AT2G24200.1', 'AT2G24200.3', 'AT3G09820.1', 'AT3G09820.2', 'AT3G52880.1', 'AT1G57720.1', 'AT1G09780.1', 'AT4G20850.1', 'AT4G21280.1', 'AT4G21280.2', 'AT1G16080.1', 'AT3G15450.1', 'AT3G05180.1', 'AT3G10020.1', 'AT2G46440.1', 'AT5G49070.1', 'AT1G57980.1', 'AT2G43590.1', 'AT5G08380.1', 'AT5G15050.1', 'AT1G79790.1', 'AT3G01440.1', 'AT5G52960.1', 'AT5G16760.1', 'AT5G64250.1', 'AT2G37470.1', 'AT1G07790.1', 'AT3G53650.1', 'AT5G24400.1', 'AT2G41430.1', 'AT2G35410.1', 'AT5G15970.1', 'AT4G28300.1', 'AT1G11660.1', 'AT5G20250.4', 'AT5G20250.1', 'AT2G25070.1', 'AT5G21100.1', 'AT1G15930.1', 'AT1G15750.1', 'AT1G36320.1', 'AT1G49975.1', 'AT5G16840.1', 'AT1G53520.1'] 
df_dd_eiwitten = ['AT1G66700.1', 'AT1G66690.1', 'AT1G66700.3', 'AT2G45220.1', 'AT4G02300.1', 'AT5G20830.1', 'AT5G63680.1', 'AT5G17990.1', 'AT2G02010.1', 'AT2G02000.1', 'AT3G24503.1', 'AT5G48540.1', 'AT5G38900.1', 'AT4G30530.1', 'AT4G30550.1', 'AT1G67980.1', 'AT1G67980.2', 'AT2G04400.1', 'AT2G29350.3', 'AT2G29350.1', 'AT5G54500.1', 'AT5G54500.2', 'AT2G21620.1', 'AT2G21620.2', 'AT5G20960.1', 'AT5G56350.1', 'AT4G26390.1', 'AT1G74590.1', 'AT1G26390.1', 'AT2G34810.1', 'AT5G39050.1', 'AT1G10700.1', 'AT5G05730.1', 'AT2G29690.1', 'AT5G05730.2', 'AT1G02930.1', 'AT1G18070.1', 'AT5G40760.1', 'AT2G24200.1', 'AT2G24200.3', 'AT3G13790.1', 'AT3G13790.2', 'AT3G02360.1', 'AT1G09130.3', 'AT1G09130.1', 'AT4G14100.1', 'AT1G63940.1', 'AT1G63940.2', 'AT1G63940.3', 'AT1G63940.4', 'AT5G07460.1', 'AT3G01120.1', 'AT4G05523.1', 'AT1G11860.1', 'AT5G58720.1', 'AT3G28720.1', 'AT1G10370.1', 'AT1G12520.1', 'AT1G12520.3', 'AT5G35790.1', 'AT3G10060.1', 'AT3G52300.1', 'AT4G25100.1', 'AT4G25100.4', 'AT4G37930.1', 'AT3G13920.1', 'AT3G13920.2', 'AT2G05920.1', 'AT1G16210.1', 'AT5G53380.1', 'AT5G18100.1', 'AT1G78060.1', 'AT2G20860.1', 'AT2G42530.1', 'AT4G21280.1', 'AT4G21280.2', 'AT5G55280.1', 'AT4G28490.1', 'AT5G02960.1', 'AT3G09680.1', 'AT3G15690.2', 'AT3G15690.1', 'AT1G01080.1', 'AT1G01080.2']
df_mpk3_eiwitten = ['AT1G02930.1', 'AT5G48540.1', 'AT1G24190.1', 'AT5G38900.1', 'AT5G54500.1', 'AT5G54500.2', 'AT1G65970.1', 'AT1G60740.1', 'AT5G17990.1', 'AT4G02520.1', 'AT2G02930.1', 'AT5G39050.1', 'AT1G02920.1', 'AT1G23730.1', 'AT2G43590.1', 'AT2G04400.1', 'AT3G54640.1', 'AT2G24200.1', 'AT2G24200.3', 'AT4G36380.1', 'AT4G37910.1', 'AT2G43570.1', 'AT5G54810.1', 'AT5G11670.1', 'AT2G19900.1', 'AT2G01250.1', 'AT2G01250.2', 'AT1G21130.1', 'AT1G21130.2', 'AT2G02010.1', 'AT2G02000.1', 'AT5G17330.1', 'AT3G24503.1', 'AT3G14990.1', 'AT3G14990.2', 'AT5G59420.1', 'AT3G09300.1', 'AT3G16530.1', 'AT2G37760.1', 'AT2G37760.3', 'AT4G38510.1', 'AT1G06000.1', 'AT2G17265.1', 'AT4G28706.1', 'AT2G19730.1', 'AT4G29410.1', 'AT1G66100.1', 'AT1G49980.1', 'AT4G15210.1', 'AT4G15210.2', 'AT1G20620.1', 'AT1G20620.2', 'AT1G20620.4', 'AT3G19130.1', 'AT3G18890.1', 'AT3G11940.1', 'AT2G37270.1', 'AT4G33640.1', 'AT4G19410.1', 'AT4G19410.2', 'AT4G00620.1', 'AT1G79720.1', 'AT1G07700.1', 'AT1G07700.3', 'AT3G11510.1', 'AT3G52580.1', 'AT2G37190.1', 'AT3G53430.1', 'AT5G60670.1', 'AT4G25100.1', 'AT4G25100.4', 'AT3G53740.1', 'AT2G37600.1', 'AT3G45140.1', 'AT5G63380.1', 'AT5G38480.1', 'AT5G38480.2', 'AT5G58250.1', 'AT5G03350.1', 'AT2G42910.1', 'AT4G30870.1', 'AT2G42130.3', 'AT4G27000.1']
df_mpk6_eiwitten = ['AT5G17870.1', 'ATCG00830.1', 'AT2G38230.1', 'AT2G38210.1', 'AT3G16050.1', 'AT4G39800.1', 'AT2G22240.1', 'AT3G13460.1', 'AT3G13460.3', 'AT3G13460.4', 'AT5G61020.1', 'ATCG00780.1', 'AT1G02930.1', 'AT5G13510.1', 'AT3G24503.1', 'AT1G02920.1', 'AT2G43030.1', 'AT5G49030.3', 'AT5G49030.2', 'ATCG01120.1', 'ATCG00660.1', 'AT4G34620.1', 'AT2G05710.1', 'AT1G05190.1', 'AT1G05010.1', 'AT1G69740.1', 'AT1G44318.1', 'AT3G48560.1', 'AT3G26740.1', 'AT3G51160.1', 'AT5G66280.1', 'AT1G74970.1', 'AT3G56910.1', 'AT3G09840.1', 'AT3G53230.1', 'AT5G13650.1', 'AT5G20720.1', 'AT1G37130.1', 'AT3G12930.1', 'AT1G54630.1', 'AT1G70890.1', 'AT1G70410.1', 'AT1G23730.1', 'AT2G42810.1', 'AT2G42810.2', 'AT1G05560.1', 'AT2G20890.1', 'AT3G20970.1', 'AT3G20970.2', 'AT2G45300.1', 'AT3G07310.1', 'AT1G12050.1', 'AT3G11710.1', 'AT5G03350.1', 'AT3G58990.1', 'AT4G00620.1', 'AT4G00600.1', 'AT4G34120.1', 'AT1G27385.2', 'AT1G27385.1', 'AT1G27385.4', 'AT1G54580.1', 'AT3G51000.1', 'AT3G10520.1', 'AT5G63570.1', 'AT5G65010.2', 'AT3G47340.1', 'AT5G10240.2', 'AT5G65010.1', 'AT1G74990.1', 'AT3G05180.1', 'AT1G13320.1', 'AT1G48850.1', 'AT1G48850.2', 'AT3G55040.1', 'AT3G47560.2', 'AT3G47590.1', 'AT3G47100.1', 'AT4G13360.1']

#f = lambda i: i in [df_dd_eiwitten,df_mpk3_eiwitten,df_mpk6_eiwitten]
#new_lijst = list(filter(f, df_kr_eiwitten))
#print(new_lijst)

Concensusproteoom = [c for c in df_kr_eiwitten if c in df_dd_eiwitten or df_mpk3_eiwitten or df_mpk6_eiwitten]

print("Dit is een lijst met het Concensusproteoom" ,Concensusproteoom)

print("\nHier is het in een lijstje")
for d in Concensusproteoom:
    print(d)
    
print("\nNu komen de unieke eiwitten")

Uniek_kr = [c for c in df_kr_eiwitten if c not in df_dd_eiwitten or df_mpk3_eiwitten or df_mpk6_eiwitten]
Uniek_dd = [c for c in df_dd_eiwitten if c not in df_kr_eiwitten or df_mpk3_eiwitten or df_mpk6_eiwitten]
Uniek_mpk3 = [c for c in df_mpk3_eiwitten if c not in df_dd_eiwitten or df_kr_eiwitten or df_mpk6_eiwitten]
Uniek_mpk6 = [c for c in df_mpk6_eiwitten if c not in df_dd_eiwitten or df_mpk3_eiwitten or df_kr_eiwitten]

print("Dit is uniek_kr")
for e in Uniek_kr:
    print(e)
print("Dit is uniek_dd")
for f in Uniek_dd:
    print(f)
print("Dit is uniek_mpk3")
for g in Uniek_mpk3:
    print(g)
print("Dit is uniek_mpk6")
for h in Uniek_mpk6:
    print(h)


# In[6]:

data = pd.ExcelFile("D:\Bio-Infmap\data-tabel.xlsx")
print(data.sheet_names)
df_data = data.parse("Sample overzicht")
df_data.head()


# In[ ]:



