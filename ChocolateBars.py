chocolate = 18

num_bars = chocolate // 5

num_squares = ((chocolate % 5) * 7) // 5

extra_squares = ((chocolate % 5) * 7) % 5

print("Each person will recieve {} bars of chocolate".format(num_bars))
print("Each person will recieve {} squares of chocolate".format(num_squares))

#Changes the context of the last print message so it makes sense no matter what the 'extra_squares' value is
plural = "s"
if extra_squares == 1:
    plural = ""

print("There will be {} square{} of chocolate remaining".format(extra_squares, plural))
