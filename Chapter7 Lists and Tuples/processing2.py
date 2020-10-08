def main():
    Cities = ['Baidoa', 'Mogadishu', 'Hargeysa', 'Galkacyo']
    file = open('Cities', 'w')
    for city in Cities:
        file.write(city + '\n')
    file.close()

main()
