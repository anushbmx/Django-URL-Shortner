import string
import datetime
from django.urls import reverse
from django.conf import settings
from django.db import models


_char_map = string.ascii_letters + string.digits


class Links(models.Model):
    link = models.URLField()
    hits = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    # Status
    created = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True, null=False)

    def __repr__(self):
        return '<Link (Hits %s): %s>' % (self.hits, self.link)

    def __str__(self):
        return '%s : %s' % (self.id, self.short_link)

    def encode(self):
        """
        Encode a positive number into string
        """
        num = str(datetime.date.today().year) + str(self.id).zfill(4)
        num = int(num)
        alphabet = _char_map

        if num == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            num, rem = divmod(num, base)
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    @staticmethod
    def decode(_str):
        """
        Decode the encoded string into the number
        """
        alphabet = _char_map
        base = len(alphabet)
        strlen = len(_str)
        num = 0

        idx = 0
        for char in _str:
            power = (strlen - (idx + 1))
            num += alphabet.index(char) * (base ** power)
            idx += 1

        num = str(num)
        link_id = num[4:]
        return int(link_id)
