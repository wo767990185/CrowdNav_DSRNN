import visdom
#使用visdom前需启动 python -m visdom.server
import numpy as np
vis = visdom.Visdom()
vis.text("nyyyao")
vis.image(np.ones((3,10,10)))