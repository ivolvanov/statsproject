import csv

row_list = [["Name", "Red Bull", "Kong strong 1", "Kong strong 2", "Hell", "Monster", "Colossus", "Rienergy", "Burn", "Delhaze Energy drink", "Siti Energy drink(lidl)", 
            "Albanski raj", "Rockstar", "Energy slammer", "Bully", "AH off-brand", "Golden power", "Action off-brand"],
            ["Andrei", 8, 2, 7.5, 4, 2, 7.5, 6, 7.5, 9.5, 6, -1, -1, -1, -1, -1, -1, -1],
            ["Andy", 6, 4.33, 4.5, 5, 2, 3, 5.69, 3.5, 5, 6, -1, -1, -1, -1, -1, -1, -1],
            ["Theo", 8, 6, 6, 7, 5, 8, 5, 4, 4, 7, -1, -1, -1, -1, -1, -1, -1],
            ["Mirna", 8, 4, 8, 7, 3, 5, 6, 7, 8, 6.7, -1, -1, -1, -1, -1, -1, -1],
            ["Vera", 8, 5.1, 6, 5, 1.5, 4.2, 8.3, 5, 9, 9.2, -1, -1, -1, -1, -1, -1, -1],
            ["Dimitar", 5, 6, 8, 8, 9, -1, -1, 3, -1, -1, 7, 5, 4, 5, 8, 3, 4],
            ["Kalo", 6, 3.5, 5, 5, 10, -1, -1, 2.5, -1, -1, 6.5, 5, 7.5, 5, 1, 3, 2],
            ["Sasho", 2.1, 6.9, 7.5, 1, 7, -1, -1, 1, -1, -1, 2, 2.2, 3, 4, 2, 3, 5],
            ["Ivcho", 3.5, 6, 4, 5.5, 9, -1, -1, 1.5, -1, -1, 4, 7, 2.5, 2, 7, 7.5, 1.5],
            ["Marto 2", 2, 6.5, 5, 8, 4, -1, -1, 2.5, -1, -1, 4, 5, 6, 5, 3, 6, 2],
            ["Bobi", 1, 1, 7, 9, 9, -1, -1, 3.2, -1, -1, 1, 6.5, 6, 2, 5, 7, 1],
            ["Marto 1", 1, 2, 7, 4.5, 1, -1, -1, 9, -1, -1, 4, 6, 4, 6, 4, 5, 5],
            ["Ivo", 3, 6.5, 6, 4, 6, -1, -1, 3.5, -1, -1, 4, 5, 2, 5, 6, 6, 2]
            ]

with open('rating_data.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerows(row_list)
