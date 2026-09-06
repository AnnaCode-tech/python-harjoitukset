korkeus=float(input("Anna suorakulmion korkeus senttimetreinä:"))
leveys=float(input("Anna suorakolmion leveys senttimetreinä:"))
ala = korkeus*leveys
piiri=2*korkeus+2*leveys
print(f"Suorkulmion ala on: {ala:6.2f} cm^2")
print(f"Suorakulmion piiri on: {piiri:6.2f} cm")