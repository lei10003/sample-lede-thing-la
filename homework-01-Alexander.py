# # Ligea Alexander
# # 06-06-2023
# # Homework 1

# #year_of_birth = input("When is your birth year (YYYY)?")
# #print(year_of_birth)
# #current_year = 2023

# # for year in year_of_birth:
# #     if int(year_of_birth) < current_year: 
# #         current_year - int(year_of_birth)
# #     elif int(input("Error: Year cannot be greater than current year \n Come on now, tell us what year you were born.")) < current_year:
# #         print(current_year - year_of_birth)


# # (transparency) Yes I asked chatGPT when the above garbage wouldn't work. I kept getting TypeError: 'int' object is not iterable

current_year = 2023
while True:
    year_of_birth = int(input("When is your birth year (YYYY)?"))
    if year_of_birth > current_year:
        print("The year you entered is in the future. Please try again.")
    else:
        break

current_age = current_year - int(year_of_birth)

avg_annual_hb = ((80 * 60)*24) * 365 #not accounting for leap years 
avg_annual_hb_whale = ((10 * 60)*24) * 365
human_lifetime_heartbeats = avg_annual_hb * current_age
whale_lifetime_heartbeats = avg_annual_hb_whale * current_age
avg_annual_hb_rabbit = ((220 * 60)*24) * 365
rabbit_lifetime_heartbeats = avg_annual_hb_rabbit * current_age
venus_year_in_earth_years = 0.615
age_on_venus = current_age / venus_year_in_earth_years
neptune_year_in_earth_years = 164.79
age_on_neptune = current_age / neptune_year_in_earth_years
older_younger = current_age - int(year_of_birth)
print(f"Did you know your heart has beaten approximately {int(human_lifetime_heartbeats)} times since you were born?")
print(f"And a blue whales' heart has beat approximately {int(whale_lifetime_heartbeats)} times")
print(f"And my goodness, a rabbits' heart has beat {int(rabbit_lifetime_heartbeats)} times")
print(f"And if you were on Venus today, you'd be {age_on_venus:.0f} Venus years old")
print(f"And if you were on Neptune today, you'd be {age_on_venus:.0f} Neputune years old")
ligea_age = 32

if current_age > ligea_age:
    print(f"And it seems like you're older than me by {int(current_age - ligea_age)} years!")
elif current_age < ligea_age:
    print(f"And it seems like you're younger than me by {int(current_age - ligea_age)} years!")
else:
    print(f"And we're the same age!")

if year_of_birth % 2 == 0:
    print(f"And it seems like you were born in an even year, you're even keeled ")
else:
    print(f"And it seems like you were born in an odd year, you oddball ;)")

#Democratic presidents since birth will populate
# every president listed URL:https://www.theguardian.com/news/datablog/2012/oct/15/us-presidents-listed

if year_of_birth > 1960 and year_of_birth < 1963:
    print(f"There's been one Democratic president since you've been born.")
elif year_of_birth > 1963 and year_of_birth < 1968:
    print(f"There's been two Democratic presidents since you've been born.")
elif year_of_birth >1968 and year_of_birth < 1980:
    print(f"There's been three Democratic presidents since you've been born.")
elif year_of_birth >1980 and year_of_birth < 2000:
    print(f"There's been four Democratic presidents since you've been born.")
elif year_of_birth >2000 and year_of_birth < 2013:
    print(f"There's been five Democratic presidents since you've been born.")
elif year_of_birth > 2013 and year_of_birth < current_year:
    print(f"There's been four Democratic presidents since you've been born.")

# presidents = {
#     1960: "Dwight D. Eisenhower",
#     1961: "John F. Kennedy",
#     1963: "Lyndon B. Johnson",
#     1969: "Richard Nixon",
#     1974: "Gerarld Ford", 
#     1977: "Jimmy Carter",
#     1981: "Ronald Reagan",
#     1989: "George Bush",
#     1993: "Bill Clinton",
#     2001: "George W. Bush",
#     2009: "Barack Obama",
#     2016: "Fart Face",
#     2020: "Joe Biden"
# }

# if year_of_birth >= 1960 and year_of_birth in presidents:
#     president = presidents[year_of_birth]
#     print(f"The U.S. President in {year_of_birth} was {president} ")
# else:
#     print(f"No U.S. President information available for the given year.")

presidents = {
    "Dwight D. Eisenhower": (1953, 1961),
    "John F. Kennedy": (1961, 1963),
    "Lyndon B. Johnson": (1963, 1969),
    "Richard Nixon": (1969, 1974),
    "Gerarld Ford" : (1974, 1977),
    "Jimmy Carter" : (1977, 1981),
    "Ronald Reagan" : (1981, 1989),
    "George Bush" : (1989, 1993), 
    "Bill Clinton" : (1993, 2001), 
    "George W. Bush" : (2001, 2009), 
    "Barack Obama" : (2009, 2016), 
    "Fart Face" : (2016, 2020), 
    "Joe Biden" : (2020, 2023)
}

presidents_in_office = []

for president, years in presidents.items():
    start_year, end_year = years
    if start_year <= year_of_birth < end_year:
        presidents_in_office.append(president)

if presidents_in_office:
    print("The US President(s) in", year_of_birth, "were:", ", ".join(presidents_in_office))
else:
    print("No US President information available for the given year.")