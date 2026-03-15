import hashlib


def generate_cache_key(data):

    text = f"{data['make']}-{data['model']}-{data['year']}-{data['mileage']}-{data['question']}"

    return hashlib.md5(text.encode()).hexdigest()
