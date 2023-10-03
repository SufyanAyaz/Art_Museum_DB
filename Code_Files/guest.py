import mysql.connector


def guest_view():
    username = "guest"
    password = None

    cnx = mysql.connector.connect(

        user=username,
        password=password,
        host="127.0.0.1",
        port=3306)

    cursor = cnx.cursor()
    cursor.execute("use artmuseum")

    print("Welcome to our art museum! Please select which one of the following you would like to browse:\n")

    print("1. Art Pieces")
    print("2. Art Exhibitions")
    print("3. Art Collections")
    print("4. Artists")
    print("5. I Would Like To Leave")

    choice = int(input("Please enter the number of your choice here: "))

    while (choice != 5):
        if (choice == 1):
            query = ''
            print("What type of Art Pieces would you like to explore: ")

            print("1. Paintings")
            print("2. Statues and Sculptures")
            print("3. Other")
            print("4. All of Them")

            art_type = int(
                input("Enter the number of your selected art piece(s) here: "))

            if (art_type == 1):
                query += 'SELECT  '

                all_info = input(
                    "Do you want all the information on paintings? Enter Y or N: ")
                if (all_info == 'Y') or (all == 'y'):
                    query += '* FROM PAINTING AS P '
                else:
                    list_attributes = []
                    id = input(
                        "Do you want to see the ids of the paintings? Enter Y or N: ")
                    if (id == 'Y') or (id == 'y'):
                        list_attributes.append('P.Id_no')
                    paint = input(
                        "Do you want to see the paint type of the paintings? Enter Y or N: ")
                    if (paint == 'Y') or (paint == 'y'):
                        list_attributes.append('P.Paint_Type')
                    style = input(
                        "Do you want to see the styles of the paintings? Enter Y or N: ")
                    if (style == 'Y') or (style == 'y'):
                        list_attributes.append('P.Style')
                    draw = input(
                        "Do you want to see the material the paintings are drawn on? Enter Y or N: ")
                    if (draw == 'Y') or (draw == 'y'):
                        list_attributes.append('P.Material_Drawn_On')
                    query += (', '.join(list_attributes)) + \
                        ' FROM PAINTING AS P '

                specifics = input(
                    "Are you looking for a specific painting? Enter Y or N: ")
                if (specifics == 'N') or (specifics == 'n'):
                    query += ';'
                else:
                    where_conditions = []
                    is_spec_id = input(
                        "Are you looking for a painting with a specific id? Enter Y or N: ")
                    if (is_spec_id == 'Y') or (is_spec_id == 'y'):
                        spec_id = 'P.Id_no = "' + \
                            input("Enter the id number you are looking for: ") + '"'
                        where_conditions.append(spec_id)
                    is_spec_type = input(
                        "Are you looking for a painting with a specific type? Enter Y or N: ")
                    if (is_spec_type == 'Y') or (is_spec_type == 'y'):
                        spec_type = 'P.Painting_Type = "' + \
                            input("Enter the type you are looking for: ") + '"'
                        where_conditions.append(spec_type)
                    is_spec_style = input(
                        "Are you looking for a painting with a specific style? Enter Y or N: ")
                    if (is_spec_style == 'Y') or (is_spec_style == 'y'):
                        spec_style = 'P.Style = "' + \
                            input("Enter the style you are looking for: ") + '"'
                        where_conditions.append(spec_style)
                    is_spec_material = input(
                        "Are you looking for a painting drawn with a specific material? Enter Y or N: ")
                    if (is_spec_material == 'Y') or (is_spec_material == 'y'):
                        spec_material = 'P.Material_Drawn_On = "' + \
                            input("Enter the material you are looking for: ") + '"'
                        where_conditions.append(spec_material)
                    query += ' WHERE ' + (' AND '.join(where_conditions)) + ';'

            elif (art_type == 2):
                query += 'SELECT '

                all_info = input(
                    "Do you want all the information on sculptures and statues? Enter Y or N: ")
                if (all_info == 'Y') or (all == 'y'):
                    query += '* FROM SCULPTED AS S '
                else:
                    list_attributes = []
                    id = input(
                        "Do you want to see the ids of the sculptures and statues? Enter Y or N: ")
                    if (id == 'Y') or (id == 'y'):
                        list_attributes.append('S.Id_no')
                    type = input(
                        "Do you want to see whether the object is a painting or sculpture? Enter Y or N: ")
                    if (type == 'Y') or (type == 'y'):
                        list_attributes.append('S.is_Sculpture, S.is_statue')
                    style = input(
                        "Do you want to see the styles of the sculptures and statues? Enter Y or N: ")
                    if (style == 'Y') or (style == 'y'):
                        list_attributes.append('S.Style')
                    material = input(
                        "Do you want to see the material the sculptures or statues are made on? Enter Y or N: ")
                    if (material == 'Y') or (material == 'y'):
                        list_attributes.append('S.Material')
                    height = input(
                        "Do you want to see the heights of the sculptures and statues? Enter Y or N: ")
                    if (height == 'Y') or (height == 'y'):
                        list_attributes.append('S.Height')
                    weight = input(
                        "Do you want to see the wights of the sculptures and statues? Enter Y or N: ")
                    if (weight == 'Y') or (weight == 'y'):
                        list_attributes.append('S.Weight')
                    query += (', '.join(list_attributes)) + \
                        ' FROM SCULPTED AS S '

                specifics = input(
                    "Are you looking for a specific sculpture or statue? Enter Y or N: ")
                if (specifics == 'N') or (specifics == 'n'):
                    query += ';'
                else:
                    where_conditions = []
                    is_spec_id = input(
                        "Are you looking for a sculpture or statue with a specific id? Enter Y or N: ")
                    if (is_spec_id == 'Y') or (is_spec_id == 'y'):
                        spec_id = 'S.Id_no = "' + \
                            input("Enter the id number you are looking for: ") + '"'
                        where_conditions.append(spec_id)
                    is_spec_sculp = input(
                        "Are you looking for only scultpures? Enter Y or N: ")
                    if (is_spec_sculp == 'Y') or (is_spec_sculp == 'y'):
                        spec_sculp = 'S.is_Sculpture = "True"'
                        where_conditions.append(spec_sculp)
                    is_spec_stat = input(
                        "Are you looking for only statues? Enter Y or N: ")
                    if (is_spec_stat == 'Y') or (is_spec_stat == 'y'):
                        spec_stat = 'S.is_statue = "True"'
                        where_conditions.append(spec_stat)
                    is_spec_style = input(
                        "Are you looking for a sculpted item with a specific style? Enter Y or N: ")
                    if (is_spec_style == 'Y') or (is_spec_style == 'y'):
                        spec_style = 'S.Style = "' + \
                            input("Enter the style you are looking for: ") + '"'
                        where_conditions.append(spec_style)
                    is_spec_material = input(
                        "Are you looking for a item sculpted with a specific material? Enter Y or N: ")
                    if (is_spec_material == 'Y') or (is_spec_material == 'y'):
                        spec_material = 'S.Material = "' + \
                            input("Enter the material you are looking for: ") + '"'
                        where_conditions.append(spec_material)
                    is_spec_height = input(
                        "Are you looking for a specific height? Enter Y or N: ")
                    if (is_spec_height == 'Y') or (is_spec_height == 'y'):
                        spec_height = 'S.Height = "' + \
                            input("Enter the height you are looking for: ") + '"'
                        where_conditions.append(spec_height)
                    is_spec_weight = input(
                        "Are you looking for a specific weight? Enter Y or N: ")
                    if (is_spec_weight == 'Y') or (is_spec_weight == 'y'):
                        spec_weight = 'S.Weight = "' + \
                            input("Enter the weight you are looking for: ") + '"'
                        where_conditions.append(spec_weight)
                    query += ' WHERE ' + (' AND '.join(where_conditions)) + ';'

            elif (art_type == 3):
                query += 'SELECT '

                all_info = input(
                    "Do you want all the information on other pieces? Enter Y or N: ")
                if (all_info == 'Y') or (all == 'y'):
                    query += '* FROM OTHER AS O '
                else:
                    list_attributes = []
                    id = input(
                        "Do you want to see the ids of the other pieces? Enter Y or N: ")
                    if (id == 'Y') or (id == 'y'):
                        list_attributes.append('O.Id_no')
                    type = input(
                        "Do you want to see the types of the other pieces? Enter Y or N: ")
                    if (type == 'Y') or (type == 'y'):
                        list_attributes.append('O.Type')
                    style = input(
                        "Do you want to see the styles of the other pieces? Enter Y or N: ")
                    if (style == 'Y') or (style == 'y'):
                        list_attributes.append('O.Style')
                    query += (', '.join(list_attributes)) + \
                        ' FROM OTHER AS O '

                specifics = input(
                    "Are you looking for something specific from the other pieces? Enter Y or N: ")
                if (specifics == 'N') or (specifics == 'n'):
                    query += ';'
                else:
                    where_conditions = []
                    is_spec_id = input(
                        "Are you looking for a piece with a specific id? Enter Y or N: ")
                    if (is_spec_id == 'Y') or (is_spec_id == 'y'):
                        spec_id = 'O.Id_no = "' + \
                            input("Enter the id number you are looking for: ") + '"'
                        where_conditions.append(spec_id)
                    is_spec_type = input(
                        "Are you looking for a piece with a specific type? Enter Y or N: ")
                    if (is_spec_type == 'Y') or (is_spec_type == 'y'):
                        spec_type = 'O.Type = "' + \
                            input("Enter the type you are looking for: ") + '"'
                        where_conditions.append(spec_type)
                    is_spec_style = input(
                        "Are you looking for a piece with a specific style? Enter Y or N: ")
                    if (is_spec_style == 'Y') or (is_spec_style == 'y'):
                        spec_style = 'O.Style = "' + \
                            input("Enter the style you are looking for: ") + '"'
                        where_conditions.append(spec_style)
                    query += ' WHERE ' + (' AND '.join(where_conditions)) + ';'

            elif (art_type == 4):
                query += 'SELECT '

                all_info = input(
                    "Do you want all the information on all the art items? Enter Y or N: ")
                if (all_info == 'Y') or (all == 'y'):
                    query += '* FROM ART_OBJECTS AS AO '
                else:
                    list_attributes = []
                    id = input(
                        "Do you want to see the ids of the art items? Enter Y or N: ")
                    if (id == 'Y') or (id == 'y'):
                        list_attributes.append('AO.Id_no')
                    year = input(
                        "Do you want to see what year the item was made? Enter Y or N: ")
                    if (year == 'Y') or (year == 'y'):
                        list_attributes.append('AO.year')
                    title = input(
                        "Do you want to see the title of the items? Enter Y or N: ")
                    if (title == 'Y') or (title == 'y'):
                        list_attributes.append('AO.Title')
                    description = input(
                        "Do you want to see the description of the item? Enter Y or N: ")
                    if (description == 'Y') or (description == 'y'):
                        list_attributes.append('AO.Description')
                    origin = input(
                        "Do you want to see the originating country/culture of the item? Enter Y or N: ")
                    if (origin == 'Y') or (origin == 'y'):
                        list_attributes.append('AO.Origin_Country_Culture')
                    epoch = input(
                        "Do you want to see the epoch of the items? Enter Y or N: ")
                    if (epoch == 'Y') or (epoch == 'y'):
                        list_attributes.append('AO.Epoch')
                    artist = input(
                        "Do you want to see the artist who made the items? Enter Y or N: ")
                    if (artist == 'Y') or (artist == 'y'):
                        list_attributes.append('AO.Artist')
                    query += (', '.join(list_attributes)) + \
                        ' FROM ART_OBJECTS AS AO '

                specifics = input(
                    "Are you looking for a specific art items? Enter Y or N: ")
                if (specifics == 'N') or (specifics == 'n'):
                    query += ';'
                else:
                    where_conditions = []
                    is_spec_id = input(
                        "Are you looking for an item with a specific id? Enter Y or N: ")
                    if (is_spec_id == 'Y') or (is_spec_id == 'y'):
                        spec_id = 'AO.Id_no = "' + \
                            input("Enter the id number you are looking for: ") + '"'
                        where_conditions.append(spec_id)
                    is_spec_year = input(
                        "Are you looking for an item made in a specific year? Enter Y or N: ")
                    if (is_spec_year == 'Y') or (is_spec_year == 'y'):
                        spec_year = 'AO.year = "' + \
                            input("Enter the year you are looking for: ") + '"'
                        where_conditions.append(spec_year)
                    is_spec_title = input(
                        "Are you looking for an item with a specific title? Enter Y or N: ")
                    if (is_spec_title == 'Y') or (is_spec_title == 'y'):
                        spec_title = 'AO.Title = "' + \
                            input("Enter the title you are looking for: ") + '"'
                        where_conditions.append(spec_title)
                    is_spec_origin = input(
                        "Are you looking for a item originating somewhere specific? Enter Y or N: ")
                    if (is_spec_origin == 'Y') or (is_spec_origin == 'y'):
                        spec_origin = 'AO.Origin_Country_Culture = "' + \
                            input(
                                "Enter the originating country/culture you are looking for: ") + '"'
                        where_conditions.append(spec_origin)
                    is_spec_epoch = input(
                        "Are you looking for items with a specific epoch? Enter Y or N: ")
                    if (is_spec_epoch == 'Y') or (is_spec_epoch == 'y'):
                        spec_epoch = 'AO.Epoch = "' + \
                            input("Enter the epoch you are looking for: ") + '"'
                        where_conditions.append(spec_epoch)
                    is_spec_artist = input(
                        "Are you looking for an item from a specific artist? Enter Y or N: ")
                    if (is_spec_artist == 'Y') or (is_spec_artist == 'y'):
                        spec_artist = 'AO.Artist = "' + \
                            input("Enter the artist you are looking for: ") + '"'
                        where_conditions.append(spec_artist)
                    query += ' WHERE ' + (' AND '.join(where_conditions)) + ';'

            try:
                cursor.execute(f'{query}')

                attribute_names = cursor.column_names
                attributes_size = len(attribute_names)

                for i in range(attributes_size):
                    print(f'{attribute_names[i]:<25}', end='')
                print()
                print((attributes_size * 25) * '-')

                information = cursor.fetchall()
                information_size = len(information)

                for j in range(information_size):
                    for k in range(len(information[j])):
                        string = str(information[j][k])
                        print(f'{string:<25}', end='')
                    print()

                print(
                    "What would you like to do next! Please select another of the following you would like to browse:\n")

                print("1. Art Pieces")
                print("2. Art Exhibitions")
                print("3. Art Collections")
                print("4. Artists")
                print("5. I Would Like To Leave")

                choice = int(
                    input("Please enter the number of your next choice here: "))
            except:

                print(
                    "What would you like to do next! Please select another of the following you would like to browse:\n")

                print("1. Art Pieces")
                print("2. Art Exhibitions")
                print("3. Art Collections")
                print("4. Artists")
                print("5. I Would Like To Leave")

                choice = int(
                    input("Please enter the number of your next choice here: "))

            print("What would you like to do next! Please select another of the following you would like to browse:\n")

            print("1. Art Pieces")
            print("2. Art Exhibitions")
            print("3. Art Collections")
            print("4. Artists")
            print("5. I Would Like To Leave")

            choice = int(
                input("Please enter the number of your next choice here: "))

        elif (choice == 2):
            query = ''
            query += 'SELECT '

            all_info = input(
                "Do you want all the information on exhibits? Enter Y or N: ")
            if (all_info == 'Y') or (all == 'y'):
                query += '* FROM EXHIBIT AS E '
            else:
                list_attributes = []
                name = input(
                    "Do you want to see the name of the exhibits? Enter Y or N: ")
                if (name == 'Y') or (name == 'y'):
                    list_attributes.append('E.Name')
                start = input(
                    "Do you want to see when the exhibits start? Enter Y or N: ")
                if (start == 'Y') or (start == 'y'):
                    list_attributes.append('E.Start_Date')
                end = input(
                    "Do you want to see when the exhibits end? Enter Y or N: ")
                if (end == 'Y') or (end == 'y'):
                    list_attributes.append('E.End_Date')
                query += (', '.join(list_attributes)) + \
                    ' FROM EXHIBIT AS E '

            specifics = input(
                "Are you looking for a specific exhibit? Enter Y or N: ")
            if (specifics == 'N') or (specifics == 'n'):
                order = input(
                    "Do you want the exhibits ordered from those starting sooner to those starting later? Enter Y or N: ")
                if (order == 'Y') or (order == 'y'):
                    query += 'ORDER BY E.Start_Date ASC;'
                query += ';'
            else:
                where_conditions = []
                is_spec_name = input(
                    "Are you looking for a exhibit with a specific name? Enter Y or N: ")
                if (is_spec_name == 'Y') or (is_spec_name == 'y'):
                    spec_name = 'E.Name = "' + \
                        input(
                            "Enter the name of the exhibit you are looking for: ") + '"'
                    where_conditions.append(spec_name)
                is_spec_start = input(
                    "Are you looking for a exhibit with a specific start date? Enter Y or N: ")
                if (is_spec_start == 'Y') or (is_spec_start == 'y'):
                    spec_start = 'E.Start_Date = "' + \
                        input("Enter the start date you are looking for: ") + '"'
                    where_conditions.append(spec_start)
                is_spec_end = input(
                    "Are you looking for a exhibit with a specific end date? Enter Y or N: ")
                if (is_spec_end == 'Y') or (is_spec_end == 'y'):
                    spec_end = 'E.End_Date = "' + \
                        input("Enter the end date you are looking for: ") + '"'
                    where_conditions.append(spec_end)
                query += ' WHERE ' + (' AND '.join(where_conditions))
                order = input(
                    "Do you want the exhibits ordered from those starting sooner to those starting later? Enter Y or N: ")
                if (order == 'Y') or (order == 'y'):
                    query += ' ORDER BY E.Start_Date ASC;'
                query += ';'

            try:
                cursor.execute(f'{query}')

                attribute_names = cursor.column_names
                attributes_size = len(attribute_names)

                for i in range(attributes_size):
                    print(f'{attribute_names[i]:<25}', end='')
                print()
                print((attributes_size * 25) * '-')

                information = cursor.fetchall()
                information_size = len(information)

                for j in range(information_size):
                    for k in range(len(information[j])):
                        string = str(information[j][k])
                        print(f'{string:<25}', end='')
                    print()

                print(
                    "What would you like to do next! Please select another of the following you would like to browse:\n")

                print("1. Art Pieces")
                print("2. Art Exhibitions")
                print("3. Art Collections")
                print("4. Artists")
                print("5. I Would Like To Leave")

                choice = int(
                    input("Please enter the number of your next choice here: "))
            except:

                print(
                    "What would you like to do next! Please select another of the following you would like to browse:\n")

                print("1. Art Pieces")
                print("2. Art Exhibitions")
                print("3. Art Collections")
                print("4. Artists")
                print("5. I Would Like To Leave")

                choice = int(
                    input("Please enter the number of your next choice here: "))

            print("What would you like to do next! Please select another of the following you would like to browse:\n")

            print("1. Art Pieces")
            print("2. Art Exhibitions")
            print("3. Art Collections")
            print("4. Artists")
            print("5. I Would Like To Leave")

            choice = int(
                input("Please enter the number of your next choice here: "))

        elif (choice == 3):
            query = ''
            query += 'SELECT '

            all_info = input(
                "Do you want all the information on collections? Enter Y or N: ")
            if (all_info == 'Y') or (all == 'y'):
                query += '* FROM COLLECTION AS C '
            else:
                list_attributes = []
                name = input(
                    "Do you want to see the name of the collection? Enter Y or N: ")
                if (name == 'Y') or (name == 'y'):
                    list_attributes.append('C.Name')
                type = input(
                    "Do you want to see  the type of collection it is? Enter Y or N: ")
                if (type == 'Y') or (type == 'y'):
                    list_attributes.append('C.Type')
                description = input(
                    "Do you want to see a description of the collection? Enter Y or N: ")
                if (description == 'Y') or (description == 'y'):
                    list_attributes.append('C.Description')
                contact = input(
                    "Do you want to see a contact point of the collection? Enter Y or N: ")
                if (contact == 'Y') or (contact == 'y'):
                    list_attributes.append('C.Current_Contact_Point')
                address = input(
                    "Do you want to see the address of the collection? Enter Y or N: ")
                if (address == 'Y') or (address == 'y'):
                    list_attributes.append('C.Address')
                phone = input(
                    "Do you want to see a phone number for the collection? Enter Y or N: ")
                if (phone == 'Y') or (phone == 'y'):
                    list_attributes.append('C.Phone')
                query += (', '.join(list_attributes)) + \
                    ' FROM COLLECTION AS C '

            specifics = input(
                "Are you looking for a specific collection? Enter Y or N: ")
            if (specifics == 'N') or (specifics == 'n'):
                borrow = input(
                    "Do you want to focus on collections that have been borrowed from? Enter Y or N: ")
                if (borrow == 'Y') or (borrow == 'y'):
                    query += 'WHERE C.Name IN (SELECT B.Collection_Name FROM BORROWED AS B);'
                query += ';'
            else:
                where_conditions = []
                is_spec_name = input(
                    "Are you looking for a collection with a specific name? Enter Y or N: ")
                if (is_spec_name == 'Y') or (is_spec_name == 'y'):
                    spec_name = 'C.Name = "' + \
                        input(
                            "Enter the name of the collection you are looking for: ") + '"'
                    where_conditions.append(spec_name)
                is_spec_type = input(
                    "Are you looking for a specific type of collection? Enter Y or N: ")
                if (is_spec_type == 'Y') or (is_spec_type == 'y'):
                    spec_type = 'C.Type = "' + \
                        input("Enter the type you are looking for: ") + '"'
                    where_conditions.append(spec_type)
                is_spec_contact = input(
                    "Are you looking for a collection with a specific contact point? Enter Y or N: ")
                if (is_spec_contact == 'Y') or (is_spec_contact == 'y'):
                    spec_contact = 'C.Current_Contact_Point = "' + \
                        input("Enter the contact point you are looking for: ") + '"'
                    where_conditions.append(spec_contact)
                is_spec_address = input(
                    "Are you looking for a collection at a specific address? Enter Y or N: ")
                if (is_spec_address == 'Y') or (is_spec_address == 'y'):
                    spec_address = 'C.Address = "' + \
                        input("Enter the address you are looking for: ") + '"'
                    where_conditions.append(spec_address)
                is_spec_phone = input(
                    "Are you looking for a collection with a specific phone number? Enter Y or N: ")
                if (is_spec_phone == 'Y') or (is_spec_phone == 'y'):
                    spec_phone = 'C.Phone = "' + \
                        input("Enter the phone number you are looking for: ") + '"'
                    where_conditions.append(spec_phone)
                query += ' WHERE ' + (' AND '.join(where_conditions))
                borrow = input(
                    "Do you want to focus on collections that have been borrowed from? Enter Y or N: ")
                if (borrow == 'Y') or (borrow == 'y'):
                    query += 'AND C.Name IN (SELECT B.Collection_Name FROM BORROWED AS B);'
                query += ';'

            try:
                cursor.execute(f'{query}')

                attribute_names = cursor.column_names
                attributes_size = len(attribute_names)

                for i in range(attributes_size):
                    print(f'{attribute_names[i]:<25}', end='')
                print()
                print((attributes_size * 25) * '-')

                information = cursor.fetchall()
                information_size = len(information)

                for j in range(information_size):
                    for k in range(len(information[j])):
                        string = str(information[j][k])
                        print(f'{string:<25}', end='')
                    print()

                print(
                    "What would you like to do next! Please select another of the following you would like to browse:\n")

                print("1. Art Pieces")
                print("2. Art Exhibitions")
                print("3. Art Collections")
                print("4. Artists")
                print("5. I Would Like To Leave")

                choice = int(
                    input("Please enter the number of your next choice here: "))
            except:

                print(
                    "What would you like to do next! Please select another of the following you would like to browse:\n")

                print("1. Art Pieces")
                print("2. Art Exhibitions")
                print("3. Art Collections")
                print("4. Artists")
                print("5. I Would Like To Leave")

                choice = int(
                    input("Please enter the number of your next choice here: "))

            print("What would you like to do next! Please select another of the following you would like to browse:\n")

            print("1. Art Pieces")
            print("2. Art Exhibitions")
            print("3. Art Collections")
            print("4. Artists")
            print("5. I Would Like To Leave")

            choice = int(
                input("Please enter the number of your next choice here: "))

        elif (choice == 4):
            query = ''
            query += 'SELECT '

            all_info = input(
                "Do you want all the information on all the artists? Enter Y or N: ")
            if (all_info == 'Y') or (all == 'y'):
                join = input(
                    "Would you like to see some brief information on the art objects contributed by the artist")
                if (join == 'Y') or (join == 'y'):
                    query += 'A.Name, A.Date_Born, A.Date_Died, A.Description, A.Origin_Country, A.Main_Style, AO.Id_no, AO.year, AO.Title, AO.Description '
                    query += 'FROM ARTIST AS A LEFT JOIN ART_OBJECTS AS AO ON AO.Artist=A.Name '
                query += '* FROM ARTIST AS A '

            else:
                list_attributes = []
                name = input(
                    "Do you want to see the name of the artist? Enter Y or N: ")
                if (name == 'Y') or (name == 'y'):
                    list_attributes.append('A.Name')
                born = input(
                    "Do you want to see the date the artist was born? Enter Y or N: ")
                if (born == 'Y') or (born == 'y'):
                    list_attributes.append('A.Date_Born')
                death = input(
                    "Do you want to see the date the artist died? Enter Y or N: ")
                if (death == 'Y') or (death == 'y'):
                    list_attributes.append('A.Date_Died')
                description = input(
                    "Do you want to see a description of the artist? Enter Y or N: ")
                if (description == 'Y') or (description == 'y'):
                    list_attributes.append('A.Description')
                origin = input(
                    "Do you want to see the originatiing country of the artist? Enter Y or N: ")
                if (origin == 'Y') or (origin == 'y'):
                    list_attributes.append('A.Origin_Country')
                style = input(
                    "Do you want to see the main style of the artist? Enter Y or N: ")
                if (style == 'Y') or (style == 'y'):
                    list_attributes.append('A.Main_Style')
                query += (', '.join(list_attributes))

                join = input(
                    "Would you like to see some brief information on the art objects contributed by the artist: ")
                if (join == 'Y') or (join == 'y'):
                    query += ', AO.Id_no, AO.year, AO.Title, AO.Description '
                    query += 'FROM ARTIST AS A LEFT JOIN ART_OBJECTS AS AO ON AO.Artist=A.Name '
                else:
                    query += ' FROM ARTIST AS A '

            specifics = input(
                "Are you looking for a specific artist? Enter Y or N: ")
            if (specifics == 'N') or (specifics == 'n'):
                query += ';'
            else:
                where_conditions = []
                is_spec_name = input(
                    "Are you looking for a artist with a specific name? Enter Y or N: ")
                if (is_spec_name == 'Y') or (is_spec_name == 'y'):
                    spec_name = 'A.Name = "' + \
                        input(
                            "Enter the name of the artist you are looking for: ") + '"'
                    where_conditions.append(spec_name)
                is_spec_born = input(
                    "Are you looking for an artist with a specific birth date? Enter Y or N: ")
                if (is_spec_born == 'Y') or (is_spec_born == 'y'):
                    spec_born = 'A.Date_Born = "' + \
                        input("Enter the birth date you are looking for: ") + '"'
                    where_conditions.append(spec_born)
                is_spec_death = input(
                    "Are you looking for an artist with a specific death date? Enter Y or N: ")
                if (is_spec_death == 'Y') or (is_spec_death == 'y'):
                    spec_death = 'A.Date_Died = "' + \
                        input("Enter the death date you are looking for: ") + '"'
                    where_conditions.append(spec_death)
                is_spec_origin = input(
                    "Are you looking for an artist originating somewhere specific? Enter Y or N: ")
                if (is_spec_origin == 'Y') or (is_spec_origin == 'y'):
                    spec_origin = 'A.Origin_Country = "' + \
                        input(
                            "Enter the country of origin you are looking for: ") + '"'
                    where_conditions.append(spec_origin)
                is_spec_style = input(
                    "Are you looking for an artist with a specific main style? Enter Y or N: ")
                if (is_spec_style == 'Y') or (is_spec_style == 'y'):
                    spec_style = 'A.Main_Style = "' + \
                        input("Enter the main style you are looking for: ") + '"'
                    where_conditions.append(spec_style)
                query += ' WHERE ' + (' AND '.join(where_conditions)) + ';'

            try:
                cursor.execute(f'{query}')

                attribute_names = cursor.column_names
                attributes_size = len(attribute_names)

                for i in range(attributes_size):
                    print(f'{attribute_names[i]:<25}', end='')
                print()
                print((attributes_size * 25) * '-')

                information = cursor.fetchall()
                information_size = len(information)

                for j in range(information_size):
                    for k in range(len(information[j])):
                        string = str(information[j][k])
                        print(f'{string:<25}', end='')
                    print()

                print(
                    "What would you like to do next! Please select another of the following you would like to browse:\n")

                print("1. Art Pieces")
                print("2. Art Exhibitions")
                print("3. Art Collections")
                print("4. Artists")
                print("5. I Would Like To Leave")

                choice = int(
                    input("Please enter the number of your next choice here: "))
            except:

                print(
                    "What would you like to do next! Please select another of the following you would like to browse:\n")

                print("1. Art Pieces")
                print("2. Art Exhibitions")
                print("3. Art Collections")
                print("4. Artists")
                print("5. I Would Like To Leave")

                choice = int(
                    input("Please enter the number of your next choice here: "))

        elif (5 < choice < 1):
            print("That Is Not A Valid Option! Please Try Again!")
            choice = int(
                input("Please enter the number of your choice here: "))

    cnx.close()
    return
