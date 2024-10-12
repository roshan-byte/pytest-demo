import connection as c


def test_fun():
    con_obj = c.connect('13.60.195.224', 'ubuntu')

    stdin, stdout, stderr = con_obj.exec_command("ip a")
    print(stdout.read().decode())