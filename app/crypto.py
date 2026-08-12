from coincurve import PrivateKey


def generate_keypair():
    private_key = PrivateKey()
    public_key = private_key.public_key
    return {
        "private_key": private_key,
        "public_key": public_key,
    }


def sign(private_key: PrivateKey, message: bytes):
        signature = private_key.sign(message=message)
        return signature


def verify(public_key, message: bytes, signature: bytes):
    pass
