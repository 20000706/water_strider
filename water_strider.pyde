import string

def setup():
    size(1000, 1000, P3D)
    
r = 0 #rotate
R = 0 #radius
M = 0 #weight
L = 0 #length
F = 0 #fall_down
Q = 'int(random(2))'
C = ['#FF0000', '#FF9900', '#FFFF00', '#00FF00', '#0099FF', '#6600FF']
CN = 0
theta = 0

population = []

for i in range(5):
    g = int(random(0, 6)) # weight_of_body => (a - f) : (lighter - heavier)
    c1 = string.ascii_letters[g]
    g = int(random(6, 12)) # length_of_legs => (g - l) : (shorter - longer)
    c2 = string.ascii_letters[g]
    g = int(random(12, 18))# amount_of_bristles => (m - r) : (more(red) - less(purple))
    c3 = string.ascii_letters[g]
    population.append(c1+c2+c3)

print('initial population', population)

scores = []

def fitness_function():
    
    for dna in population:
        score = 1
        if dna[0] == 'a':
            score += 1
        if dna[1] == 'l':
            score += 1
        if dna[2] == 'm':
            score += 1
            
        scores.append(score)

    for p, s in zip(population, scores):
        print('fitness score', p, s)
        
selection_pool = [] 

def selection():
    for p, s in zip(population, scores):
        for i in range(int(s)):
            selection_pool.append(p)
            
    print('selection pool', selection_pool) 
    
    parent1 = selection_pool[int(random(0, len(selection_pool)))]
    parent2 = selection_pool[int(random(0, len(selection_pool)))]
    return [parent1, parent2]

fitness_function()
parents = selection()

print('parents', parents)

P1 = list(parents[0])
P2 = list(parents[1])
G1 = [P1[0], P2[0]]
G2 = [P1[1], P2[1]]
G3 = [P1[2], P2[2]]

O1 = G1[int(random(2))]
O2 = G2[int(random(2))]
O3 = G3[int(random(2))]
offspring = [O1, O2, O3]
print('offspring', O1+O2+O3)
RN = Q
    
def draw():
    global r, R, M, L, F, C, CN, RN, theta, offspring
    background(0)
    lights()
    
    R = 80
    M = 4 + ord(offspring[0]) - 97
    L = 16 * (ord(offspring[1]) - 100)
    
    if offspring[2] == 'm':
        Color = C[0]
        CN = 1
    if offspring[2] == 'n':
        Color = C[1]
        CN = 2
    if offspring[2] == 'o':
        Color = C[2]
        CN = 3
    if offspring[2] == 'p':
        Color = C[3]
        CN = 4
    if offspring[2] == 'q':
        Color = C[4]
        CN = 5
    if offspring[2] == 'r':
        Color = C[5]
        CN = 6
        
    x = cos(theta)/6
    y = sin(theta)/6
    
    if M > 7:
        if L < R:
            F +=200 and F <= 500
        if L >= R and L< 112:
            if RN == 1:
                if CN <= 2:
                    F = 0
                if CN > 2:
                    F +=100 and F <= 500
            if RN == 0:
                F = 0
        if L >112:
            F = 0
            
    if M == 7:
        if L < R:
            F +=200 and F <= 500
            
        if L >= R and L< 112:
            if RN == 1:
                if CN <= 4:
                    F = 0
                if CN > 4:
                    F +=100 and F <= 500
            if RN == 0:
                F = 0
        if L >= 112:
            F = 0
            
    
    if M < 7:
        if L < R:
            F +=200 and F <= 500
        if L == R:    
            if RN == 1:
                if CN <= 5:
                    F = 0
                if CN == 6:
                    F +=100 and F <= 500
            if RN == 0:
                F = 0
        if L > R:
            F = 0
        
    
    #water
    pushMatrix()
    stroke(255, 255, 255, 100)
    noFill()
    #line(0,350+R, 0,1000, 350+R, 0)
    beginShape()
    vertex(0,350+R)
    bezierVertex(75, 340+R+y*200, 175, 360+R, 250, 350+R)
    endShape()
    beginShape()
    vertex(250,350+R)
    bezierVertex(325, 340+R, 425, 360+R+x*100, 500, 350+R)
    endShape()
    beginShape()
    vertex(500,350+R)
    bezierVertex(575, 320+R+y*100, 675, 360+R, 750, 350+R)
    endShape()
    beginShape()
    vertex(750,350+R)
    bezierVertex(825, 340+R, 925, 360+R+x*200, 1000, 350+R)
    endShape()
    popMatrix()

    translate(500, 350)
    rotateZ(PI)
    rotateX(PI/10)
    rotateY(r)
    theta += 0.05
    
    #water_strider    
    pushMatrix()
    translate(0, y*50-F)
    
    #body
    pushMatrix()
    fill('#FFFFFF')
    stroke(Color)
    strokeWeight(10)
    sphereDetail(M)
    sphere(R)
    popMatrix()
    
    #middle leg
    pushMatrix()
    rotate(y)
    line(R/2, 0, R/2, R, 0, R*3/2)
    line(R, 0, R*3/2, R*3/2, -L, R*2)
    popMatrix()
    pushMatrix()
    rotate(x)
    line(-R/2, 0, R/2, -R, 0, R*3/2)
    line(-R, 0, R*3/2, -R*3/2, -L, R*2)
    popMatrix()
    #hind leg
    pushMatrix()
    rotate(-y)
    line(R/2, 0, -R/2, R, 0, -R*3/2)
    line(R, 0, -R*3/2, R*3/2, -L, -R*2)
    popMatrix()
    pushMatrix()
    rotate(-x)
    line(-R/2, 0, -R/2, -R, 0, -R*3/2)
    line(-R, 0, -R*3/2, -R*3/2, -L, -R*2)
    popMatrix()
    
    popMatrix()
    
    r += 0.005
    
    
    
