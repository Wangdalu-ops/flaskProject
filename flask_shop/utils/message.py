status_msg = {
    200: '成功',

}


def to_dict_msg(status=200, data=None, msg=None):
    return {
        'status': status,
        'data': data,
        'msg': msg if msg else status_msg.get(status)
    }