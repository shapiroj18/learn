import os
from datetime import datetime
from glob import glob

# def add_files():

#     for i in os.listdir('/Users/jonathanshapiro/Desktop/phish albums'):
#         position = i.find("_")
#         title = f"{i[:position]}*"

#         if not glob(f'/Users/jonathanshapiro/Desktop/Git/phish-bot/app/static/img/livephish_logos/{title}'):
#             os.rename(i, f'/Users/jonathanshapiro/Desktop/Git/phish-bot/app/static/img/livephish_logos/{i}')


def rename_files():
    for i in os.listdir(
        "/Users/jonathanshapiro/Desktop/Git/phish-bot/app/static/img/livephish_logos"
    ):
        if i[:9] == "livephish":
            position = i.find("_")
            date = i[9:position]

            date_obj = datetime.strptime(date, "%m%d%y")
            new_date_str = date_obj.strftime("%Y-%m-%d")

            os.rename(
                f"/Users/jonathanshapiro/Desktop/Git/phish-bot/app/static/img/livephish_logos/{i}",
                f"/Users/jonathanshapiro/Desktop/Git/phish-bot/app/static/img/livephish_logos/{new_date_str}.jpg",
            )


# Function to rename multiple files
def main():

    # for i in os.listdir(os.path.dirname(os.path.realpath(__file__))):

    # if i.find('_') != 8:

    #     date = i[:8]

    #     date_obj = datetime.strptime(date, "%Y%m%d")
    #     new_date_str = date_obj.strftime("%-m%-d%y")

    #     newname = f"livephish{new_date_str}" + i[8:]

    #     os.rename(i, newname)

    # if i.find('_') == 10:

    #     date = i[:10]

    #     date_obj = datetime.strptime(date, "%Y-%m-%d")
    #     new_date_str = date_obj.strftime("%-m%-d%y")

    #     newname = f"livephish{new_date_str}" + i[10:]

    #     os.rename(i, newname)

    # add_files()

    rename_files()


if __name__ == "__main__":

    main()
