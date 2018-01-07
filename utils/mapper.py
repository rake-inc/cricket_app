import logging


def re_map_query_params(query_params_dict):
    result = dict()
    try:
        for key in dict(query_params_dict).keys():
            result[key] = dict(query_params_dict).get(key).pop()
    except Exception as e:
        logging.error("MAPPER RE_MAP_QUERY_PARAMS EXCEPTION REACHED %s" % e)
    return result
