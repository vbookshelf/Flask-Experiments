
def read_tb_file():

    """
    Reads the csv file containing the info on each image.
    :return: A list of dicts e.g. [{}, {}, ...]
    """

    with open('tb_all_images.csv') as file:
        content = file.readlines()

    # Remove the newline character that's at the end of each row
    file_rows = [x.strip() for x in content]

    # Remove the header row
    file_rows = file_rows[1:]

    #print(file_rows)

    data_list = []

    for item in file_rows:

        # split by the comma
        item_list = item.split(',')

        # Convert to a dict
        my_dict = {
            'image_id': int(item_list[0]),
            'image_fname': item_list[1],
            'diagnosis': item_list[2],
            'binary_target': int(item_list[3])
        }

        # Create a list of dicts.
        # This will be our database.
        data_list.append(my_dict)

    return data_list

