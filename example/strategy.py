from abc import abstractmethod
from typing import List


class UpgradeStrategy:
    @abstractmethod
    def enumerate_asgs(self) -> List[str]:
        pass

    @abstractmethod
    def start_upgrade(self, asg_id: str) -> bool:
        pass

    @abstractmethod
    def get_upgrade_status(self, asg_id: str) -> bool:
        pass

    @abstractmethod
    def cancel_upgrade(self, asg_id: str) -> bool:
        pass
