file_size = int(input("Set File size: "))
connection = int(input("Set connection speed: "))
downloaded = connection
seconds = 1
percents = 0
for file in range(connection,file_size):
        percents = round(downloaded / file_size*100)
        print(seconds, 'sec', '.Downloaded', downloaded, 'from', file_size, 'MB','(',percents,'%)')
        downloaded += connection
        seconds += 1
        if downloaded >= file_size:
            print(seconds, 'sec', '.Downloaded', file_size, 'from', file_size, 'MB','(',100,'%)')
            break


#
