import time, hashlib, random

Block = lambda index, previous_block, previous_hash, timestamp, data: {
    'index' : index,
    'previous_block' : previous_block,
    'previous_hash' : previous_hash,
    'timestamp' : timestamp,
    'data' : data,
    'hash' : hashlib.sha256(str(random.random())).hexdigest()
}

first_block = lambda : Block (0, 0, None, int(time.time()), 'genesis block')

next_block = lambda block_data: Block (
    block_data['index'] + 1,
    block_data['previous_block'] + 1,
    block_data['hash'],
    int(time.time()),
    "new data" + str(block_data['index'] + 1)
)
