def main():
    m = int(input("ente the mass: "))
    print(energy(m))

def energy(mass):
    E = mass * (3*10**8)*(3*10**8)
    return E

main()