import os,sys
s=0
f=open('results.txt','r')
line=f.readline()
se=0
fe=0
g=0
while line :
    v1=line.strip('\n')
    v=v1.split()
    s+=1
    if s==1:
        pass
    else:
        for i in range(4):
            if i==0:
                if fe==0 :
                    f_garme=v[i]
                    sal_f_garme=v[3]
                    fe+=1
                elif fe==1:
                    f_sard=v[i]
                    sal_f_sard=v[3]
                    fe+=1
                    if int(f_garme)<int(f_sard):
                        temp=f_garme
                        f_garme=f_sard
                        f_sard=temp
                        temp=sal_f_garme
                        sal_f_garme=sal_f_sard
                        sal_f_sard=temp
                else:
                    if int(v[i])>int(f_garme):
                        f_garme=v[i]
                        sal_f=v[3]
                    if int(v[i])<int(f_sard):
                        f_sard=v[i]
                        sal_f_sard=v[3]
            if i==1:
                if se==0 :
                    s_garme=v[i]
                    sal_s_garme=v[3]
                    se+=1
                elif se==1:
                    s_sard=v[i]
                    sal_s_sard=v[3]
                    se+=1
                    if int(s_garme)<int(s_sard):
                        temp=s_garme
                        s_garme=s_sard
                        s_sard=temp
                        temp=sal_s_garme
                        sal_s_garme=sal_s_sard
                        sal_s_sard=temp
                else:
                    if int(v[i])>int(s_garme):
                        s_garme=v[i]
                        sal_s=v[3]
                    if int(v[i])<int(s_sard):
                        s_sard=v[i]
                        sal_s_sard=v[3]
            if i==2:
                if g==0 :
                    g_garme=v[i]
                    sal_g_garme=v[3]
                    g+=1
                elif g==1:
                    g_sard=v[i]
                    sal_g_sard=v[3]
                    g+=1
                    if int(g_garme)<int(g_sard):
                        temp=g_garme
                        g_garme=g_sard
                        g_sard=temp
                        temp=sal_g_garme
                        sal_g_garme=sal_g_sard
                        sal_g_sard=temp
                else:
                    if int(v[i])>int(g_garme):
                        g_garme=v[i]
                        sal_g=v[3]
                    if int(v[i])<int(g_sard):
                        g_sard=v[i]
                        sal_g_sard=v[3]
    line=f.readline()
print('frace => ','garme',sal_f_garme,'sard',sal_f_sard)
print('sewdeen => ','garme',sal_s_garme,'sard',sal_s_sard)
print('germany => ','garme',sal_g_garme,'sard',sal_g_sard)