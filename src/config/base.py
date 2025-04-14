from dataclasses import dataclass

from environs import Env

env = Env()


@dataclass
class OpenTelemetryConfig:
    service_name: str
    otlp_endpoint: str
    environment: str


class BaseConfig:
    SERVICE_NAME = env("SERVICE_NAME", "sealify")
    ENVIRONMENT = env("ENVIRONMENT", "local")

    #
    # Logging config
    #
    LOG_LEVEL = env("LOG_LEVEL", "INFO")
    LOG_FORMAT = env(
        "LOG_FORMAT",
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    #
    # OpenTelemetry config
    #
    OTEL_OTLP_ENDPOINT = env("OTEL_OTLP_ENDPOINT", "http://localhost:4317")

    #
    # AWS config
    #

    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", "test")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", "test")
    AWS_REGION_NAME = env("AWS_REGION_NAME", "us-east-1")
    AWS_ENDPOINT_URL = env("AWS_ENDPOINT_URL", "http://localstack:4566")

    #
    # Timezone
    #

    DEFAULT_TIMEZONE = env("DEFAULT_TIMEZONE", "America/Guayaquil")

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
    # Keytool command
    #

    KEYTOOL_COMMAND = env("KEYTOOL_COMMAND", "")

    #
    # Fernet
    #

    FERNET_KEY = env("FERNET_KEY", "gMt0dT-y1KKIb3hRYAKUlaKIL8vPm_75YMXrTu6Ovxg=")

    #
    # Admins
    #

    ADMINS = ["a@example.com", "b@example.com", "c@example.com", "d@example.com"]

    def get_otel_config(self) -> OpenTelemetryConfig:
        return OpenTelemetryConfig(
            service_name=self.SERVICE_NAME,
            otlp_endpoint=self.OTEL_OTLP_ENDPOINT,
            environment=self.ENVIRONMENT,
        )
