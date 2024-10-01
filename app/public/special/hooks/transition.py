from reactpy import use_state


def use_transition():
    is_pending, set_is_pending = use_state(False)

    def start_transition(callback):
        set_is_pending(True)
        callback()
        set_is_pending(False)

    return is_pending, start_transition
