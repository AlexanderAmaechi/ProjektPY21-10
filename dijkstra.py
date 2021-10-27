
while len(unvisited) > 0:
    count += 1

    n = unvisited.removeminimum()

    u = n.value
    upos = u.Position
    uposindex = upos[0] * width + upos[1]

    if distances[uposindex] == infinity:
        break

    if upos == endpos:
        completed = True
        break

    for v in u.Neighbours:
        if v != None:
            vpos = v.Position
            vposindex = vpos[0] * width + vpos[1]

            if not visited[vposindex]:
                d = abs(vpos[0] - upos[0]) + abs(vpos[1] - upos[1])

                newdistance = distances[uposindex] + d

                if newdistance < distances[vposindex]:
                    vnode = nodeindex[vposindex]

                    if vnode == None:
                        vnode = FibHeap.Node(newdistance, v)
                        unvisited.insert(vnode)
                        nodeindex[vposindex] = vnode
                        distances[vposindex] = newdistance
                        prev[vposindex] = u

                    else:
                        unvisited.decreasekey(vnode, newdistance)
                        distances[vposindex] = newdistance
                        prev[vposindex] = u