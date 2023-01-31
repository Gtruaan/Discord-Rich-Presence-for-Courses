import os
import sys
import threading
import time
import utils
from presence import PresenceHandler


def run(handler: PresenceHandler, lock: threading.Lock):

    update_interval = utils.get("update_interval")

    while True:
        with lock:
            if not handler.update_presence():
                print("Something went wrong when updating your presence")

        time.sleep(update_interval)


# CLI functions

class CLI:
    """
    Operates everything related to the CLI and managing the Presence Handler
    """

    def __init__(self, handler: PresenceHandler, lock: threading.Lock,
                 courses: list, statuses: list):
        self.handler = handler
        self.lock = lock
        self.courses = courses
        self.statuses = statuses

    def menu_loop(self):
        while True:
            os.system("cls")

            print("What do you want to do:\n[0] Change course" +
                  "\n[1] Change status\n[2] Stop")

            ans = utils.r_input(range(3))

            if ans == 0:
                new_course = self.prompt_course()

                with self.lock:
                    self.handler.set_details(
                        "Studying {}".format(new_course["name"]),
                        new_course["code"]
                    )

            elif ans == 1:
                new_status = self.prompt_status()

                with self.lock:
                    self, handler.set_image(
                        new_status["image"],
                        new_status["quote"]
                    )

            elif ans == 2:
                return sys.exit()

    def prompt_course(self):
        os.system("cls")
        print("Select your course:")

        for i, course in enumerate(self.courses):
            print(f"{[i]} {course['name']}")

        ans = utils.r_input(range(len(self.courses)))

        return self.courses[ans]

    def prompt_status(self):
        os.system("cls")
        print("Select your status:")

        for i, status in enumerate(self.statuses):
            print(f"{[i]} {status['quote']}")

        ans = utils.r_input(range(len(self.statuses)))

        return self.statuses[ans]


if __name__ == "__main__":

    client_id = utils.get("app_id")
    course_list = utils.get("course")
    status_list = utils.get("status")

    handler = PresenceHandler(client_id=client_id)
    information_lock = threading.Lock()

    handler_thread = threading.Thread(
        target=run, args=(handler, information_lock),
        daemon=True
    )

    menu = CLI(handler, information_lock, course_list, status_list)

    if handler.init_presence():
        handler_thread.start()
        menu.menu_loop()
