from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

diamond = 57

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, diamond)
    sleep(0.1)
