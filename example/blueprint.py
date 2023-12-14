from typing import Optional
from flask import Blueprint, abort

from .strategy import UpgradeStrategy

manager = Blueprint('manager', __name__)

_upgrade_strategy: Optional[UpgradeStrategy] = None

def set_upgrade_strategy(instance: UpgradeStrategy):
    global _upgrade_strategy
    _upgrade_strategy = instance

@manager.route('/')
def list():
    if _upgrade_strategy is None:
        abort(500)
        raise

    return {'asgs': _upgrade_strategy.enumerate_asgs()}


@manager.route('/upgrade/<asg_id>', methods=['POST'])
def start_upgrade(asg_id: str):
    if _upgrade_strategy is None:
        abort(500)
        raise

    return {'status': _upgrade_strategy.start_upgrade(asg_id)}


@manager.route('/upgrade/<asg_id>', methods=['DELETE'])
def stop_upgrade(asg_id: str):
    if _upgrade_strategy is None:
        abort(500)
        raise

    return {'status': _upgrade_strategy.cancel_upgrade(asg_id)}

@manager.route('/upgrade/<asg_id>', methods=['GET'])
def upgrade_status(asg_id: str):
    if _upgrade_strategy is None:
        abort(500)
        raise

    return {'status': _upgrade_strategy.get_upgrade_status(asg_id)}

