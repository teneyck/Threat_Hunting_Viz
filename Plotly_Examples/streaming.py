import json
import os
import numpy as np
import plotly as py
import plotly.plotly as ply
import plotly.tools as tls
import plotly.graph_objs as go
from plotly.graph_objs import *
i = 0
while i < 100:
    os.system('python stream_generate.py')
    new_data = json.load(open("nums.txt"))
    print new_data
    data = Data( [ new_data ] )
    plot_url = ply.plot(data, filename='extend plot', fileopt='extend', auto_open=False)
    i += 1
    # content = f.readlines()
    # content = [x.strip() for x in content]
    # for line in content:
    #     if line is not None:
    #         print line
    #         new_data = ast.literal_eval(line)
    #         print new_data
    #         data = Data( [ new_data ] )
    #         plot_url = ply.plot(data, filename='extend plot', fileopt='extend', auto_open=False)
