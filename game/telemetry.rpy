init python in telemetry:
    # Historical release safety patch: telemetry is disabled in this build.
    # Keep the namespace and function signatures used by existing game scripts.
    host = ""
    project_id = ""
    game_id = ""
    collected_data = {}
    sessions = 1
    last_session_length = 0
    session_blocks = []
    status = ""

    def init():
        global host, project_id, game_id, collected_data, sessions, last_session_length, session_blocks, status
        host = ""
        project_id = ""
        game_id = ""
        collected_data = {}
        sessions = 1
        last_session_length = 0
        session_blocks = []
        status = ""

    def setup():
        return

    def _setup():
        return

    def collect():
        return

    def sync():
        return

    def _sync(available_data, url):
        return

    def check_internet():
        return False

    def resume():
        return

    def end(name):
        return

    def _end(name, play_time, session, url):
        return

    def submit_form():
        return

    def _submit_form(available_data, url):
        return
