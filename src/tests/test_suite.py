import pendulum as pdl


def test_my_age():
    tonys_bd = pdl.date(year=1970, month=1, day=29)
    assert tonys_bd.age == 51
    print(tonys_bd.format("[Hi! My birthdate] DD MMMM, YYYY"))
