import math

trees               = 333
shadedTrees         = 222
sunnyTrees          = 111

shadeOutputMod      = 0.8

sunnyTreeOutput     = 146
shadedTreeOutput    = 116.8

sunnyOutput         = (sunnyTrees * sunnyTreeOutput)
shadedOutput        = (shadedTrees * shadedTreeOutput * shadeOutputMod)
totalOutput         = (sunnyOutput + shadedOutput)

owners              = 4

eatCount            = (totalOutput - math.floor(totalOutput))
sellableOutput      = (totalOutput - eatCount)
cut                 = math.floor(sellableOutput / 4)

print(cut)