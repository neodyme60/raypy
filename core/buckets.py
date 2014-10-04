from enum import Enum
import random


class BucketOrderSortType(Enum):
    Row = 0
    Column = 1
    Diagonal = 2
    Spiral = 3
    Hilbert = 4
    Random = 5


class BucketOrder:
    def __init__(self, width: int, height: int, sort_order: BucketOrderSortType):
        self.buckets_orders = []
        self.width = width
        self.height = height
        self.sort_order = sort_order

    @staticmethod
    def create(width: int, height: int, sort_order: BucketOrderSortType):
        if sort_order == BucketOrderSortType.Row:
            return RowBucketOrder(width, height)
        if sort_order == BucketOrderSortType.Column:
            return ColumnBucketOrder(width, height)
        elif sort_order == BucketOrderSortType.Random:
            return RandomBucketOrder(width, height)
        elif sort_order == BucketOrderSortType.Hilbert:
            return HilbertBucketOrder(width, height)
        elif sort_order == BucketOrderSortType.Diagonal:
            return DiagonalBucketOrder(width, height)
        else:
            return RandomBucketOrder(width, height)


class BucketExtend:
    def __init__(self, start_x: int, start_y: int, end_x: int, end_y: int):
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y

    def get_width(self):
        return self.end_x - self.start_x

    def get_height(self):
        return self.end_y - self.start_y

    def get_is_null(self):
        return self.start_x == self.end_x and self.start_y == self.end_y


class BucketOrderInfo:
    def __init__(self, bucket_order_type: BucketOrderSortType, width: int, height: int):
        self.bucket_order_type = bucket_order_type
        self.width = width
        self.height = height


class RowBucketOrder(BucketOrder):
    def __init__(self, width: int, height: int):

        BucketOrder.__init__(self, width, height, BucketOrderSortType.Row)

        for i in range(self.height * self.width):
            by = i // self.width
            bx = i % self.width
            if (by & 1) == 1:
                bx = self.width - 1 - bx
            self.buckets_orders.append(bx + by * self.width)


class ColumnBucketOrder(BucketOrder):
    def __init__(self, width: int, height: int):

        BucketOrder.__init__(self, width, height, BucketOrderSortType.Column)

        for i in range(self.height * self.width):
            by = i // self.width
            bx = i % self.width
            if (by & 1) == 1:
                bx = self.width - 1 - bx
            self.buckets_orders.append(by + bx * self.width)


class RandomBucketOrder(BucketOrder):
    def __init__(self, width: int, height: int):

        BucketOrder.__init__(self, width, height, BucketOrderSortType.Random)

        for i in range(self.height * self.width):
            by = i // self.width
            bx = i % self.width
            if (by & 1) == 1:
                bx = self.width - 1 - bx
            self.buckets_orders.append(bx + by * self.width)

        random.shuffle(self.buckets_orders)


class DiagonalBucketOrder(BucketOrder):
    def __init__(self, width: int, height: int):

        BucketOrder.__init__(self, width, height, BucketOrderSortType.Random)

        x = y = 0
        nx = 1
        ny = 0
        for i in range(self.height * self.width):
            self.buckets_orders.append(x + y * self.width)

            while True:
                if y == ny:
                    y = 0
                    x = nx
                    ny += 1
                    nx += 1
                else:
                    x -= 1
                    y += 1
                if not ((y >= height or x >= width) and i != (width * height - 1)):
                    break


class HilbertBucketOrder(BucketOrder):
    def __init__(self, width: int, height: int):

        BucketOrder.__init__(self, width, height, BucketOrderSortType.Random)

        hi = hn = 0
        while ((1 << hn) < width or (1 << hn) < height) and hn < 16:
            hn += 1
        hnn = 1 << (2 * hn)
        n = width * height
        for i in range(n):
            hx = 0
            hy = 0
            while True:
                s = hi
                s |= 0x55555555 << (2 * hn)
                sr = (s >> 1) & 0x55555555
                cs = ((s & 0x55555555) + sr) ^ 0x55555555
                cs ^= cs >> 2
                cs ^= cs >> 4
                cs ^= cs >> 8
                cs ^= cs >> 16
                swap = cs & 0x55555555
                comp = (cs >> 1) & 0x55555555
                t = (s & swap) ^ comp
                s = s ^ sr ^ t ^ (t << 1)
                s &= (1 << 2 * hn) - 1
                t = (s ^ (s >> 1)) & 0x22222222
                s = s ^ t ^ (t << 1)
                t = (s ^ (s >> 2)) & 0x0C0C0C0C
                s = s ^ t ^ (t << 2)
                t = (s ^ (s >> 4)) & 0x00F000F0
                s = s ^ t ^ (t << 4)
                t = (s ^ (s >> 8)) & 0x0000FF00
                s = s ^ t ^ (t << 8)
                hx = s >> 16
                hy = s & 0xFFFF
                hi += 1
                if not ((hx >= width or hy >= height or hx < 0 or hy < 0) and hi < hnn):
                    break
            self.buckets_orders.append(hx + hy * width)
