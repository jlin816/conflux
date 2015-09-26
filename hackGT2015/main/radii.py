def findLocation(points):
    lastDist = float(10000.0)
    minMeasure = distance([points[0],points[1]])/10000
    for i in xrange(20000):
        r = []
        for p in points:
            # print [p[0],p[1],minMeasure*i*p[2]]
            r.append([p[0],p[1],minMeasure*i*p[2]])
        # r1, r2, r3 = minMeasure*i*p1[2],minMeasure*i*p2[2],minMeasure*i*p3[2]
        dist,avgcoord = getMinDistance(r)
        # print dist, avgcoord
        # print avgcoord
        if dist is not None:
            if dist<lastDist:
                lastDist = dist
            else:
                return avgcoord

def intersect(x1,y1,r1,x2,y2,r2):
    d = ((x2-x1)**2.0+(y2-y1)**2.0)
    if d==0:
        return None, None
    d1 = d**0.5
    c = (d1+r1+r2)*(-d1+r1+r1)*(d1-r1+r2)*(d1+r1-r2)
    if c<0:
        return None,None
    K = (0.25)*(c)**0.5
    xa = (0.5)*(x2+x1) + (0.5)*(x2-x1)*(r1**2.0-r2**2.0)/d + 2*(y2-y1)*K/d
    ya = (0.5)*(y2+y1) + (0.5)*(y2-y1)*(r1**2.0-r2**2.0)/d - 2*(x2-x1)*K/d

    xb = (0.5)*(x2+x1) + (0.5)*(x2-x1)*(r1**2.0-r2**2.0)/d - 2*(y2-y1)*K/d
    yb = (0.5)*(y2+y1) + (0.5)*(y2-y1)*(r1**2.0-r2**2.0)/d + 2*(x2-x1)*K/d
    return (xa,ya),(xb,yb)

def getMinDistance(points):
    # p1,p2,p3 = points
    # print len(points)
    minDists = []
    groups = []
    for p in xrange(0,len(points)):
        f = points[p]
        # print p
        for k in points[p:]:
            if k is not f:
            # print f,k
                i,j = intersect(f[0],f[1],f[2], k[0],k[1],k[2])
                # print f,k,':',i,j
                if i==None or j==None:
                    return None,None
                groups.append([i,j])
    xavg = 0.0
    yavg = 0.0
    for groupindex in xrange(len(groups)):
        group = groups[groupindex]
        for g2 in groups[groupindex:]:
            if g2 is not group:
                d1 = distance([group[0],g2[0]])
                d2 = distance([group[0],g2[1]])
                d3 = distance([group[1],g2[0]])
                d4 = distance([group[1],g2[1]])
                minimum = min([d1,d2,d3,d4])
                if minimum==d1:
                    xavg+=group[0][0]
                    # xavg+=g2[0][0]
                    yavg+=group[0][1]
                    # yavg+=g2[0][1]
                elif minimum==d2:
                    xavg+=group[0][0]
                    # xavg+=g2[1][0]
                    yavg+=group[0][1]
                    # yavg+=g2[1][1]
                elif minimum==d3:
                    xavg+=group[1][0]
                    # xavg+=g2[0][0]
                    yavg+=group[1][1]
                    # yavg+=g2[0][1]
                else:
                    xavg+=group[1][0]
                    # xavg+=g2[1][0]
                    yavg+=group[1][1]
                    # yavg+=g2[1][1]
                minDists.append(minimum)
        # print group

        # xavg+=group[0][0]
        # xavg+=group[1][0]
        # yavg+=group[0][1]
        # yavg+=group[1][1]
    
    # print points
    # i1,i2 = intersect(p1[0],p1[1],p1[2],p2[0],p2[1],p2[2])
    # i3,i4 = intersect(p2[0],p2[1],p2[2],p3[0],p3[1],p3[2])
    # i5,i6 = intersect(p3[0],p3[1],p3[2],p1[0],p1[1],p1[2])
    # if None in [i1,i2,i3,i4,i5,i6]:
    #     return None,None
    # # print min(distance([i1,i3]),distance([i1,i4]))
    # v1 = min(min(distance([i1,i3]),distance([i1,i4])), min(distance([i2,i3]),distance([i2,i4])))
    # v2 = min(min(distance([i3,i5]),distance([i3,i6])), min(distance([i4,i5]),distance([i4,i6])))
    # v3 = min(min(distance([i5,i1]),distance([i5,i2])), min(distance([i6,i1]),distance([i6,i2])))
    # print minDists
    length = len(groups)
    # print length
    return sum(minDists)/len(groups), [xavg/length,yavg/length]
def distance(points):
    p1,p2 = points
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
