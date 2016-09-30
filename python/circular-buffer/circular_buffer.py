#implement a circular buffer, with read, write and clear methods
#also implement an overwrite method that ignores BufferFullException, and reset read position?

class BufferFullException(Exception):
    '''Cannot Write to a full buffer'''

class BufferEmptyException(Exception):
    '''Cannot Read from an empty buffer'''

class CircularBuffer:
    def __init__(self,size):
        assert size > 0, 'Buffer size must be greater than 0'
        self._size = size
        self._init_buffer(self._size)

    def _init_buffer(self,size):
        self._buffer = [[]]*size
        self._rpos = 0
        self._wpos = 0

    def clear(self):
        self._init_buffer(self._size)

    def write(self,data):
        if self._buffer[self._wpos] != []:
            raise BufferFullException('Cannot write: buffer is full')
        self._buffer[self._wpos] = [data]
        self._wpos = (self._wpos+1)%self._size

    def read(self):
        if self._buffer[self._rpos] == []:
            raise BufferEmptyException('Cannot read: buffer is empty')
        data = self._buffer[self._rpos].pop()
        self._rpos = (self._rpos+1)%self._size
        return data


    def overwrite(self,data):
        self._buffer[self._wpos] = [data]
        self._wpos = (self._wpos+1)%self._size
        self._rpos = (self._wpos)
