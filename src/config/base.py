from environs import Env

env = Env()


class BaseConfig:
    ENVIRONMENT = env("ENVIRONMENT", "local")

    #
    # AWS config
    #

    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", "test")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", "test")
    AWS_REGION_NAME = env("AWS_REGION_NAME", "us-east-1")
    AWS_ENDPOINT_URL = env("AWS_ENDPOINT_URL", "http://localstack:4566")

    #
    # JWT config
    #

    JWT_SECRET_KEY = env(
        "JWT_SECRET_KEY",
        "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
    )
    JWT_ALGORITHM = env("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = env.int("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30)

    #
    # Admins
    #

    ADMINS = ["a@example.com", "b@example.com", "c@example.com", "d@example.com"]
