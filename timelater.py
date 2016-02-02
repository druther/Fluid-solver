''' Fluid equation for time>0 '''


from timestart import *
import pdb;pdb.set_trace()
print 'tempA:'
print tempA

def gauss_siedel_2(num, arr):
  count,test = 0,0
  while count<4:
    for i in range(1,sizeX-1):
      for j in range(1,sizeY-1):
#      import pdb;pdb.set_trace()
        if not checker[i][j]:
          if num == 1:
            val = ktb1*tempB[i,j] + ktb2*(tempW12[i,j] + tempB2[i-1,j]) + ktb3*(tempW22[i,j] + tempB2[i-1,j]) + ktb4*(tempB2[i-1,j]) + ktb5*(tempB2[i+1,j]+tempB2[i-1,j])
          elif num == 2:
            val = ktw11*tempW1 + ktw12*(tempA2[i,j] + tempA2[i,j-1]) + ktw13*(tempB2[i,j] + tempB2[i-1,j]) + ktw14*(tempW12[i+1,j] + tempW12[i-1,j]) + ktw15*(tempW12[i,j-1] + tempW12[i,j+1])
          elif num == 3:
            val = ktw21*tempW2 + ktw22*(tempB2[i,j] + tempB2[i-1,j]) + ktw23*(tempC2[i,j] + tempC2[i,j-1]) + ktw25*(tempW22[i+1,j] + tempW22[i-1,j]) + ktw26*(tempW22[i,j-1] + tempW22[i,j+1])
          elif num == 4:
            val = kta1*tempA + kta2*tempW12[i,j] + kta3*tempA2[i,j-1] + kta4*(tempA2[i,j+1] + tempA2[i,j-1])
          elif num == 5:
            val = ktc1*tempC + ktc2*tempW22[i,j] + ktc3*tempC2[i-1,j] + ktc4*(tempC2[i+1,j] + tempC2[i-1,j])

          if abs(val-arr[i,j])>error:
            arr[i,j] = val
            test = 1
          else:
            checker[i][j] = True
            count+=1

  reset()
  print arr,num
  if test:
    return True
  return False


for i in range(timesteps):
  print 'Calculating for time :'+str(i)
  tempA2 = np.zeros(shape=(sizeX,sizeY))
  tempB2 = np.zeros(shape=(sizeX,sizeY))
  tempC2 = np.zeros(shape=(sizeX,sizeY))
  tempW12 = np.zeros(shape=(sizeX,sizeY))
  tempW22 = np.zeros(shape=(sizeX,sizeY))

# Getting initial input over fluid B

  for j in range(sizeY):
    tempB2[0,j] = 1         # For constant input

  seq = [(1,tempB2),(2,tempW12),(3,tempW22),(4,tempA2),(5,tempC2)]
  counter = 0
  while seq:
    pai = seq.pop(0)
    counter+=1
    print counter
    if gauss_siedel_2(pai[0], pai[1]):
      seq.append(pai)

  tempA = np.copy(tempA2)
  tempB = np.copy(tempB2)
  tempC = np.copy(tempC2)
  tempW1 = np.copy(tempW12)
  tempW2 = np.copy(tempW22)  

print 'FINAL VALUE\n'
print 'Temperature of Fluid B'
print tempB
print 'Temperature of Wall 1'
print tempW1
print 'Temperature of Wall 2'
print tempW2
print 'Temperature of Fluid A'
print tempA
print 'Temperature of Fluid C'
print tempC
