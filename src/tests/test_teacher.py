from pycli.teacher import Teacher


def test_teacher():
    tony_teacher = Teacher("Antonel", "Pazargic")
    print(f"Teacher: {tony_teacher}")

    assert tony_teacher.first_name == "Antonel"
    assert tony_teacher.last_name == "Pazargic"
