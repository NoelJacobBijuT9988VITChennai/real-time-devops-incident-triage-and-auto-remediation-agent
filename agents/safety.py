"""
Allow only approved actions.
"""

ALLOWED_ACTIONS = [

    "restart_deployment",
    "scale_deployment"
]

def validate(action):

    return (
        action
        in ALLOWED_ACTIONS
    )