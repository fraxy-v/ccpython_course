from clock_angle import Hour, Minute, clock_angle

assert clock_angle(Hour(-1), Minute(0)) == None
assert clock_angle(Hour(25), Minute(0)) == None
assert clock_angle(Hour(2), Minute(60)) == None
assert clock_angle(Hour(2), Minute(-1)) == None
assert clock_angle(Hour(0), Minute(0)) == 0
assert clock_angle(Hour(12), Minute(0)) == 0
assert clock_angle(Hour(24), Minute(0)) == 0
assert clock_angle(Hour(6), Minute(0)) == 180
assert clock_angle(Hour(18), Minute(0)) == 180
assert clock_angle(Hour(18), Minute(30)) == 15
assert clock_angle(Hour(4), Minute(22)) == 1
assert clock_angle(Hour(17), Minute(56)) == 158
assert clock_angle(Hour(9), Minute(6)) == 123

print("Test success.")
