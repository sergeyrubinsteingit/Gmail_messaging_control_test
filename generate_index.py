###################################################
# A script to generate random hash and index

gener_hash_: str


def generate_index(selected_priority):
    from start_test_amy import send_mail
    from all_imports_amy import random, time
    print(selected_priority)
    global gener_hash_
    #  md5-hash is just a 128-bit value;
    gener_hash_ = str(random.getrandbits(128))[:10] #  stringed to let limitate a number of digits to 10
    # This hash plays a role of the unique id for mail, so that each mail in gmail is displayed
    # as separate entry and not into stack.
    priority_label: list = [0.0, 0.1, 1.0]
    priority_lbl: float = 0.0
    if selected_priority == "High":
        priority_lbl = priority_label[0]
    elif selected_priority == "Medium":
        priority_lbl = priority_label[1]
    elif selected_priority == "Low":
        priority_lbl = priority_label[2]

    time.sleep(2)
    send_mail(gener_hash_, selected_priority, priority_lbl)

