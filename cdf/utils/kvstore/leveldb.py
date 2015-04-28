from __future__ import absolute_import

import logging
import leveldb

from . import base
from . import constants


logger = logging.getLogger(__name__)


class LevelDB(base.LevelDBBase):
    def open(self, **configs):
        """Open the DB
        """
        self.db = leveldb.LevelDB(self.path, create_if_missing=True, **configs)

    def close(self):
        """Close the DB
        """
        self._check()
        del self.db
        self.db = None

    def batch_write(self, kv_stream, batch_size=constants.DEFAULT_BATCH_SIZE):
        """Batch write a key-value stream into the DB

        Note it's generally better to configure the DB with large write buffer
        `reopen` can be used upon batch write to change the configuration

        :param kv_stream: a key-value pair stream
        :param batch_size: size of each write batch
        """
        self._check()
        batch = leveldb.WriteBatch()

        for count, (k, v) in enumerate(kv_stream):
            batch.Put(str(k), str(v))
            if count != 0 and count % batch_size == 0:
                self.db.Write(batch)
                batch = leveldb.WriteBatch()
                logger.debug(
                    "Put {} records in DB {}".format(count, self.path))

        self.db.Write(batch)

    def iterator(self):
        """Returns an iterator for key-ordered iteration
        """
        self._check()
        # iteration means we do a full pass on the data
        # but no random lookup, cache is not relevant in
        # this case
        return self.db.RangeIter(fill_cache=False)

    def put(self, key, value):
        """Put a key-value pair
        """
        self._check()
        self.db.Put(key, value)

    def get(self, key):
        """Get a value from a key
        """
        self._check()
        return self.db.Get(key)

    def __del__(self):
        self.destroy()
