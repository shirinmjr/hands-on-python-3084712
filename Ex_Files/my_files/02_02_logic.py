# This script sets the current environment based on the ENV_NAME environment variable. If the variable is not set, it defaults to DEVELOPMENT. It then prints out which environment is currently active based on the value of current_env.
# To set the ENV_NAME environment variable, you can use the following command in your terminal:
# export ENV_NAME=development

import os
# set the current environment based on the ENV_NAME environment variable, defaulting to DEVELOPMENT if not set
DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"
# set the current environment based on the ENV_NAME environment variable, defaulting to DEVELOPMENT if not set
current_env = os.environ.get("ENV_NAME", DEVELOPMENT)
# check the value of current_env and print out which environment is currently active
if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env == CODE_SPACE:
    print("Code Space environment")
elif current_env == LOCAL:
    print("Local environment")
else:
    print("Unknown environment")

print("=================")