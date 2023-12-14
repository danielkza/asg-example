from typing import List
from .strategy import UpgradeStrategy

class AsgUpgradeStrategy(UpgradeStrategy):
    def __init__(self) -> None:
        self.upgrading = set()

    def enumerate_asg(self) -> List[str]:
        return ['hello', 'world']

    def start_upgrade(self, asg_id: str) -> bool:
        print(f'Started upgrade for asg: {asg_id}')
        self.upgrading.add(asg_id)
        return True

    def get_upgrade_status(self, asg_id: str) -> bool:
        return asg_id in self.upgrading

    def cancel_upgrade(self, asg_id: str) -> bool:
        if asg_id in self.upgrading:
            print(f'Cancelling upgrade for asg: {asg_id}')
            self.upgrading.remove(asg_id)
            return True

        return False
