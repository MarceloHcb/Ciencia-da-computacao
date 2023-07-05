env = open('.env', mode="w")

env.write("DEBUG=True\n")
print("done!")
env.close()