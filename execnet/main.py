import execnet
gateway = execnet.makegateway("popen//python=python2.7")
channel = gateway.remote_exec("""
  import numpy as np
  array = np.array([1, 2, 3])
  while 1:
    x = channel.receive()
    if x is None:
      break
    array = np.append(array, x)
  channel.send(repr(array))
""")

for x in range(10):
    channel.send(x)
channel.send(None)
print(channel.receive())