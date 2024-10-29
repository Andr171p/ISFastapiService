from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


print(verify_password(
    plain_password='7777',
    hashed_password='$2b$12$EFZuo.tdDjii9gX0u79nLuWg4OlIGEXpa2tc0I4otD9JZBwcqhBe.'
))
