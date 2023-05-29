import sys
from importlib import reload

import BI
import BII
#import gg

if __name__ == '__main__':
    print(list(sys.modules))
    BI.x = 12
    BII.show()
    BI.A.x = 12
    BII.show()
    reload(BI.A)
    BII.show()
    #gg.#error
