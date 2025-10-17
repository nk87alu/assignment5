from datetime import datetime
import math

def SolveKepler(M, e):
    E = M
    for i in range(100):
        E = M + e * math.sin(E)
    return E

def GetTrueAnomaly(E, e):
    return 2 * math.atan(math.sqrt((1 + e) / (1 - e)) * math.tan(E / 2))

#Mars
Periapsis1 = datetime(2007, 6, 1, 7, 20)
Observation1 = datetime(1672, 8, 6)
TimeDiff1 = (Observation1 - Periapsis1).total_seconds() / 86400
M1 = 2 * math.pi * (TimeDiff1 / 687)
E1 = SolveKepler(M1, 0.0934)
Nu1 = GetTrueAnomaly(E1, 0.0934)
print(f"Mars true anomaly: {math.degrees(Nu1)}°")

Periapsis2 = datetime(2024, 12, 3)
Observation2 = datetime(2025, 4, 20)
TimeDiff2 = (Observation2 - Periapsis2).total_seconds() / 86400
M2 = 2 * math.pi * (TimeDiff2 / 1343)
E2 = SolveKepler(M2, 0.1876)
Nu2 = GetTrueAnomaly(E2, 0.1876)
print(f"Asteroid true anomaly: {math.degrees(Nu2)}°")
