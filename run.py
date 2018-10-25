import ptvsd
# Allow other computers to attach to ptvsd at this IP address and port.
ptvsd.enable_attach(address=('0.0.0.0', 3000), redirect_output=False)
# Pause the program until a remote debugger is attached
ptvsd.wait_for_attach()

print("I can run:")

for i in range(5):
    print(i)

print("done.")