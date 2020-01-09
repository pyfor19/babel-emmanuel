# YEAR

import datetime


def controller_input():

    dates_to_test = {
        ("01/01/1701", 18),
        ("30/03/0019", 1),
        ("29/02/1700", 17),
        ("18/03/2011", 21),
        ("12/12/1200", 12),
        ("25/09/0403", 5),
        ("01/06/0000", None),
        ("29/02/1904", 20),
    }

    for i in dates_to_test:
        print("- " * 31)
        century = get_century_from_string(i[0], True)
        print(f"Expected century is {i[1]}")
        if not century:
            print("FAILED !")
        elif century == i[1]:
            print("PASS")
        else:
            print("FAILED")


def get_century_from_string(date_string, is_verbose=False):
    try:
        dt = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        return get_century_from_dt(dt, is_verbose)
    except Exception as e:
        print(f"error in date {date_string} -> {str(e)}")
        return None


def get_century_from_dt(dt, is_verbose=False):
    try:
        if is_verbose:

            print(f"Day {dt.day} Month {dt.month} Year {dt.year}")

        tmp_century = (dt.year // 100) if dt.year >= 100 else 1
        beg_century = (tmp_century * 100) + 1
        end_century = (tmp_century + 1) * 100

        if is_verbose:
            print(beg_century)
            print(end_century)

        dt_begcentury = datetime.date(beg_century, 1, 1)
        dt_endcentury = datetime.date(end_century, 12, 31)
        if dt_begcentury <= dt <= dt_endcentury:
            tmp_century += 1

        if is_verbose:
            print(f"{dt_begcentury} < {dt} < {dt_endcentury}")
            print(f"in century : {tmp_century}")

    except Exception as e:
        print(f"error in date {str(e)}")
        return None

    return tmp_century


if __name__ == "__main__":
    controller_input()
