local input = 4
local t, c = 1, 1

repeat
    t = t * c
    c = c + 1
until c > input

io.write (t)
