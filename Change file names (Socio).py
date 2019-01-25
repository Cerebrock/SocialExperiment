import os, re
with open('puntajes.txt', 'r') as p:
    puntajes = p.read().split()
path = r'D:\Matias\Downloads\PsiSoc\Avatares'
os.chdir(path)
files = sorted(os.listdir(path), key = lambda x: (int(re.sub('\D','',x))))
print(files)
for i in range(0, len(puntajes)):
    try:
        os.rename(os.path.join(path, files[i]), puntajes[i] + '.png')
    except:
        os.rename(os.path.join(path, files[i]), puntajes[i] + ' {0}.png'.format(i + 1))