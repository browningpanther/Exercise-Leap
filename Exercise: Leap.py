def is_leap(year):
    # A leap year is divisible by 4
    # but not by 100, unless it is also divisible by 400
    if year 4 == 0:
        if year 100 == 0:
            if year  400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Example usage:
year = int(input("Enter a year: "))
print(is_leap(year))
