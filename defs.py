def set_state_mailing():
    f = open("state.cfg", "w")
    f.write("mailing")
    f.close()


def set_state_default():
    f = open("state.cfg", "w")
    f.write("default")
    f.close()


def get_state():
    f = open("state.cfg", "r")
    temp = f.read()
    f.close()
    return temp
