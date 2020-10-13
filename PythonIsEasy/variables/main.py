import datetime


def perc_of_total(duration, total):
    return round(duration / total * 100, 2)


"""
Taylor Swift Songs
Album: Taylor Swift
"""
artist = "Taylor Swift"
album = artist
release_date = datetime.date(2006, 10, 24)
writer_tay = "Taylor Swift"
writer_tay_rose = "Taylor Swift, Rose"
total_ab1 = 2428

print(f"""--------------------------------
Artist: {artist}
Album: {album}
Release Date: {release_date}
________________________________
""")

title = "Tim McGraw"
duration = 234
percoftotal = perc_of_total(duration, total_ab1)

print(f"""
1. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay}
   % of Total: {percoftotal}%
""")

title = "Picture to Burn"
duration = 174
writer = "Taylor Swift, Rose"
percoftotal = perc_of_total(duration, total_ab1)

print(f"""
2. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay_rose}
   % of Total: {percoftotal}%
""")

title = "Teardrops on My Guitar"
duration = 235
percoftotal = perc_of_total(duration, total_ab1)

print(f"""
3. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay_rose}
   % of Total: {percoftotal}%
""")

title = "A Place in This World"
duration = 202
percoftotal = perc_of_total(duration, total_ab1)

print(f"""
4. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay_rose}
   % of Total: {percoftotal}%
""")

title = "Cold as You"
duration = 241
percoftotal = perc_of_total(duration, total_ab1)

print(f"""
5. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay_rose}
   % of Total: {percoftotal}%
""")

title = "Stay Beautiful"
duration = 238
percoftotal = perc_of_total(duration, total_ab1)

print(f"""
6. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay_rose}
   % of Total: {percoftotal}%
""")

"""
Taylor Swift Songs
Album: Folklore
"""
artist = "Taylor Swift"
album = "Folklore"
release_date = datetime.date(2020, 6, 24)
writer_tay_aaron = "Taylor Swift, Aaron Dessner"
writer_tay_will = "Taylor Swift, William Bowery"
writer_tay_will_just = "Taylor Swift, William Bowery, Justin Vernon"
global total_ab2
total_ab2 = 3809

print(f"""--------------------------------
Artist: {artist}
Album: {album}
Release Date: {release_date}
________________________________
""")

title = "Peace"
duration = 220
percoftotal = perc_of_total(duration, total_ab2)

print(f"""
7. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay_aaron}
   % of Total: {percoftotal}%
""")

title = "My Tears Ricochet"
duration = 255
percoftotal = perc_of_total(duration, total_ab2)

print(f"""
8. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay_aaron}
   % of Total: {percoftotal}%
""")

title = "Seven"
duration = 208
percoftotal = perc_of_total(duration, total_ab2)

print(f"""
9. Title: {title}
   Duration: {duration} seconds
   Writer: {writer_tay_aaron}
   % of Total: {percoftotal}%
""")

title = "Betty"
duration = 294
percoftotal = perc_of_total(duration, total_ab2)

print(f"""
10. Title: {title}
    Duration: {duration} seconds
    Writer: {writer_tay_will}
    % of Total: {percoftotal}%
""")

title = "Hoax"
duration = 220
percoftotal = perc_of_total(duration, total_ab2)

print(f"""
11. Title: {title}
    Duration: {duration} seconds
    Writer: {writer_tay_aaron}
    % of Total: {percoftotal}%
""")

title = "Exile"
duration = 285
percoftotal = perc_of_total(duration, total_ab2)

print(f"""
11. Title: {title}
    Duration: {duration} seconds
    Writer: {writer_tay_will_just}
    % of Total: {percoftotal}%
""")
