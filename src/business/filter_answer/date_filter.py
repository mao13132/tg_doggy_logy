# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime


def date_filter(answer):
    result = False

    try:
        result = datetime.strptime(answer, "%d.%m.%Y")
    except:
        pass

    if result:
        return result

    try:
        result = datetime.strptime(answer, "%d %m %Y")
    except:
        pass

    if result:
        return result

    try:
        result = datetime.strptime(answer, "%d_%m_%Y")
    except:
        pass

    if result:
        return result

    try:
        result = datetime.strptime(answer, "%d,%m,%Y")
    except:
        pass

    if result:
        return result

    return False


