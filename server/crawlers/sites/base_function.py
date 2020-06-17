from utils.Constants import LIMIT_ALL
from utils.HTTPUtils import HTTPUtils
import logging
logger = logging.getLogger('crawlers')


class BaseFunction:
    def __init__(self):
        pass

    @classmethod
    def fetch_all_xml(cls, limit, source_code, channel_list, save_func):
        process_limit = limit if limit != LIMIT_ALL else -1
        process_count = 0
        is_stopped = False
        logger.debug("---------- [{}] Processing {} items ----------"
                     .format(source_code, process_limit if process_limit >= 0 else "ALL"))
        for channel in channel_list:
            if is_stopped:
                break
            logger.debug('[{}] Process channel "{}"'.format(source_code, channel['name']))
            xml_object = HTTPUtils.get_xml_response(channel['url'])
            if not xml_object:
                continue
            for element in xml_object.iter('item'):
                if is_stopped:
                    break
                process_count += 1
                is_stopped = (process_limit >= 0) and (process_count >= process_limit)
                logger.debug('[{}] Process item {}'.format(source_code, process_count))
                save_func(element)