from pycli.teacher import Teacher


def test_teacher():
    tony_teacher = Teacher("Antonel", "Pazargic")
    print(f"Teacher: {tony_teacher}")

    assert "Antonel" == tony_teacher.first_name
    assert "Pazargic" == tony_teacher.last_name
