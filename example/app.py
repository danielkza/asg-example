from flask import Flask

from . import asg_strategy
from . import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint.manager)

strategy = asg_strategy.AsgUpgradeStrategy()
blueprint.set_upgrade_strategy(strategy)
