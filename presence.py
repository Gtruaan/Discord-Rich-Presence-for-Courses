from pypresence import Presence
import utils


class PresenceHandler:
    """
    Simple interface for the use of PyPresence
    """

    def __init__(self, client_id: str):
        """
        Args:
            client_id from the Discord Developer Portal
            update_interval (optional): frequency in which thread updates
        """
        self.RPC = Presence(client_id=client_id)

        name = utils.get("name")

        # Initialize default values
        self.state = "Nothing"
        self.details = "Nothingness"
        self.large_image = utils.get("default_image")
        self.large_text = utils.get("default_text")
        self.small_image = utils.get("verification_image")
        self.small_text = utils.get("verification_text").format(name)

    def init_presence(self) -> bool:
        """
        Returns boolean
        True if connected succesfully, else False
        """
        try:
            self.RPC.connect()
        except Exception as e:
            print(e)
            return False

        return True

    def update_presence(self) -> bool:
        """
        Returns boolean
        True if update was succesful, else False
        """
        try:
            self.RPC.update(
                state=self.state, details=self.details,
                large_image=self.large_image, large_text=self.large_text,
                small_image=self.small_image, small_text=self.small_text
            )
        # TODO: Specify exception type
        except Exception as e:
            print(e)
            return False

        return True

    def set_details(self, state: str, details: str):
        """
        Evil hehehe
        """
        self.state = state
        self.details = details

    def set_image(self, img_url: str, img_text: str):
        """
        Hehehehe
        """
        self.large_image = img_url
        self.large_text = img_text
