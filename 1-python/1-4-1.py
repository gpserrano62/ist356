import beautiful_date as bd 

today = bd.BeautifulDate.fromisoformat('2024-06-15')

#add two months to the date
today = today + 2 * bd.months

print(today)