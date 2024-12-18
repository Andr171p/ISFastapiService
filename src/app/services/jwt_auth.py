import jwt

from typing import Any

from src.config import settings


def encode_jwt(
        payload: dict[str, Any],
        private_key: str = settings.auth_jwt.private_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm
) -> str:
    encoded = jwt.encode(
        payload=payload,
        key=private_key,
        algorithm=algorithm
    )
    return encoded


def decode_jwt(
        token: str | bytes,
        public_key: str = settings.auth_jwt.public_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm
) -> Any:
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm]
    )
    return decoded
